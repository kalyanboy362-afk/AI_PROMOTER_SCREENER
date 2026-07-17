import os
import requests
from datetime import datetime, timedelta

class NSEDownloader:

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update({

            "User-Agent":"Mozilla/5.0",

            "Referer":"https://www.nseindia.com"

        })

        self.base = "https://www.nseindia.com"

        self.data_folder = "data"

        os.makedirs(self.data_folder, exist_ok=True)

    def warmup(self):

        self.session.get(self.base, timeout=30)

    def download_file(self, url, filename):

        self.warmup()

        r = self.session.get(url, timeout=60)

        r.raise_for_status()

        path = os.path.join(self.data_folder, filename)

        with open(path, "wb") as f:

            f.write(r.content)

        print("Downloaded :", filename)

        return path

    def run(self):

        print("Downloader Started...")

        today = datetime.today()

        from_date = today - timedelta(days=90)

        print("FROM :", from_date.strftime("%d-%m-%Y"))

        print("TO   :", today.strftime("%d-%m-%Y"))

        # এখানেই পরের ধাপে সব Downloader কল হবে

        print("Downloader Finished")
            def download_insider(self):

        print("Downloading Insider Trading...")

        url = (
            "https://www.nseindia.com/api/corporates-pit?"
            "index=equities"
        )

        try:

            self.download_file(
                url,
                "CF_Insider.csv"
            )

        except Exception as e:

            print("Insider Download Failed :", e)


    def download_shareholding(self):

        print("Downloading Shareholding...")

        url = (
            "https://www.nseindia.com/api/corporate-share-holdings"
        )

        try:

            self.download_file(
                url,
                "CF_Shareholding.csv"
            )

        except Exception as e:

            print(e)


    def download_sast(self):

        print("Downloading SAST...")

        url = (
            "https://www.nseindia.com/api/corporate-sast"
        )

        try:

            self.download_file(
                url,
                "CF_SAST.csv"
            )

        except Exception as e:

            print(e)


    def download_pledged(self):

        print("Downloading Pledged Data...")

        url = (
            "https://www.nseindia.com/api/corporate-pledged"
        )

        try:

            self.download_file(
                url,
                "CF_Pledged.csv"
            )

        except Exception as e:

            print(e)


    def download_equity(self):

        print("Downloading EQUITY LIST...")

        url = (
            "https://archives.nseindia.com/content/equities/EQUITY_L.csv"
        )

        try:

            self.download_file(
                url,
                "EQUITY_L.csv"
            )

        except Exception as e:

            print(e)