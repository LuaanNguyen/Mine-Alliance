import unittest
import json
from app import app, db
from models import MiningLocation

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        # Set up the Flask test client
        self.app = app.test_client()
        self.app.testing = True

        # Set up the database (using an in-memory SQLite database)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Drop all the tables after each test
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_mining_location(self):
        # Test the POST /mining_locations endpoint
        new_location = {
            "location": "Test Gold Mine",
            "type_of_mining": "Gold",
            "tenure": 20,
            "affect_radius": 15.5,
            "impact_scale": 7.5,
            "water_quality": 5.5,
            "air_quality": 6.2,
            "soil_quality": 5.8,
            "biodiversity": "Moderate impact on local wildlife.",
            "socioeconomic_index": "Stable economic development around the area.",
            "description": "A gold mining operation that has been running for 20 years with moderate environmental impact."
        }

        response = self.app.post('/mining_locations', data=json.dumps(new_location), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'], "Location added")

    def test_generate_assessment(self):
        # First, add a mining location
        self.test_add_mining_location()

        # Test the POST /assessment endpoint to generate the assessment
        response = self.app.post('/assessment', data=json.dumps({"location_id": 1}), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.data)
        self.assertIn("assessment", response_data)
        self.assertIsInstance(response_data["assessment"], str)

        # Save the response for verification
        with open('post_assessment_response.json', 'w') as f:
            json.dump(response_data, f, indent=4)

    def test_get_assessment(self):
        # First, generate an assessment by running the above function
        self.test_generate_assessment()

        # Test the GET /assessment endpoint
        response = self.app.get('/assessment')
        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.data)
        self.assertGreater(len(response_data), 0)
        self.assertEqual(response_data[0]['location'], "Test Gold Mine")
        self.assertIn("assessment", response_data[0])
        self.assertIsInstance(response_data[0]["assessment"], str)

        # Save the response for verification
        with open('get_assessment_response.json', 'w') as f:
            json.dump(response_data, f, indent=4)

if __name__ == '__main__':
    unittest.main()
