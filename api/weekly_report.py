import json
import os
from http.server import BaseHTTPRequestHandler

from services import reports, sheets
from services.telegram import TelegramClient


def json_response(handler, status, payload):
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


def authorized(headers):
    secret = os.environ.get("CRON_SECRET")
    if not secret:
        return True
    return headers.get("Authorization") == f"Bearer {secret}"


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if not authorized(self.headers):
            json_response(self, 401, {"ok": False, "error": "Unauthorized"})
            return
        tz_name = os.environ.get("TIMEZONE", "Europe/Moscow")
        admin_chat_id = os.environ.get("ADMIN_CHAT_ID")
        if not admin_chat_id:
            json_response(self, 500, {"ok": False, "error": "ADMIN_CHAT_ID is not configured"})
            return
        rows = sheets.all_expenses()
        start, end = reports.last_7_days_range(tz_name)
        text = reports.build_period_report(rows, "Еженедельный отчет", start, end, tz_name)
        TelegramClient().send_message(admin_chat_id, text)
        json_response(self, 200, {"ok": True})
