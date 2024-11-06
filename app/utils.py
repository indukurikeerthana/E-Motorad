from .models import BikeStat, MaintenanceLog, Trip, UserSettings

def model_to_dict(instance):
    return {column.name: getattr(instance, column.name) for column in instance.__table__.columns}

BikeStat.to_dict = model_to_dict
MaintenanceLog.to_dict = model_to_dict
Trip.to_dict = model_to_dict
UserSettings.to_dict = model_to_dict
