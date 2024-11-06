import os
from flask import Blueprint, redirect, url_for, session, jsonify
from . import oauth, db  # Ensure this is correct
from .models import User  # Assuming models is in the same package
from config import Config
import secrets  # Use this to generate a nonce

auth_bp = Blueprint('auth', __name__)

google = oauth.register(
    name='google',
    client_id=Config.GOOGLE_CLIENT_ID,
    client_secret=Config.GOOGLE_CLIENT_SECRET,
    server_metadata_url=Config.GOOGLE_DISCOVERY_URL,
    client_kwargs={'scope': 'openid email profile'},
)

@auth_bp.route('/login')
def login():
    # Generate a nonce and store it in the session
    nonce = secrets.token_urlsafe(16)
    session['nonce'] = nonce
    
    redirect_uri = url_for('auth.callback', _external=True)
    return google.authorize_redirect(redirect_uri, nonce=nonce)  # Pass nonce here

@auth_bp.route('/callback')
def callback():
    token = google.authorize_access_token()
    
    # Retrieve the nonce from the session
    nonce = session.pop('nonce', None)
    
    # Pass the nonce when parsing the ID token
    user_info = google.parse_id_token(token, nonce=nonce)
    
    if user_info:
        user = User.query.filter_by(email=user_info['email']).first()
        
        if not user:
            user = User(
                google_id=user_info['sub'],  # Include the google_id here
                email=user_info['email'],
                name=user_info['name'],
                profile_picture=user_info['picture']  # Corrected here
            )
            db.session.add(user)
            db.session.commit()
        
        session['user'] = {'email': user.email, 'name': user.name, 'picture': user.profile_picture}
        return redirect("http://localhost:3000/dashboard")
    
    return "Authorization failed", 401

@auth_bp.route('/user', methods=['GET'])
def get_user():
    user = session.get('user')
    if user:
        return jsonify(user)
    return jsonify({"error": "Unauthorized"}), 401
