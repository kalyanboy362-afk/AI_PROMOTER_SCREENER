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