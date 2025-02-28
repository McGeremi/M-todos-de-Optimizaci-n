# README for Backend

## Overview
This is the backend of the web application prototype built using Flask. It provides a RESTful API for user authentication, data retrieval, and data insertion related to weight and height control.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd web-app-prototype/backend
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python app.py
   ```

   The application will start on `http://127.0.0.1:5000`.

## API Endpoints

### Authentication
- **POST /login**
  - Request body: `{ "username": "your_username", "password": "your_password" }`
  - Description: Authenticates a user and returns a token.

### Data Retrieval
- **GET /summary**
  - Description: Retrieves summary statistics and graphs for weight and height control data.

### Data Insertion
- **POST /control**
  - Request body: `{ "fecha": "YYYY-MM-DD", "peso_kg": number, "altura_m": number, "imc": number }`
  - Description: Inserts new control data for the current date.

## Database
The application uses SQLite for data storage. The database file is `control_peso_altura.db`.

## License
This project is licensed under the MIT License. See the LICENSE file for details.