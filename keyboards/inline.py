from states.constants import CATEGORIES, CRYPTO_CURRENCIES, STATUSES


def button(text, callback_data):
    return {"text": text, "callback_data": callback_data}


def inline_keyboard(rows):
    return {"inline_keyboard": rows}


def main_menu_keyboard():
    return inline_keyboard(
        [
            [button("➕ Добавить расход", "cmd:add"), button("📊 Отчет", "cmd:report")],
            [button("📜 История", "cmd:history"), button("ℹ Помощь", "cmd:help")],
        ]
    )


def payment_keyboard():
    return inline_keyboard(
        [
            [button("💵 Наличные", "payment:cash")],
            [button("🏦 Безналичные", "payment:card")],
            [button("₿ Крипта", "payment:crypto")],
            [button("❌ Отмена", "flow:cancel")],
        ]
    )


def crypto_keyboard():
    return inline_keyboard(
        [
            [button("₿ BTC", "crypto:BTC"), button("⟠ ETH", "crypto:ETH"), button("💵 USDT", "crypto:USDT")],
            [button("❌ Отмена", "flow:cancel")],
        ]
    )


def category_keyboard():
    emoji = {
        "Подписки": "💳",
        "Зарплата": "💰",
        "Офис": "🏢",
        "Обучение": "🎓",
        "Маркетинг": "📢",
        "Прочее": "📁",
    }
    rows = [[button(f"{emoji.get(category, '')} {category}".strip(), f"category:{category}")] for category in CATEGORIES]
    rows.append([button("❌ Отмена", "flow:cancel")])
    return inline_keyboard(rows)


def status_keyboard():
    emoji = {
        "Оплачен": "✅",
        "На рассмотрении": "⏳",
        "Отказ": "❌",
    }
    rows = [[button(f"{emoji.get(status, '')} {status}".strip(), f"status:{status}")] for status in STATUSES]
    rows.append([button("❌ Отмена", "flow:cancel")])
    return inline_keyboard(rows)


def confirm_keyboard():
    return inline_keyboard(
        [
            [button("✅ Сохранить", "confirm:save")],
            [button("❌ Отмена", "confirm:cancel")],
        ]
    )


def saved_keyboard():
    return inline_keyboard(
        [
            [button("↩️ Отменить запись", "undo:saved")],
            [button("➕ Добавить еще", "cmd:add")],
        ]
    )


def report_keyboard():
    return inline_keyboard(
        [
            [button("Сегодня", "report:today"), button("7 дней", "report:week")],
            [button("Месяц", "report:month")],
        ]
    )


def delete_confirm_keyboard():
    return inline_keyboard(
        [
            [button("✅ Удалить", "delete:confirm")],
            [button("❌ Отмена", "delete:cancel")],
        ]
    )
