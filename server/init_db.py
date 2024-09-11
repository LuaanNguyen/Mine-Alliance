from app import app
from models import db, MiningLocation
from routes import generate_assessment_for_location

# Initialize the app context
with app.app_context():
    # Drop and recreate the database tables
    db.drop_all()
    db.create_all()

    # Sample Mining Locations (without impact_scale)
    location1 = MiningLocation(
        location="Southern Gold Mine",
        type_of_mining="Gold",
        tenure=15,
        affect_radius=8.5,
        water_quality=5.6,
        air_quality=6.1,
        soil_quality=5.4,
        biodiversity="Moderate impact on local wildlife.",
        socioeconomic_index="High development with 300+ workers.",
        description="Southern Gold Mine has been in operation for 15 years with moderate environmental impact.",
        job_count_index=150,
        cycle_status="Operational",
        location_coords="35.6895,139.6917"  # Coordinates in latitude, longitude format
    )

    location2 = MiningLocation(
        location="Western Iron Mine",
        type_of_mining="Iron",
        tenure=10,
        affect_radius=10.0,
        water_quality=6.3,
        air_quality=6.5,
        soil_quality=6.0,
        biodiversity="Low impact on wildlife, but soil degradation present.",
        socioeconomic_index="Moderate development with 200+ workers.",
        description="Western Iron Mine has been in operation for 10 years with a focus on iron extraction.",
        job_count_index=200,
        cycle_status="Operational",
        location_coords="40.7128,-74.0060"  # Coordinates in latitude, longitude format
    )

    location3 = MiningLocation(
        location="Northern Coal Mine",
        type_of_mining="Coal",
        tenure=20,
        affect_radius=12.5,
        water_quality=4.9,
        air_quality=5.5,
        soil_quality=5.0,
        biodiversity="Significant impact on wildlife due to deforestation.",
        socioeconomic_index="High development with 500+ workers.",
        description="Northern Coal Mine has been in operation for 20 years with significant environmental impact.",
        job_count_index=500,
        cycle_status="Operational",
        location_coords="51.5074,-0.1278"  # Coordinates in latitude, longitude format
    )

    # Add mining locations to the session
    db.session.add(location1)
    db.session.add(location2)
    db.session.add(location3)

    # Commit changes to the database
    db.session.commit()

    # Generate assessments for the mining locations
    generate_assessment_for_location(location1.id)
    generate_assessment_for_location(location2.id)
    generate_assessment_for_location(location3.id)

    print("Database initialized with mining locations and assessments generated!")
