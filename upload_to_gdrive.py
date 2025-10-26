from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import datetime

# --- 1. Khai báo thông tin xác thực ---
SERVICE_ACCOUNT_FILE = 'service_account.json'  # file JSON tải từ Google Cloud
SCOPES = ['https://www.googleapis.com/auth/drive.file']

# --- 2. Xác thực với Google Drive ---
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
service = build('drive', 'v3', credentials=credentials)

# --- 3. Tạo file hello.txt ---
filename = 'hello.txt'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(f"Hello World - {datetime.datetime.now()}\n")

# --- 4. Upload lên Google Drive ---
file_metadata = {'name': filename}
media = MediaFileUpload(filename, mimetype='text/plain')
file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

print(f"✅ File '{filename}' uploaded to Google Drive with ID: {file.get('id')}")
