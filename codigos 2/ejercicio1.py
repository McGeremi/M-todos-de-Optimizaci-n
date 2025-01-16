def precio_vivienda(A):
		m = 1200
		b = 50000
		return m * A + b
for A in range(50, 201, 50):
        print(precio_vivienda(A))