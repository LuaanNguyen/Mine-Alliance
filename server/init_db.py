from app import app
from models import db, MiningLocation
from routes import generate_assessment_for_location

# Initialize the app context
with app.app_context():
    # Drop and recreate the database tables
    db.drop_all()
    db.create_all()

    location1 = MiningLocation(
        location="Morenci Mine",
        type_of_mining="Copper",
        tenure=85,
        affect_radius=15.0,
        water_quality=6.5,
        air_quality=5.8,
        soil_quality=6.0,
        biodiversity="Minor impacts observed in surrounding flora.",
        socioeconomic_index="Large employer with over 2,000 workers.",
        description="Morenci Mine has been operational since 1939, producing copper with significant economic impact.",
        job_count_index=2000,
        cycle_status="Operational",
        location_coords="32.91185,-109.48397"
    )

    location2 = MiningLocation(
        location="Bagdad Mine",
        type_of_mining="Copper",
        tenure=60,
        affect_radius=12.0,
        water_quality=5.4,
        air_quality=5.2,
        soil_quality=6.1,
        biodiversity="Low impact on local wildlife due to managed operations.",
        socioeconomic_index="Employs around 700 workers.",
        description="Bagdad Mine is a significant copper mine located in Yavapai County, contributing to local and state economies.",
        job_count_index=700,
        cycle_status="Operational",
        location_coords="34.23227,-113.18574"
    )

    location3 = MiningLocation(
        location="Safford Mine",
        type_of_mining="Copper",
        tenure=15,
        affect_radius=10.0,
        water_quality=5.5,
        air_quality=5.6,
        soil_quality=5.7,
        biodiversity="Moderate impact on local ecosystems.",
        socioeconomic_index="Contributes significantly to the local economy with around 400 jobs.",
        description="Safford Mine has been operational since 2007, with a focus on environmentally responsible mining practices.",
        job_count_index=400,
        cycle_status="Operational",
        location_coords="32.75098,-109.45313"
    )

    location4 = MiningLocation(
        location="Sierrita Mine",
        type_of_mining="Copper",
        tenure=30,
        affect_radius=14.0,
        water_quality=5.0,
        air_quality=5.3,
        soil_quality=5.9,
        biodiversity="Moderate impact, ongoing rehabilitation measures in place.",
        socioeconomic_index="Provides approximately 1,000 jobs in the region.",
        description="Sierrita Mine is known for its large-scale copper production and its efforts in local community engagement.",
        job_count_index=1000,
        cycle_status="Operational",
        location_coords="31.61109,-110.67549"
    )

    location5 = MiningLocation(
        location="Miami Mine",
        type_of_mining="Copper",
        tenure=20,
        affect_radius=9.0,
        water_quality=5.8,
        air_quality=5.5,
        soil_quality=5.2,
        biodiversity="Slight impact, with ongoing studies on local fauna.",
        socioeconomic_index="Supports over 600 jobs in the area.",
        description="Miami Mine has been an integral part of Arizona's copper mining industry with a long history and strong community ties.",
        job_count_index=600,
        cycle_status="Operational",
        location_coords="33.40215,-110.93844"
    )

    location6 = MiningLocation(
        location="Ray Mine",
        type_of_mining="Copper",
        tenure=50,
        affect_radius=11.5,
        water_quality=5.2,
        air_quality=5.4,
        soil_quality=5.6,
        biodiversity="Moderate impact on desert ecosystem, mitigation efforts ongoing.",
        socioeconomic_index="Major employer with approximately 800 workers.",
        description="Ray Mine is one of Arizona's largest open-pit copper mines, utilizing advanced mining technologies.",
        job_count_index=800,
        cycle_status="Operational",
        location_coords="33.15478,-110.97277"
    )

    location7 = MiningLocation(
        location="Mission Mine",
        type_of_mining="Copper",
        tenure=40,
        affect_radius=10.5,
        water_quality=5.6,
        air_quality=5.7,
        soil_quality=5.5,
        biodiversity="Managed impact with ongoing environmental monitoring programs.",
        socioeconomic_index="Employs about 500 people from surrounding communities.",
        description="Mission Mine is a significant copper producer, known for its community engagement initiatives.",
        job_count_index=500,
        cycle_status="Operational",
        location_coords="31.97888,-111.04944"
    )

    location8 = MiningLocation(
        location="Pinto Valley Mine",
        type_of_mining="Copper",
        tenure=35,
        affect_radius=9.5,
        water_quality=5.9,
        air_quality=6.0,
        soil_quality=5.8,
        biodiversity="Low to moderate impact, with active wildlife conservation programs.",
        socioeconomic_index="Provides around 550 jobs in the Globe-Miami area.",
        description="Pinto Valley Mine is a long-standing copper operation with a focus on sustainable mining practices.",
        job_count_index=550,
        cycle_status="Operational",
        location_coords="33.39722,-110.96111"
    )

    location9 = MiningLocation(
        location="Florence Copper Project",
        type_of_mining="Copper",
        tenure=5,
        affect_radius=7.0,
        water_quality=6.2,
        air_quality=6.3,
        soil_quality=6.1,
        biodiversity="Minimal surface disturbance due to in-situ recovery method.",
        socioeconomic_index="Expected to create about 170 direct jobs when fully operational.",
        description="Florence Copper Project uses innovative in-situ copper recovery technology, minimizing environmental impact.",
        job_count_index=170,
        cycle_status="Operational",
        location_coords="33.03083,-111.43028"
    )

    location10 = MiningLocation(
        location="Resolution Copper Project",
        type_of_mining="Copper",
        tenure=0,
        affect_radius=13.0,
        water_quality=6.0,
        air_quality=5.9,
        soil_quality=5.7,
        biodiversity="Potential significant impact, extensive environmental studies ongoing.",
        socioeconomic_index="Projected to create about 1,400 direct jobs when operational.",
        description="Resolution Copper Project is a proposed large-scale copper mine, currently in the permitting and development phase.",
        job_count_index=1400,
        cycle_status="Development",
        location_coords="33.30194,-111.09722"
    )
        
    location11 = MiningLocation(
        location="Silver Bell Mine",
        type_of_mining="Copper",
        tenure=65,
        affect_radius=10.5,
        water_quality=5.7,
        air_quality=5.8,
        soil_quality=5.6,
        biodiversity="Moderate impact on local desert ecosystem, ongoing monitoring.",
        socioeconomic_index="Significant employer in Pima County.",
        description="Silver Bell Mine is an open-pit copper mine using leaching extraction methods.",
        job_count_index=350,
        cycle_status="Operational",
        location_coords="32.38917,-111.49917"
    )

    location12 = MiningLocation(
        location="Carlota Mine",
        type_of_mining="Copper",
        tenure=15,
        affect_radius=8.0,
        water_quality=5.9,
        air_quality=6.0,
        soil_quality=5.8,
        biodiversity="Low to moderate impact, with reclamation efforts in progress.",
        socioeconomic_index="Contributes to local economy near Miami, Arizona.",
        description="Carlota Mine is an open-pit copper mine utilizing heap leaching technology.",
        job_count_index=250,
        cycle_status="Operational",
        location_coords="33.28333,-110.99167"
    )

    location13 = MiningLocation(
        location="Copper Creek Project",
        type_of_mining="Copper",
        tenure=0,
        affect_radius=6.0,
        water_quality=6.2,
        air_quality=6.3,
        soil_quality=6.1,
        biodiversity="Minimal current impact, environmental studies ongoing.",
        socioeconomic_index="Potential future employer in Pinal County.",
        description="Copper Creek Project is a proposed underground copper mine in the exploration phase.",
        job_count_index=0,
        cycle_status="Exploration",
        location_coords="32.71667,-110.65000"
    )

    location14 = MiningLocation(
        location="Mineral Park Mine",
        type_of_mining="Copper",
        tenure=55,
        affect_radius=12.0,
        water_quality=5.5,
        air_quality=5.6,
        soil_quality=5.4,
        biodiversity="Significant historical impact, current status limits new effects.",
        socioeconomic_index="Previously a major employer in Mohave County.",
        description="Mineral Park Mine is a large open-pit copper and molybdenum mine, currently on care and maintenance.",
        job_count_index=50,
        cycle_status="Care and Maintenance",
        location_coords="35.36667,-114.10000"
    )

    location15 = MiningLocation(
        location="Johnson Camp Mine",
        type_of_mining="Copper",
        tenure=40,
        affect_radius=9.0,
        water_quality=5.8,
        air_quality=5.9,
        soil_quality=5.7,
        biodiversity="Moderate historical impact, potential for renewed effects if restarted.",
        socioeconomic_index="Potential for job creation if operations resume.",
        description="Johnson Camp Mine is a past-producing open-pit copper mine, potentially restarting operations.",
        job_count_index=0,
        cycle_status="Care and Maintenance",
        location_coords="32.08333,-110.08333"
    )

    location16 = MiningLocation(
        location="Gunnison Copper Project",
        type_of_mining="Copper",
        tenure=4,
        affect_radius=7.5,
        water_quality=6.1,
        air_quality=6.2,
        soil_quality=6.0,
        biodiversity="Low impact due to in-situ recovery method.",
        socioeconomic_index="Growing employer in Cochise County.",
        description="Gunnison Copper Project is an in-situ copper recovery project that began production in 2020.",
        job_count_index=100,
        cycle_status="Operational",
        location_coords="32.25000,-109.83333"
    )

    # Add mining locations to the session
    db.session.add(location1)
    db.session.add(location2)
    db.session.add(location3)
    db.session.add(location4)
    db.session.add(location5)
    db.session.add(location6)
    db.session.add(location7)
    db.session.add(location8)
    db.session.add(location9)
    db.session.add(location11)
    db.session.add(location12)
    db.session.add(location13)
    db.session.add(location14)
    db.session.add(location15)
    db.session.add(location16)

    # Commit changes to the database
    db.session.commit()

    # Generate assessments for the mining locations
    generate_assessment_for_location(location1.id)
    generate_assessment_for_location(location2.id)
    generate_assessment_for_location(location3.id)

    print("Database initialized with mining locations and assessments generated!")
