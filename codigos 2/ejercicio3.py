def tiempo_procesamiento(D):
		k = 0.05
		c = 2
		return k * D + c
		
for D in range(100, 501, 100):
		print(tiempo_procesamiento(D))