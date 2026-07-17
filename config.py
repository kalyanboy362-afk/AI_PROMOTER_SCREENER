from pathlib import Path

# ==========================
# GOOGLE SHEET
# ==========================

SHEET_ID = "1B2UwR0Tmp6J72EmOJTN6o05lsFXeI9SZhNZ8XNiXYnM"

SHEET_NAME = "OUTPUT"

# ==========================
# DIRECTORIES
# ==========================

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

OUTPUT_DIR = BASE_DIR / "output"

LOG_DIR = BASE_DIR / "logs"

DATA_DIR.mkdir(exist_ok=True)

OUTPUT_DIR.mkdir(exist_ok=True)

LOG_DIR.mkdir(exist_ok=True)

# ==========================
# DATE RANGE
# ==========================

LOOKBACK_DAYS = 90

# ==========================
# NSE URL
# ==========================

NSE_HOME = "https://www.nseindia.com"

# ==========================
# USER AGENT
# ==========================

HEADERS = {

    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/138 Safari/537.36",

    "Accept":
    "*/*",

    "Referer":
    "https://www.nseindia.com"

}