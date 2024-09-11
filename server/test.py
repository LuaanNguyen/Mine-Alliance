import unittest
from app import app, db
from models import MiningLocation

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        # Set up test environment
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory DB for testing
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

        # Add sample data
        self.sample_location = MiningLocation(
            location="Sample Gold Mine",
            type_of_mining="Gold",
            tenure=5,
            affect_radius=10.5,
            water_quality=6.0,
            air_quality=7.0,
            soil_quality=6.5,
            biodiversity="Moderate impact on wildlife",
            socioeconomic_index="High development",
            description="A sample gold mine for testing",
            location_coords="40.7128,-74.0060"
        )
        db.session.add(self.sample_location)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_home_page(self):
        # Test if the home route works
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Mining Assessment API', response.data)

    def test_add_mining_location(self):
        # Test POST request to add a new mining location
        response = self.app.post('/mining_locations', json={
            "location": "Test Mine",
            "type_of_mining": "Coal",
            "tenure": 20,
            "affect_radius": 15.5,
            "water_quality": 5.8,
            "air_quality": 6.5,
            "soil_quality": 6.0,
            "biodiversity": "High impact",
            "socioeconomic_index": "Moderate development",
            "description": "A test mine for testing purposes",
            "location_coords": "51.5074,-0.1278"
        })

        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn("Location added successfully", data["message"])
        self.assertIn("assessment", data)
        self.assertIn("impact_scale", data)

    def test_get_mining_location(self):
        # Test GET request for a mining location
        response = self.app.get(f'/mining_locations?id={self.sample_location.id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['location'], "Sample Gold Mine")
        self.assertIn('assessment', data)
        self.assertIn('impact_scale', data)

    def test_generate_assessment(self):
        # Test POST request to generate an assessment for an existing mining location
        response = self.app.post('/assessment', json={"location_id": self.sample_location.id})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('assessment', data)
        self.assertIn('impact_scale', data)

    def test_missing_location_field(self):
        # Test POST request with missing fields
        response = self.app.post('/mining_locations', json={
            "location": "Incomplete Mine",
            "type_of_mining": "Copper",
            # Missing tenure, affect_radius, water_quality, etc.
            "location_coords": "10.0,20.0"
        })
        
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        
        # Adjust for the tuple being returned in the error response
        self.assertIn("Missing fields", data[0]['error'])


    def test_chatbot_question(self):
        # Test POST request to the chatbot endpoint
        response = self.app.post('/chatbot', json={"question": "What are the environmental impacts of gold mining?"})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("response", data)

    def test_chatbot_missing_question(self):
        # Test POST request to the chatbot with no question provided
        response = self.app.post('/chatbot', json={})
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn("No question provided", data["error"])

if __name__ == '__main__':
    unittest.main()
