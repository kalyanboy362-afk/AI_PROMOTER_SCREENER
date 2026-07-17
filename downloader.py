import requests
from pathlib import Path
from datetime import datetime, timedelta

from config import DATA_DIR

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/138.0 Safari/537.36",
    "Accept": "application/json,text/csv,text/plain,*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.nseindia.com/",
    "Origin": "https://www.nseindia.com"
}


class NSEDownloader:

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update(HEADERS)

        self.today = datetime.today()

        self.from_date = self.today - timedelta(days=90)

        DATA_DIR.mkdir(exist_ok=True)

    def start_session(self):

        """
        Generate NSE Cookies
        """

        url = "https://www.nseindia.com/"

        r = self.session.get(url, timeout=30)

        r.raise_for_status()

        print("NSE Session Started")

    def save_file(self, response, filename):

        path = DATA_DIR / filename

        with open(path, "wb") as f:

            f.write(response.content)

        print(f"Saved : {filename}")

        return path

    def format_date(self, dt):

        return dt.strftime("%d-%m-%Y")
    # ==========================================================
# DATE RANGE
# ==========================================================

    def get_from_date(self):

        return self.from_date.strftime("%d-%m-%Y")


    def get_to_date(self):

        return self.today.strftime("%d-%m-%Y")


# ==========================================================
# DOWNLOAD URL BUILDER
# ==========================================================

    def build_date_params(self):

        return {

            "from_date": self.get_from_date(),

            "to_date": self.get_to_date()

        }


# ==========================================================
# COMMON DOWNLOAD FUNCTION
# ==========================================================

    def download_csv(self, url, params, filename):

        print(f"Downloading {filename}")

        response = self.session.get(

            url,

            params=params,

            timeout=60

        )

        response.raise_for_status()

        return self.save_file(response, filename)