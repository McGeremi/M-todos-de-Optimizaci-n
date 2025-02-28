import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_table import ControlPesoAltura
from datetime import datetime

def insert_data(session, data):
    for row in data:
        fecha, peso_kg, altura_m, imc = row
        record = ControlPesoAltura(
            fecha=datetime.strptime(fecha, '%Y-%m-%d'),
            peso_kg=float(peso_kg),
            altura_m=float(altura_m),
            imc=float(imc)
        )
        session.add(record)
    session.commit()

def read_csv(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        data = [row for row in reader]
    return data

if __name__ == "__main__":
    engine = create_engine('sqlite:///control_peso_altura.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    data = read_csv('control_peso_altura.csv')
    insert_data(session, data)