import pandas as pd
from pathlib import Path


class Processor:

    def __init__(self):
        self.data_dir = Path("data")

    def process(self):

        columns = [
            "DATE",
            "SYMBOL",
            "VALUE OF SECURITY (ACQUIRED/DISPLOSED)",
            "BUYING QTY OF PROMOTERS/PROMOTER GROUP",
            "BUYING AVG PRICE OF PROMOTERS/PROMOTER GROUP",
            "SELLING QTY PRICE OF PROMOTERS/PROMOTER GROUP (MARKET SELL DATA)",
            "SELLING AVG PRICE OF PROMOTERS/PROMOTER GROUP (MARKET SELL DATA)",
            "SHAREHOLDING PATTERN OF PROMOTERS/PROMOTER GROUP",
            "SAST REGULATIONS (SOLD QTY)",
            "PLEDGED DATA OF PROMOTER/PROMOTER GROUP",
            "CLOSE_PRICE",
            "DIFFERENCE %",
            "SIGNAL",
            "REASON"
        ]

        return pd.DataFrame(columns=columns)