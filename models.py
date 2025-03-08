from datetime import datetime
from app import db

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model_number = db.Column(db.String(20), nullable=False)
    serial_number = db.Column(db.String(50), unique=True, nullable=False)
    location = db.Column(db.String(200))
    max_amperage = db.Column(db.Float)
    evse_count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    consumption_records = db.relationship('ConsumptionRecord', backref='device', lazy=True)

class ConsumptionRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    kwh_consumption = db.Column(db.Float, nullable=False)
    rate = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'), nullable=False)
    invoice_number = db.Column(db.String(50), unique=True, nullable=False)
    billing_period_start = db.Column(db.DateTime, nullable=False)
    billing_period_end = db.Column(db.DateTime, nullable=False)
    total_kwh = db.Column(db.Float, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pending')
    pdf_path = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
