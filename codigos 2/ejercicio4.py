def costo_almacenamiento(D):
		p = 0.1
		f = 50
		return p * D + f
		
for D in range(10, 101, 10):
		print(costo_almacenamiento(D))