from datetime import datetime
from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255))
    profile_picture = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class BikeStat(db.Model):
    __tablename__ = 'bike_stats'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
    bike_id = db.Column(db.String(50), nullable=False)
    distance_km = db.Column(db.Float)
    battery_level = db.Column(db.Float)
    speed = db.Column(db.Float)
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow)

class MaintenanceLog(db.Model):
    __tablename__ = 'maintenance_logs'
    id = db.Column(db.Integer, primary_key=True)
    bike_id = db.Column(db.String(50), nullable=False)
    maintenance_date = db.Column(db.DateTime)
    description = db.Column(db.Text)
    cost = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="SET NULL"))

class Trip(db.Model):
    __tablename__ = 'trips'
    id = db.Column(db.Integer, primary_key=True)
    bike_id = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    distance_km = db.Column(db.Float)
    duration_minutes = db.Column(db.Integer)

class UserSettings(db.Model):
    __tablename__ = 'user_settings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
    unit_of_measurement = db.Column(db.String(10), default="metric")
    notification_enabled = db.Column(db.Boolean, default=True)
