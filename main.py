import json
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Load credentials from Railway secret
creds_json = os.environ["GOOGLE_APPLICATION_CREDENTIALS_JSON"]
creds_dict = json.loads(creds_json)
creds = Credentials.from_service_account_info(creds_dict)

# Connect to Google Sheets
service = build("sheets", "v4", credentials=creds)
sheet = service.spreadsheets()

SPREADSHEET_ID = "19I5ZUlp0GpIeRKYuWwGSddzs6H383GB7a62z7Z9k4n4"
RANGE = "Sheet1!A1"

# Test zapis
sheet.values().append(
    spreadsheetId=SPREADSHEET_ID,
    range=RANGE,
    valueInputOption="RAW",
    body={"values": [["Agent beží!"]]}
).execute()
