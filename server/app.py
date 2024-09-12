from flask import Flask, jsonify
from flask_cors import CORS
from models import db
from config import Config
from routes import assessment_bp, chatbot_bp
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

migrate = Migrate(app, db)

db.init_app(app)
CORS(app)

# Register the blueprint for routes
app.register_blueprint(assessment_bp)
app.register_blueprint(chatbot_bp)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Mining Assessment API"})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(host='0.0.0.0', debug=True)
