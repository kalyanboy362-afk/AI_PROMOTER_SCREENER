from downloader import NSEDownloader
from processor import Processor
from sheets import upload_sheet

def main():

    downloader = NSEDownloader()

    downloader.run()

    processor = Processor()

    df = processor.process()

    upload_sheet(df)

if __name__ == "__main__":
    main()