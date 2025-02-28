from flask import Blueprint, request, jsonify
from models import ControlPesoAltura, session, User
from datetime import datetime
from sqlalchemy import select
from werkzeug.security import generate_password_hash, check_password_hash


bp = Blueprint('api', __name__)

@bp.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    # Check if user already exists
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user:
        return jsonify({"message": "User already exists"}), 400

    hashed_password = generate_password_hash(password, method='scrypt')
    new_user = User(username=username, password=hashed_password)
    session.add(new_user)
    session.commit()

    return jsonify({"message": "User registered successfully"}), 201

@bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = session.query(User).filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        return jsonify({"message": "Inicio de sesión exitoso"}), 200
    else:
        return jsonify({"message": "Nombre de usuario o contraseña no válidos"}), 401

@bp.route('/summary', methods=['GET'])
def get_summary():
    """
    retorna todos los datos de la tabla ControlPesoAltura
    """
    records = session.scalars(select(ControlPesoAltura)).all()
    summary_data = [
        {
            "fecha": record.fecha.strftime('%Y-%m-%d'),
            "peso_kg": record.peso_kg,
            "altura_m": record.altura_m,
            "imc": record.imc
        }
        for record in records
    ]
    return jsonify(summary_data), 200

@bp.route('/insert', methods=['POST'])
def insert_data():
    fecha = request.json.get('fecha')
    peso_kg = request.json.get('peso_kg')
    altura_m = request.json.get('altura_m')
    imc = peso_kg / (altura_m ** 2)
    respuesta = ""
    if imc < 18.5:
        respuesta = "Bajo peso: Aumenta tu ingesta calórica con alimentos nutritivos."
    elif 18.5 <= imc < 24.9:
        respuesta = "Peso normal: Mantén una alimentación equilibrada y actividad física regular."
    elif 25 <= imc < 29.9:
        respuesta = "Sobrepeso: Reduce el consumo de calorías y aumenta la actividad física."
    else:
        respuesta = "Obesidad: Consulta con un especialista para un plan de alimentación y ejercicio."

    new_record = ControlPesoAltura(
        fecha=datetime.strptime(fecha, '%Y-%m-%d'),
        peso_kg=float(peso_kg),
        altura_m=float(altura_m),
        imc=float(imc)
    )
    session.add(new_record)
    session.commit()
    return jsonify({"message": respuesta    }), 201

