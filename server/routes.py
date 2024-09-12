import openai
from flask import Blueprint, jsonify, request
from models import db, MiningLocation
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Blueprint for the assessment and chatbot routes
assessment_bp = Blueprint('assessment_bp', __name__)
chatbot_bp = Blueprint('chatbot_bp', __name__)

# Initialize OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Helper function to validate mining location input
def validate_location_data(data):
    required_fields = ['location', 'type_of_mining', 'tenure', 'affect_radius', 
                       'water_quality', 'air_quality', 'soil_quality', 
                       'biodiversity', 'socioeconomic_index', 'description']
    
    missing_fields = [field for field in required_fields if not data.get(field)]
    
    if missing_fields:
        return {"error": f"Missing fields: {', '.join(missing_fields)}"}, 400
    return None

def get_mining_location(location_id=None, location_name=None, location_coords=None):
    if location_id:
        return db.session.get(MiningLocation, location_id)  # Use session.get() now
    elif location_name:
        return MiningLocation.query.filter_by(location=location_name).first()
    elif location_coords:
        return MiningLocation.query.filter_by(location_coords=location_coords).first()
    return None

# Helper function to generate GPT prompt based on mining location data
def generate_prompt(mining_location):
    return f"""
    Conduct an environmental impact assessment for the mining location "{mining_location.location}" with the following details:
    
    - Type of Mining: {mining_location.type_of_mining}
    - Tenure: {mining_location.tenure} years
    - Affect Radius: {mining_location.affect_radius} km
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
    5. Estimate an environmental impact scale between 1 and 10.
    """

# Helper function to call GPT model and generate the assessment and impact scale
def get_gpt_assessment(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an environmental impact assessment expert."},
            {"role": "user", "content": prompt}
        ]
    )
    assessment_text = response['choices'][0]['message']['content']
    
    # Extract impact scale from the assessment
    impact_scale = extract_impact_scale(assessment_text)
    
    return assessment_text, impact_scale

# Helper function to extract impact scale from GPT assessment response
def extract_impact_scale(assessment_text):
    lines = assessment_text.split('\n')
    for line in lines:
        if "Impact Scale" in line and ":" in line:
            try:
                return float(line.split(":")[1].strip())
            except (ValueError, IndexError):
                return None  # Handle error gracefully
    return None  # Default to None if no scale is found



