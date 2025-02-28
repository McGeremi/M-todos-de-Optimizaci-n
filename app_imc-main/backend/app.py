from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from routes import bp as api_routes

app = Flask(__name__)
CORS(app)
CORS(api_routes)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///control_peso_altura.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

app.register_blueprint(api_routes)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)