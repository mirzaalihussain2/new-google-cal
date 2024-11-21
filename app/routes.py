from flask import redirect, url_for, session, request
from google_auth_oauthlib.flow import Flow
from app import app

@app.route('/')
def home():
    return 'Hello, Flask!'