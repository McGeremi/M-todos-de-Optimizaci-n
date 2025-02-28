import csv
import random
from datetime import datetime, timedelta

def generate_data():
    start_date = datetime(2011, 1, 1)  # Assuming the boy is 14 years old in 2011
    data = []
    for i in range(4 * 12):  # 4 years, monthly data
        date = start_date + timedelta(days=30 * i)
        peso_kg = round(40 + i * 0.5 + random.uniform(-1, 1), 2)  # Simulated weight progression
        altura_m = round(1.5 + i * 0.01 / 12 + random.uniform(-0.01, 0.01), 2)  # Simulated height progression
        imc = round(peso_kg / (altura_m ** 2), 2)
        data.append([date.strftime('%Y-%m-%d'), peso_kg, altura_m, imc])
    return data

def write_csv(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['fecha', 'peso_kg', 'altura_m', 'imc'])
        writer.writerows(data)

if __name__ == "__main__":
    data = generate_data()
    write_csv('control_peso_altura.csv', data)