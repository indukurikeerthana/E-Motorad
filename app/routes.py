# app/routes.py
from flask import Blueprint, jsonify
from .models import Trip
from . import db  # import db from app/__init__.py if necessary

# Define the Blueprint
bp = Blueprint('main', __name__)

@bp.route('/api/trips/recent', methods=['GET'])
def get_recent_trips():
    trips = Trip.query.order_by(Trip.start_time.desc()).limit(10).all()
    trip_data = [{
        'bike_id': trip.bike_id,
        'distance_km': trip.distance_km,
        'duration_minutes': trip.duration_minutes,
        'start_time': trip.start_time
    } for trip in trips]
    return jsonify(trip_data), 200
