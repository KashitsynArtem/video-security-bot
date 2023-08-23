import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    BOT_API_TOKEN = os.getenv('BOT_API_TOKEN')
    ID_ADMIN = os.getenv('ID_ADMIN')
    RTSP = os.getenv('RTSP')


Settings = Settings()

