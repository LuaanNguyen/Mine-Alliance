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


# Endpoint to manage mining locations (both POST and GET requests)
@assessment_bp.route('/mining_locations', methods=['POST', 'GET'])
def manage_mining_locations():
    if request.method == 'POST':
        # Handle the POST request: Add a new mining location
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
    
    elif request.method == 'GET':
        # Handle the GET request: Retrieve all mining locations
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


@assessment_bp.route('/assessment', methods=['POST', 'GET'])
def generate_assessment():
    if request.method == 'POST':
        # Handle the POST request: Generate the assessment for a specific mining location
        location_id = request.json.get('location_id')
        
        # Fetch the mining location details from the database
        mining_location = MiningLocation.query.get(location_id)
        
        if not mining_location:
            return jsonify({"error": "Mining location not found"}), 404

        # Generate prompt dynamically using the mining location data
        gpt_prompt = generate_prompt(mining_location)
        
        # Get the GPT-generated assessment
        assessment = get_gpt_assessment(gpt_prompt)
        
        # Save the assessment in the database
        mining_location.assessment = assessment
        db.session.commit()
        
        # Return the generated assessment in the response
        return jsonify({"assessment": assessment})
    
    elif request.method == 'GET':
        # Handle the GET request: Return all mining location details, including their assessments
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
            "description": location.description,
            "assessment": location.assessment  # Include the assessment in the response
        } for location in mining_locations])


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
    Call the GPT model to generate the assessment based on the generated prompt, using the latest OpenAI API version.
    """
    # Set the API key directly for testing purposes (replace 'your_openai_api_key_here' with the actual key)
    openai.api_key = os.getenv('OPENAI_API_KEY')
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an environmental impact assessment expert."},
            {"role": "user", "content": prompt}
        ]
    )
    
    # The correct structure for accessing the generated response in the latest OpenAI API
    return response['choices'][0]['message']['content']

