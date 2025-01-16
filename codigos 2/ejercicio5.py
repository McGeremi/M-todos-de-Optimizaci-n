def medicion_calibrada(R):
		a = 1.2
		b = 5
		return a * R + b
		
for R in range(10, 51, 10):
		print(medicion_calibrada(R))