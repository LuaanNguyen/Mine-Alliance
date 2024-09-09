import openai
from flask import Blueprint, jsonify, request
from models import db, User, MiningLocation
from openai import ChatCompletion
import os

# Blueprint for the assessment routes
assessment_bp = Blueprint('assessment_bp', __name__)

# Initialize OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Endpoint to add a new user (Mining Company / Workers, Regulators, Community Members)
@assessment_bp.route('/users', methods=['GET', 'POST'])
def manage_users():
    if request.method == 'POST':
        data = request.json
        user = User(username=data['username'], user_type=data['user_type'])
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User added"}), 201
    elif request.method == 'GET':
        users = User.query.all()
        return jsonify([{"id": user.id, "username": user.username, "user_type": user.user_type} for user in users])


# Endpoint to add a new mining location
@assessment_bp.route('/mining_locations', methods=['POST'])
def add_mining_location():
    data = request.json
    mining_location = MiningLocation(
        location=data.get('location'),
        type_of_mining=data.get('type_of_mining'),
        tenure=data.get('tenure'),
        affect_radius=data.get('affect_radius'),
        impact_scale=data.get('impact_scale'),
        water_quality=data.get('water_quality'),
        air_quality=data.get('air_quality'),
        soil_quality=data.get('soil_quality'),
        biodiversity=data.get('biodiversity'),
        socioeconomic_index=data.get('socioeconomic_index'),
        description=data.get('description')
    )
    db.session.add(mining_location)
    db.session.commit()
    return jsonify({"message": "Location added"}), 201

# Endpoint to generate an assessment based on mining location data
@assessment_bp.route('/assessment', methods=['POST'])
def generate_assessment():
    location_id = request.json.get('location_id')
    
    # Fetch the mining location details from the database
    mining_location = MiningLocation.query.get(location_id)
    
    if not mining_location:
        return jsonify({"error": "Mining location not found"}), 404

    # Generate prompt dynamically using the mining location data
    gpt_prompt = generate_prompt(mining_location)
    
    # Get the GPT-generated assessment
    assessment = get_gpt_assessment(gpt_prompt)
    
    return jsonify({"assessment": assessment})

def generate_prompt(mining_location):
    """
    Generate a prompt for GPT based on the mining location data.
    """
    return f"""
    Conduct an environmental impact assessment for the mining location "{mining_location.location}" with the following details:
    
    - Type of Mining: {mining_location.type_of_mining}
    - Tenure: {mining_location.tenure} years
    - Affect Radius: {mining_location.affect_radius} km
    - Impact Scale: {mining_location.impact_scale}
    - Water Quality: {mining_location.water_quality}
    - Air Quality: {mining_location.air_quality}
    - Soil Quality: {mining_location.soil_quality}
    - Biodiversity Impact: {mining_location.biodiversity}
    - SocioEconomic Index: {mining_location.socioeconomic_index}
    
    Please provide:
    1. Assessment methods
    2. Predicted impacts
    3. Mitigation strategies
    4. Recommendations for mining companies, community, and regulators.
    """

def get_gpt_assessment(prompt):
    """
    Call the GPT model to generate the assessment based on the generated prompt.
    """
    response = ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an environmental impact assessment expert."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"]

#function to get the mining location details of all the mining locations
@assessment_bp.route('/mining_locations', methods=['GET'])
def get_mining_locations():
    mining_locations = MiningLocation.query.all()
    return jsonify([{
        "id": location.id,
        "location": location.location,
        "type_of_mining": location.type_of_mining,
        "tenure": location.tenure,
        "affect_radius": location.affect_radius,
        "impact_scale": location.impact_scale,
        "water_quality": location.water_quality,
        "air_quality": location.air_quality,
        "soil_quality": location.soil_quality,
        "biodiversity": location.biodiversity,
        "socioeconomic_index": location.socioeconomic_index,
        "description": location.description
    } for location in mining_locations])
    
