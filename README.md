# Mining Assessment and Chatbot API

This is a Flask-based web application that integrates OpenAI's GPT-4 model to perform environmental impact assessments for mining locations. It also features a chatbot capable of answering mining-related questions. The project includes endpoints for adding and retrieving mining locations, generating assessments, and interacting with a chatbot.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
  - [Home](#home)
  - [Mining Locations](#mining-locations)
  - [Generate Assessment](#generate-assessment)
  - [Chatbot](#chatbot)
- [Database Schema](#database-schema)

## Overview

The Mining Assessment API allows users to:
1. Add and retrieve mining locations.
2. Generate environmental impact assessments using GPT-4 based on mining data.
3. Interact with a mining-specific chatbot that answers relevant questions.

The assessments provide:
- Assessment methods
- Predicted impacts
- Mitigation strategies
- Recommendations for mining companies, communities, and regulators
- An environmental impact scale (1-10)

## Project Structure

├── app.py # Main Flask application ├── config.py # Configuration file for environment variables and API keys ├── models.py # SQLAlchemy models for the database ├── routes.py # Blueprint routes for assessments and chatbot ├── test.py # Unit tests for the Flask application ├── migrations/ # Database migration files (Flask-Migrate) ├── venv/ # Virtual environment (optional) ├── README.md # This documentation file └── .env # Environment variables (not included in repo)


## Setup

### Prerequisites

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- OpenAI Python client library
- Virtual environment (optional, but recommended)

### Installation

1. **Clone the repository:**
  ```
  git clone https://github.com/yourusername/your-repo.git
  cd your-repo
  ```

2. **Create Virtual environment (Optional)**
  ```
  python3 -m venv venv
  source venv/bin/activate  # For Windows use `venv\Scripts\activate`
  ```

3. **Install dependencies**
  ```
  pip install -r requirements.txt
  ```

4. **Run the application**
  ```
  flask run
  ```

5. **Create Database if needed**
  ```
  flask db init
  flask db migrate
  flask db upgrade
  ```

6. **Environment Variables**

**Create a ```.env``` file in the root directory with the following content.**

```makefile
OPENAI_API_KEY=<your-openai-api-key>
```

# API Endpoints
## Home
### URL: /

**Method: GET**

**Description: Returns a welcome message.**

**Response:**

```json
{
  "message": "Welcome to the Mining Assessment API"
}
```

## Mining Locations
### URL: /mining_locations

**Methods: POST, GET**

**POST (Add a new mining location)**
**Description: Adds a new mining location to the database.**

**Payload (JSON):**

```json
{
  "location": "Southern Gold Mine",
  "type_of_mining": "Gold",
  "tenure": 15,
  "affect_radius": 8.5,
  "water_quality": 5.6,
  "air_quality": 6.1,
  "soil_quality": 5.4,
  "biodiversity": "Moderate impact on local wildlife.",
  "socioeconomic_index": "High development with 300+ workers.",
  "description": "Southern Gold Mine has been in operation for 15 years with moderate environmental impact.",
  "location_coords": "35.6895,139.6917"
}
```

**Response:**

```json
{
  "message": "Location added successfully",
  "assessment": "<GPT-generated assessment>",
  "impact_scale": 7.5
}
```

### GET (Retrieve mining locations)
**You can query mining locations using their id, location, or coords.**
**Query Parameters:**

-id: Mining location ID
-location: Mining location name
-coords: Coordinates of the mining location

**Example Request:**

```
GET /mining_locations?id=1
```
**Response:**

```json
{
  "id": 1,
  "location": "Southern Gold Mine",
  "type_of_mining": "Gold",
  "tenure": 15,
  "affect_radius": 8.5,
  "impact_scale": 7.5,
  "water_quality": 5.6,
  "air_quality": 6.1,
  "soil_quality": 5.4,
  "biodiversity": "Moderate impact on local wildlife.",
  "socioeconomic_index": "High development with 300+ workers.",
  "description": "Southern Gold Mine has been in operation for 15 years with moderate environmental impact.",
  "assessment": "<GPT-generated assessment>",
  "location_coords": "35.6895,139.6917"
}
```


### Generate Assessment
### URL: /assessment

**Method: POST**

**Description: Generate an environmental impact assessment for an existing mining location.**

**Payload (JSON):**

```json
{
  "location_id": 1
}
```

**Response:**

```json
{
  "assessment": "<GPT-generated assessment>",
  "impact_scale": 7.5
}
```
### Chatbot
### URL: /chatbot

**Method: POST**

**Description: Interact with a mining-related chatbot.**

**Payload (JSON):**

```json
{
  "question": "What are the environmental impacts of gold mining?"
}
```
**Response:**

```json
{
  "response": "<GPT-generated response>"
}
```

## Database Schema
The `MiningLocation` model represents mining locations, with the following fields:

`id`: Integer, Primary Key
`location`: String, the name of the mining location
`type_of_mining`: String, the type of mining (e.g., gold, coal, iron)
`tenure`: Integer, how long the mining has been active
`affect_radius`: Float, the radius affected by the mining
`impact_scale`: Float, a GPT-generated impact scale (1-10)
`water_quality`: Float, water quality score
`air_quality`: Float, air quality score
`soil_quality`: Float, soil quality score
`biodiversity`: Text, biodiversity impact description
`socioeconomic_index`: Text, socioeconomic description
`job_count_index`: Integer, number of jobs created by the mining
`description`: Text, description of the mining site
`cycle_status`: String, status of the mining site (e.g., operational, closed)
`assessment`: Text, GPT-generated environmental assessment
`location_coords`: String, coordinates of the location (latitude, longitude)
