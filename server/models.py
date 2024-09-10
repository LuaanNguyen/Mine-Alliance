from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    user_type = db.Column(db.String(50), nullable=False)  # Mining, Regulator, Community
    company_locations = relationship('MiningLocation', backref='company', lazy=True, foreign_keys='MiningLocation.company_id')  # Specify the foreign key for mining company
    job_count = db.Column(db.Integer, default=0)  # This will aggregate job counts for the mining company
    nearest_location_id = db.Column(db.Integer, db.ForeignKey('mining_location.id'))  # For community members
    nearest_location = relationship('MiningLocation', foreign_keys=[nearest_location_id])  # Community member's nearest mining location
    permits = relationship('Permit', backref='regulator', lazy=True)  # For regulators

class MiningLocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # ForeignKey to associate mining location with a company
    location = db.Column(db.String(200), nullable=False)
    type_of_mining = db.Column(db.String(100), nullable=False)
    tenure = db.Column(db.Integer)
    affect_radius = db.Column(db.Float)
    impact_scale = db.Column(db.Float)
    water_quality = db.Column(db.Float)
    air_quality = db.Column(db.Float)
    soil_quality = db.Column(db.Float)
    biodiversity = db.Column(db.Text)
    socioeconomic_index = db.Column(db.Text)
    job_count_index = db.Column(db.Integer)  # Job count specific to this mining location
    description = db.Column(db.Text)
    cycle_status = db.Column(db.String(50))
    permits = relationship('Permit', backref='location', lazy=True)  # List of permits for this location
    assessment = db.Column(db.Text)  # Assessment generated for this location

class Permit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('mining_location.id'))  # ForeignKey to associate permit with a mining location
    regulator_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # ForeignKey to associate permit with a regulator
    permit_details = db.Column(db.Text, nullable=False)
    issue_date = db.Column(db.DateTime)
    expiry_date = db.Column(db.DateTime)
