def tiempo_respuesta(S):
		m = 0.02
		b = 1
		return m * S + b
		
for S in range(10, 101, 10):
		print(tiempo_respuesta(S))