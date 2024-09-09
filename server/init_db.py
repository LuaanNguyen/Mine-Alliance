from app import app
from models import db, User, MiningLocation

# Initialize the app context
with app.app_context():
    # Drop and recreate the database tables
    db.drop_all()
    db.create_all()

    # Sample Users
    user1 = User(username="Mining Company A", user_type="Mining")
    user2 = User(username="Environmental Regulator 1", user_type="Regulator")
    user3 = User(username="Community Member A", user_type="Community")
    
    # Sample Mining Locations
    location1 = MiningLocation(
        company_id=1,  # Assuming this is the ID for Mining Company A
        location="Southern Gold Mine",
        type_of_mining="Gold",
        tenure=15,
        affect_radius=8.5,
        impact_scale=7.2,
        water_quality=5.6,
        air_quality=6.1,
        soil_quality=5.4,
        biodiversity="Moderate impact on local wildlife.",
        socioeconomic_index="High development with 300+ workers.",
        description="Southern Gold Mine has been in operation for 15 years with moderate environmental impact.",
        job_count_index=150
    )

    location2 = MiningLocation(
        company_id=1,  # Same company
        location="Western Iron Mine",
        type_of_mining="Iron",
        tenure=10,
        affect_radius=10.0,
        impact_scale=6.8,
        water_quality=6.3,
        air_quality=6.5,
        soil_quality=6.0,
        biodiversity="Low impact on wildlife, but soil degradation present.",
        socioeconomic_index="Moderate development with 200+ workers.",
        description="Western Iron Mine has been in operation for 10 years with a focus on iron extraction.",
        job_count_index=200
    )

    # Add users and mining locations to the session
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(location1)
    db.session.add(location2)

    # Commit changes to the database
    db.session.commit()

    print("Database initialized with test data!")
