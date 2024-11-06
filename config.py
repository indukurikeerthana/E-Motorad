import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "a3f5b3c08a9f7e2e4d9fbd02e9206a23")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:root@localhost:5432/emoto")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Set GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET using environment variables
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "${{ secrets.GOOGLE_CLIENT_ID }}")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", " ${{ secrets.GOOGLE_CLIENT_SECRET }}")
    
    GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"
