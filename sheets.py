import gspread
from google.oauth2.service_account import Credentials

SHEET_ID = "1B2UwR0Tmp6J72EmOJTN6o05lsFXeI9SZhNZ8XNiXYnM"

SERVICE_FILE = "config/service_account.json"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]


def upload_sheet(df):

    creds = Credentials.from_service_account_file(
        SERVICE_FILE,
        scopes=SCOPES
    )

    gc = gspread.authorize(creds)

    sh = gc.open_by_key(SHEET_ID)

    try:
        ws = sh.worksheet("OUTPUT")
    except:
        ws = sh.add_worksheet(
            title="OUTPUT",
            rows="5000",
            cols="30"
        )

    ws.clear()

    data = [df.columns.tolist()]

    data += df.astype(str).values.tolist()

    ws.update(data)

    print("Google Sheet Updated Successfully")