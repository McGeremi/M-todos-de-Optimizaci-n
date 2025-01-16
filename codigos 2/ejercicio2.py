def ganancia_mensual(N):
		c = 15
		b = 1000
		return c * N + b
		
for N in range(100, 601, 100):
		print(ganancia_mensual(N))