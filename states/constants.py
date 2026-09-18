STATE_PAYMENT_TYPE = "payment_type"
STATE_CRYPTO_CURRENCY = "crypto_currency"
STATE_CRYPTO_WALLET = "crypto_wallet"
STATE_CURRENCY = "currency"
STATE_AMOUNT = "amount"
STATE_DESCRIPTION = "description"
STATE_CATEGORY = "category"
STATE_STATUS = "status"
STATE_CONFIRM = "confirm"
STATE_DELETE_SELECT = "delete_select"
STATE_DELETE_CONFIRM = "delete_confirm"
STATE_DELETE_PENDING = "delete_pending"
STATE_EDIT_SELECT = "edit_select"
STATE_EDIT_FIELD = "edit_field"
STATE_EDIT_VALUE = "edit_value"
STATE_STATUS_UPDATE = "status_update"
STATE_UNDO_SAVED = "undo_saved"

PAYMENT_CASH = "Наличные"
PAYMENT_CARD = "Безналичные"
PAYMENT_CRYPTO = "Крипта"

CURRENCY_RUB = "RUB"
CURRENCY_USD = "USD"
FIAT_CURRENCIES = (CURRENCY_RUB, CURRENCY_USD)

CRYPTO_CURRENCIES = ("BTC", "ETH", "USDT")

CATEGORIES = (
    "Подписки",
    "Зарплата",
    "Офис",
    "Обучение",
    "Маркетинг",
    "Прочее",
)

STATUSES = (
    "Оплачен",
    "На рассмотрении",
    "Отказ",
)

PAYMENT_GROUPS = (
    "Наличные RUB",
    "Безналичные RUB",
    "Наличные USD",
    "Безналичные USD",
    "BTC",
    "ETH",
    "USDT",
)
