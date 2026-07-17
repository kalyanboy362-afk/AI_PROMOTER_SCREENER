import json
import base64

import gspread
from google.oauth2.service_account import Credentials

from config import SHEET_ID

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]


def get_client():
    """
    Google Service Account Login
    """

    with open("service_account.json", "r", encoding="utf-8") as f:
        info = json.load(f)

    credentials = Credentials.from_service_account_info(
        info,
        scopes=SCOPES
    )

    return gspread.authorize(credentials)


def get_sheet(sheet_name="OUTPUT"):
    """
    Return Worksheet
    """

    client = get_client()

    spreadsheet = client.open_by_key(SHEET_ID)

    try:
        worksheet = spreadsheet.worksheet(sheet_name)
    except:
        worksheet = spreadsheet.add_worksheet(
            title=sheet_name,
            rows=5000,
            cols=50
        )

    return worksheet


def clear_sheet(sheet_name="OUTPUT"):

    ws = get_sheet(sheet_name)

    ws.clear()


def write_dataframe(df, sheet_name="OUTPUT"):

    ws = get_sheet(sheet_name)

    ws.clear()

    values = [df.columns.tolist()]

    values.extend(df.fillna("").values.tolist())

    ws.update(values)