"""
AI PROMOTER SCREENER
Configuration File
"""

from pathlib import Path

# =====================================================
# GOOGLE SHEET
# =====================================================

SHEET_ID = "1B2UwR0Tmp6J72EmOJTN6o05lsFXeI9SZhNZ8XNiXYnM"
WORKSHEET_NAME = "OUTPUT"

# =====================================================
# GOOGLE SERVICE ACCOUNT
# =====================================================

SERVICE_ACCOUNT_FILE = "service_account.json"

# =====================================================
# TIMEZONE
# =====================================================

TIMEZONE = "Asia/Kolkata"

# =====================================================
# LOOKBACK PERIOD
# =====================================================

LOOKBACK_DAYS = 90

# =====================================================
# SIGNAL FILTERS
# =====================================================

MIN_PROMOTER_BUY_VALUE = 10000000      # ₹1 Crore

MIN_SHAREHOLDING = 50.0

MAX_PLEDGED = 0.0

ALLOW_SAST_SELL = 0

ALLOW_PROMOTER_SELL = 0

BUY_PRICE_UPPER = 0.10      # +10%

BUY_PRICE_LOWER = 0.50      # -50%

# =====================================================
# LOCAL FOLDERS
# =====================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

OUTPUT_DIR = BASE_DIR / "output"

LOG_DIR = BASE_DIR / "logs"

for folder in [DATA_DIR, OUTPUT_DIR, LOG_DIR]:
    folder.mkdir(exist_ok=True)

# =====================================================
# FILE NAMES
# =====================================================

INSIDER_FILE = DATA_DIR / "CF_Insider.csv"

SAST_FILE = DATA_DIR / "CF_SAST_Reg.csv"

PLEDGED_FILE = DATA_DIR / "CF_SAST_Pledged.csv"

SHAREHOLDING_FILE = DATA_DIR / "CF_Shareholding.csv"

LOOKUP_FILE = DATA_DIR / "EQUITY_L.csv"

BHAV_FILE = DATA_DIR / "BHAV.csv"

OUTPUT_FILE = OUTPUT_DIR / "promoter_screener.xlsx"

# =====================================================
# NSE URLS
# (Downloader.py ব্যবহার করবে)
# =====================================================

NSE_HOME = "https://www.nseindia.com"

INSIDER_PAGE = "https://www.nseindia.com/companies-listing/corporate-filings-insider-trading"

SAST_PAGE = "https://www.nseindia.com/companies-listing/corporate-filings-regulation-29"

PLEDGED_PAGE = "https://www.nseindia.com/companies-listing/corporate-filings-pledged-data"

SHAREHOLDING_PAGE = "https://www.nseindia.com/companies-listing/corporate-filings-shareholding-pattern"

EQUITY_PAGE = "https://www.nseindia.com/static/market-data/securities-available-for-trading"

BHAV_PAGE = "https://www.nseindia.com/all-reports"

# =====================================================
# END
# =====================================================