from flask import Flask, jsonify, request
from models import db, User, MiningLocation
from openai import ChatCompletion
import os

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    user = User(username=data['username'], user_type=data['user_type'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User added"}), 201

@app.route('/mining_locations', methods=['POST'])
def add_mining_location():
    data = request.json
    mining_location = MiningLocation(**data)
    db.session.add(mining_location)
    db.session.commit()
    return jsonify({"message": "Location added"}), 201

@app.route('/assessment', methods=['POST'])
def generate_assessment():
    location_data = request.json
    gpt_prompt = generate_prompt(location_data)
    assessment = get_gpt_assessment(gpt_prompt)
    return jsonify({"assessment": assessment})

def generate_prompt(location_data):
    return f"Assess the mining location with the following data: {location_data}"

def get_gpt_assessment(prompt):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a mining impact assessment expert."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]
