import math

# Función Gamma, Trapecio Abierto Derecha
def trapecio_abierto_der(x, a, b):
	if x < a:
		return 0
	elif a <= x and x <= b:
		return (x-a)/(b-a)
	elif x > b:
		return 1
	else:
		return -1

# Función L, Trapecio Abierto Izquierda
def trapecio_abierto_izq(x, a, b):
	if x < a:
		return 1
	elif a <= x and x <= b:
		return (b-x)/(b-a)
	elif x > b:
		return 0
	else:
		return -1

# Función Lambda, Triangular
def triangular(x, a, b, c):
	if a > x or x > c:
		return 0
	elif a <= x and x <= b:
		return (x-a)/(b-a)
	elif b <= x and x <= c:
		return (c-x)/(c-b)
	else:
		return -1

# Función Pi, Trapecio
def trapecio_pi(x, a, b, c, d):
	if a > x or x > d:
		return 0
	elif a <= x and x < b:
		return (x-a)/(b-a)
	elif b <= x and x <= c:
		return 1
	elif c < x and x <= d:
		return (d-x)/(d-c)
	else:
		return -1

# Función S
def curva_s(x, a, b):
	if x < a:
		return 0
	elif a <= x and x <= b:
		return 0.5*(1+math.cos(((x-b)/(b-a))*math.pi))
	elif x > b:
		return 1
	else:
		return -1

# Función Z
def curva_z(x, a, b):
	if x < a:
		return 1
	elif a <= x and x <= b:
		return 0.5*(1+math.cos(((x-a)/(b-a))*math.pi))
	elif x > b:
		return 0
	else:
		return -1

# Función Soft Lambda, Triangular Suave
def triangular_suave(x, a, b, c):
	if a > x or x > c:
		return 0
	elif a <= x and x <= b:
		return 0.5*(1+math.cos(((x-b)/(b-a))*math.pi))
	elif b <= x and x <= c:
		return 0.5*(1+math.cos(((x-b)/(c-b))*math.pi))
	else:
		return -1

# Función Soft Pi, Trapecio Suave
def trapecio_suave(x, a, b, c, d):
	if a > x or x > d:
		return 0
	elif a <= x and x <= b:
		return 0.5*(1+math.cos(((x-b)/(b-a))*math.pi))
	elif b <= x and x <= c:
		return 1
	elif c <= x and x <= d:
		return 0.5*(1+math.cos(((x-c)/(d-c))*math.pi))
	else:
		return -1

def min(a, b):
	if a < b: 
		return a
	else:
		return b

def max(a, b):
	if a > b:
		return a
	else:
		return b

# Operadores Fuzzy
def compAnd(ma_u, mb_u):
	return min(ma_u, mb_u)

def compOr(ma_u, mb_u):
	return max(ma_u, mb_u)

def niega(ma_u):
	return 1.0-ma_u

# Implicacion Fuzzy

def implicaZadeh(ma_x, mb_y):
	return max(min(ma_x, mb_y), niega(ma_x))

def implicaMamdani(ma_x, mb_y):
	return min(ma_x, mb_y)

def implicaGodel(ma_x, mb_y):
	if ma_x <= mb_y:
		return 1
	else:
		return mb_y