# Endpoint to manage mining locations (POST to add, GET to retrieve)
@assessment_bp.route('/mining_locations', methods=['POST', 'GET'])
def manage_mining_locations():
    if request.method == 'POST':
        # Handle the POST request: Add a new mining location
        data = request.json
        location_coords = data.get('location_coords')

        # Validate input data
        validation_error = validate_location_data(data)
        if validation_error:
            return jsonify(validation_error), 400

        if not location_coords:
            return jsonify({"error": "location_coords is required"}), 400

        try:
            mining_location = MiningLocation(
                location=data.get('location'),
                type_of_mining=data.get('type_of_mining'),
                tenure=data.get('tenure'),
                affect_radius=data.get('affect_radius'),
                water_quality=data.get('water_quality'),
                air_quality=data.get('air_quality'),
                soil_quality=data.get('soil_quality'),
                biodiversity=data.get('biodiversity'),
                socioeconomic_index=data.get('socioeconomic_index'),
                description=data.get('description'),
                location_coords=location_coords
            )

            # Generate the GPT prompt and assessment
            gpt_prompt = generate_prompt(mining_location)
            assessment, impact_scale = get_gpt_assessment(gpt_prompt)

            # Update mining location with assessment and impact scale
            mining_location.assessment = assessment
            mining_location.impact_scale = impact_scale

            # Save to the database
            db.session.add(mining_location)
            db.session.commit()

            return jsonify({
                "message": "Location added successfully",
                "assessment": assessment,
                "impact_scale": impact_scale
            }), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

    elif request.method == 'GET':
        # Fetch query parameters
        location_id = request.args.get('id')
        location_name = request.args.get('location')
        location_coords = request.args.get('coords')

        if location_id or location_name or location_coords:
            mining_location = get_mining_location(location_id, location_name, location_coords)

            if not mining_location:
                return jsonify({"error": "Mining location not found."}), 404

            # Check if the assessment and impact scale exist, if not, generate them
            if not mining_location.assessment or not mining_location.impact_scale:
                # Generate GPT prompt based on mining location
                gpt_prompt = generate_prompt(mining_location)
                # Get GPT-generated assessment and impact scale
                assessment, impact_scale = get_gpt_assessment(gpt_prompt)

                # Update mining location with assessment and impact scale
                mining_location.assessment = assessment
                mining_location.impact_scale = impact_scale
                db.session.commit()

            return jsonify({
                "id": mining_location.id,
                "location": mining_location.location,
                "type_of_mining": mining_location.type_of_mining,
                "tenure": mining_location.tenure,
                "affect_radius": mining_location.affect_radius,
                "impact_scale": mining_location.impact_scale,
                "water_quality": mining_location.water_quality,
                "air_quality": mining_location.air_quality,
                "soil_quality": mining_location.soil_quality,
                "biodiversity": mining_location.biodiversity,
                "socioeconomic_index": mining_location.socioeconomic_index,
                "description": mining_location.description,
                "assessment": mining_location.assessment,
                "location_coords": mining_location.location_coords
            }), 200
        else:
            # No specific location requested, return all mining locations
            all_mines = MiningLocation.query.all()
            if not all_mines:
                return jsonify({"message": "No mining locations found."}), 404
            
            result = [{
                "id": mine.id,
                "location": mine.location,
                "type_of_mining": mine.type_of_mining,
                "tenure": mine.tenure,
                "affect_radius": mine.affect_radius,
                "impact_scale": mine.impact_scale,
                "water_quality": mine.water_quality,
                "air_quality": mine.air_quality,
                "soil_quality": mine.soil_quality,
                "biodiversity": mine.biodiversity,
                "socioeconomic_index": mine.socioeconomic_index,
                "description": mine.description,
                "location_coords": mine.location_coords,
                "assessment": mine.assessment
            } for mine in all_mines]

            return jsonify(result), 200
        
# Helper function for generating assessment for a specific location
def generate_assessment_for_location(location_id):
    # Fetch the mining location from the database
    mining_location = MiningLocation.query.get(location_id)
    if not mining_location:
        return {"error": "Mining location not found."}, 404

    # Generate GPT prompt based on mining location
    gpt_prompt = generate_prompt(mining_location)
    
    # Get GPT-generated assessment and impact scale
    assessment, impact_scale = get_gpt_assessment(gpt_prompt)

    # Update mining location with assessment and impact scale
    mining_location.assessment = assessment
    mining_location.impact_scale = impact_scale
    db.session.commit()

    return {"assessment": assessment, "impact_scale": impact_scale}, 200

# Update your POST route to call this function
@assessment_bp.route('/assessment', methods=['POST'])
def generate_assessment():
    location_id = request.json.get('location_id')
    if not location_id:
        return jsonify({"error": "No location_id provided."}), 400

    result, status_code = generate_assessment_for_location(location_id)
    return jsonify(result), status_code


# Route for handling mining-related chatbot questions
@chatbot_bp.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    user_question = data.get('question')
    mine_id = data.get('mineId')

    if not user_question:
        return jsonify({"error": "No question provided."}), 400

    # Generate GPT prompt based on user question and mine ID
    gpt_prompt = f"Answer the following question about mining quality for mine {mine_id}: {user_question}"

    # Get the GPT response
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in mining and environmental impact."},
            {"role": "user", "content": gpt_prompt}
        ]
    )

    answer = response['choices'][0]['message']['content']

    # Return the chatbot response
    return jsonify({"response": answer}), 200