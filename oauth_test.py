import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('DHT22 Logs-fbbd817da07a.json', scope)

gc = gspread.authorize(credentials)
wks = gc.open("DHT Humidity Logs").sheet1

wks.append_row(("DOPEEEE"))
