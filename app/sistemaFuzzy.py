from app.funcionesMembresia import *

conjAsaltoRobo = ["Baja", "Media", "Alta"]
conjHomic = ["Baja", "Media", "Alta"]
conjSecVioAcos = ["Baja", "Media", "Alta"]
conjDrogArmas = ["Baja", "Media", "Alta"]
conjInseguridad = ["Baja", "Media", "Alta", "Critica"]

nivsMemAsaltoRobo = [0.0, 0.0, 0.0]
nivsMemHomic = [0.0, 0.0, 0.0]
nivsMemSecVioAcos = [0.0, 0.0, 0.0]
nivsMemDrogArmas = [0.0, 0.0, 0.0]
nivsMemInseguridad = [0.0, 0.0, 0.0, 0.0]

def posNivMemMayor(nivelesMem):
	posMayor = 0
	mayor = 0.0
	for i in range(len(nivelesMem)):
		if nivelesMem[i] > mayor:
			mayor = nivelesMem[i]
			posMayor = i
	return posMayor

def prodMembsAsaltoRobo(valorAsRob):
	nivsMemAsaltoRobo[0] = curva_z(valorAsRob, 10, 30)
	nivsMemAsaltoRobo[1] = triangular_suave(valorAsRob, 15, 50, 75)
	nivsMemAsaltoRobo[2] = curva_s(valorAsRob, 60, 80)

def prodMembsHomic(valorHomic):
	nivsMemHomic[0] = curva_z(valorHomic, 2, 4)
	nivsMemHomic[1] = triangular_suave(valorHomic, 2, 5, 8)
	nivsMemHomic[2] = curva_s(valorHomic, 6, 9)
	print(nivsMemHomic)

def prodMembsSecVioAcos(valorSeViAc):
	nivsMemSecVioAcos[0] = curva_z(valorSeViAc, 2, 5)
	nivsMemSecVioAcos[1] = triangular_suave(valorSeViAc, 3, 6, 9)
	nivsMemSecVioAcos[2] = curva_s(valorSeViAc, 6, 8)

def prodMembsDrogArmas(valorDroArm):
	nivsMemDrogArmas[0] = curva_z(valorDroArm, 10, 20)
	nivsMemDrogArmas[1] = triangular_suave(valorDroArm, 10, 25, 45)
	nivsMemDrogArmas[2] = curva_s(valorDroArm, 30, 40)

def fuzzyAsaltoRobo(valorAsRob):
	prodMembsAsaltoRobo(valorAsRob)
	membresia = conjAsaltoRobo[posNivMemMayor(nivsMemAsaltoRobo)]
	return membresia

def fuzzyHomic(valorHomic):
	prodMembsHomic(valorHomic)
	membresia = conjHomic[posNivMemMayor(nivsMemHomic)]
	return membresia

def fuzzySecVioAcos(valorSeViAc):
	prodMembsSecVioAcos(valorSeViAc)
	membresia = conjSecVioAcos[posNivMemMayor(nivsMemSecVioAcos)]
	return membresia

def fuzzyDrogArmas(valorDroArm):
	prodMembsDrogArmas(valorDroArm)
	membresia = conjDrogArmas[posNivMemMayor(nivsMemDrogArmas)]
	return membresia

# Reglas handcodeadas
def inferenciaCualitativa(AsaltoRoboDif, homicidioDif, secVioAcoDif,
	                       drogArmasDif):
	if ((drogArmasDif == 'Baja' or homicidioDif == 'Baja') and secVioAcoDif == 'Baja' and AsaltoRoboDif == 'Baja'):
	    inseguridadDifuso = "Baja"

	elif ((drogArmasDif == 'Media' or homicidioDif == 'Media') and secVioAcoDif == 'Baja' and AsaltoRoboDif == 'Baja'):
	    inseguridadDifuso = "Media"

	elif ((drogArmasDif == 'Alta' or homicidioDif == 'Alta') and secVioAcoDif == 'Baja' and AsaltoRoboDif == 'Baja'):
	    inseguridadDifuso = "Alta"

	elif ((drogArmasDif == 'Baja' or homicidioDif == 'Baja') and secVioAcoDif == 'Media' and AsaltoRoboDif == 'Baja'):
	    inseguridadDifuso = "Baja"

	elif ((drogArmasDif == 'Media' or homicidioDif == 'Media') and secVioAcoDif == 'Media' and AsaltoRoboDif == 'Baja'):
	    inseguridadDifuso = "Media"

	elif ((drogArmasDif == 'Alta' or homicidioDif == 'Alta') and secVioAcoDif == 'Media' and AsaltoRoboDif == 'Baja'):
	    inseguridadDifuso = "Alta"

	elif ((drogArmasDif == 'Baja' or homicidioDif == 'Baja') and secVioAcoDif == 'Alta' and AsaltoRoboDif == 'Baja'):
	    inseguridadDifuso = "Media"

	elif ((drogArmasDif == 'Media' or homicidioDif == 'Media') and secVioAcoDif == 'Alta' and AsaltoRoboDif == 'Baja'):
	    inseguridadDifuso = "Alta"

	elif ((drogArmasDif == 'Alta' or homicidioDif == 'Alta') and secVioAcoDif == 'Alta' and AsaltoRoboDif == 'Baja'):
	    inseguridadDifuso = "Critica"

	elif ((drogArmasDif == 'Baja' or homicidioDif == 'Baja') and secVioAcoDif == 'Baja' and AsaltoRoboDif == 'Media'):
	    inseguridadDifuso = "Baja"

	elif ((drogArmasDif == 'Media' or homicidioDif == 'Media') and secVioAcoDif == 'Baja' and AsaltoRoboDif == 'Media'):
	    inseguridadDifuso = "Alta"

	elif ((drogArmasDif == 'Alta' or homicidioDif == 'Alta') and secVioAcoDif == 'Baja' and AsaltoRoboDif == 'Media'):
	    inseguridadDifuso = "Alta"

	elif ((drogArmasDif == 'Baja' or homicidioDif == 'Baja') and secVioAcoDif == 'Media' and AsaltoRoboDif == 'Media'):
	    inseguridadDifuso = "Media"

	elif ((drogArmasDif == 'Media' or homicidioDif == 'Media') and secVioAcoDif == 'Media' and AsaltoRoboDif == 'Media'):
	    inseguridadDifuso = "Alta"

	elif ((drogArmasDif == 'Alta' or homicidioDif == 'Alta') and secVioAcoDif == 'Media' and AsaltoRoboDif == 'Media'):
	    inseguridadDifuso = "Alta"

	elif ((drogArmasDif == 'Baja' or homicidioDif == 'Baja') and secVioAcoDif == 'Alta' and AsaltoRoboDif == 'Media'):
	    inseguridadDifuso = "Media"

	elif ((drogArmasDif == 'Media' or homicidioDif == 'Media') and secVioAcoDif == 'Alta' and AsaltoRoboDif == 'Media'):
	    inseguridadDifuso = "Alta"

	elif ((drogArmasDif == 'Alta' or homicidioDif == 'Alta') and secVioAcoDif == 'Alta' and AsaltoRoboDif == 'Media'):
	    inseguridadDifuso = "Critica"

	elif ((drogArmasDif == 'Baja' or homicidioDif == 'Baja') and secVioAcoDif == 'Baja' and AsaltoRoboDif == 'Alta'):
	    inseguridadDifuso = "Media"

	elif ((drogArmasDif == 'Media' or homicidioDif == 'Media') and secVioAcoDif == 'Baja' and AsaltoRoboDif == 'Alta'):
	    inseguridadDifuso = "Alta"

	elif ((drogArmasDif == 'Alta' or homicidioDif == 'Alta') and secVioAcoDif == 'Baja' and AsaltoRoboDif == 'Alta'):
	    inseguridadDifuso = "Critica"

	elif ((drogArmasDif == 'Baja' or homicidioDif == 'Baja') and secVioAcoDif == 'Media' and AsaltoRoboDif == 'Alta'):
	    inseguridadDifuso = "Alta"

	elif ((drogArmasDif == 'Media' or homicidioDif == 'Media') and secVioAcoDif == 'Media' and AsaltoRoboDif == 'Alta'):
	    inseguridadDifuso = "Alta"

	elif ((drogArmasDif == 'Alta' or homicidioDif == 'Alta') and secVioAcoDif == 'Media' and AsaltoRoboDif == 'Alta'):
	    inseguridadDifuso = "Critica"

	elif ((drogArmasDif == 'Baja' or homicidioDif == 'Baja') and secVioAcoDif == 'Alta' and AsaltoRoboDif == 'Alta'):
	    inseguridadDifuso = "Alta"

	elif ((drogArmasDif == 'Media' or homicidioDif == 'Media') and secVioAcoDif == 'Alta' and AsaltoRoboDif == 'Alta'):
	    inseguridadDifuso = "Critica"

	elif ((drogArmasDif == 'Alta' or homicidioDif == 'Alta') and secVioAcoDif == 'Alta' and AsaltoRoboDif == 'Alta'):
	    inseguridadDifuso = "Critica"

	return inseguridadDifuso


def inferenciaCuantitativa(AsaltoRoboDif, homicidioDif, secVioAcoDif,
	                       drogArmasDif):
	nivMemAsaltoRobo = nivsMemAsaltoRobo[posNivMemMayor(nivsMemAsaltoRobo)]
	nivMemHomic = nivsMemHomic[posNivMemMayor(nivsMemHomic)]
	nivMemSecVioAcos = nivsMemSecVioAcos[posNivMemMayor(nivsMemSecVioAcos)]
	nivMemDrogArmas = nivsMemDrogArmas[posNivMemMayor(nivsMemDrogArmas)]

	nivMemInseguridad = compAnd(compAnd(compOr(nivMemDrogArmas, nivMemHomic), nivMemSecVioAcos), nivMemAsaltoRobo)

	if ((drogArmasDif == 'Baja' or homicidioDif == 'Baja') and secVioAcoDif == 'Baja' and AsaltoRoboDif == 'Baja'):
	    nivsMemInseguridad[0]  = nivMemInseguridad

	elif ((drogArmasDif == 'Media' or homicidioDif == 'Media') and secVioAcoDif == 'Baja' and AsaltoRoboDif == 'Baja'):
	    nivsMemInseguridad[1] = nivMemInseguridad

	elif ((drogArmasDif == 'Alta' or homicidioDif == 'Alta') and secVioAcoDif == 'Baja' and AsaltoRoboDif == 'Baja'):
	    nivsMemInseguridad[2] = nivMemInseguridad

	elif ((drogArmasDif == 'Baja' or homicidioDif == 'Baja') and secVioAcoDif == 'Media' and AsaltoRoboDif == 'Baja'):
	    nivsMemInseguridad[0] = nivMemInseguridad

	elif ((drogArmasDif == 'Media' or homicidioDif == 'Media') and secVioAcoDif == 'Media' and AsaltoRoboDif == 'Baja'):
	    nivsMemInseguridad[1] = nivMemInseguridad

	elif ((drogArmasDif == 'Alta' or homicidioDif == 'Alta') and secVioAcoDif == 'Media' and AsaltoRoboDif == 'Baja'):
	    nivsMemInseguridad[2] = nivMemInseguridad

	elif ((drogArmasDif == 'Baja' or homicidioDif == 'Baja') and secVioAcoDif == 'Alta' and AsaltoRoboDif == 'Baja'):
	     nivsMemInseguridad[1] = nivMemInseguridad

	elif ((drogArmasDif == 'Media' or homicidioDif == 'Media') and secVioAcoDif == 'Alta' and AsaltoRoboDif == 'Baja'):
	    nivsMemInseguridad[2] = nivMemInseguridad

	elif ((drogArmasDif == 'Alta' or homicidioDif == 'Alta') and secVioAcoDif == 'Alta' and AsaltoRoboDif == 'Baja'):
	    nivsMemInseguridad[3] = nivMemInseguridad

	elif ((drogArmasDif == 'Baja' or homicidioDif == 'Baja') and secVioAcoDif == 'Baja' and AsaltoRoboDif == 'Media'):
	    nivsMemInseguridad[0] = nivMemInseguridad

	elif ((drogArmasDif == 'Media' or homicidioDif == 'Media') and secVioAcoDif == 'Baja' and AsaltoRoboDif == 'Media'):
	    nivsMemInseguridad[2] = nivMemInseguridad

	elif ((drogArmasDif == 'Alta' or homicidioDif == 'Alta') and secVioAcoDif == 'Baja' and AsaltoRoboDif == 'Media'):
	    nivsMemInseguridad[2] = nivMemInseguridad

	elif ((drogArmasDif == 'Baja' or homicidioDif == 'Baja') and secVioAcoDif == 'Media' and AsaltoRoboDif == 'Media'):
	    nivsMemInseguridad[1] = nivMemInseguridad

	elif ((drogArmasDif == 'Media' or homicidioDif == 'Media') and secVioAcoDif == 'Media' and AsaltoRoboDif == 'Media'):
	    nivsMemInseguridad[2] = nivMemInseguridad

	elif ((drogArmasDif == 'Alta' or homicidioDif == 'Alta') and secVioAcoDif == 'Media' and AsaltoRoboDif == 'Media'):
	    nivsMemInseguridad[2] = nivMemInseguridad

	elif ((drogArmasDif == 'Baja' or homicidioDif == 'Baja') and secVioAcoDif == 'Alta' and AsaltoRoboDif == 'Media'):
	    nivsMemInseguridad[1] = nivMemInseguridad

	elif ((drogArmasDif == 'Media' or homicidioDif == 'Media') and secVioAcoDif == 'Alta' and AsaltoRoboDif == 'Media'):
	    nivsMemInseguridad[2] = nivMemInseguridad

	elif ((drogArmasDif == 'Alta' or homicidioDif == 'Alta') and secVioAcoDif == 'Alta' and AsaltoRoboDif == 'Media'):
	    nivsMemInseguridad[3] = nivMemInseguridad

	elif ((drogArmasDif == 'Baja' or homicidioDif == 'Baja') and secVioAcoDif == 'Baja' and AsaltoRoboDif == 'Alta'):
	    nivsMemInseguridad[1] = nivMemInseguridad

	elif ((drogArmasDif == 'Media' or homicidioDif == 'Media') and secVioAcoDif == 'Baja' and AsaltoRoboDif == 'Alta'):
	    nivsMemInseguridad[2] = nivMemInseguridad

	elif ((drogArmasDif == 'Alta' or homicidioDif == 'Alta') and secVioAcoDif == 'Baja' and AsaltoRoboDif == 'Alta'):
	    nivsMemInseguridad[3] = nivMemInseguridad

	elif ((drogArmasDif == 'Baja' or homicidioDif == 'Baja') and secVioAcoDif == 'Media' and AsaltoRoboDif == 'Alta'):
	    nivsMemInseguridad[2] = nivMemInseguridad

	elif ((drogArmasDif == 'Media' or homicidioDif == 'Media') and secVioAcoDif == 'Media' and AsaltoRoboDif == 'Alta'):
	    nivsMemInseguridad[2] = nivMemInseguridad

	elif ((drogArmasDif == 'Alta' or homicidioDif == 'Alta') and secVioAcoDif == 'Media' and AsaltoRoboDif == 'Alta'):
	    nivsMemInseguridad[3] = nivMemInseguridad

	elif ((drogArmasDif == 'Baja' or homicidioDif == 'Baja') and secVioAcoDif == 'Alta' and AsaltoRoboDif == 'Alta'):
	    nivsMemInseguridad[2] = nivMemInseguridad

	elif ((drogArmasDif == 'Media' or homicidioDif == 'Media') and secVioAcoDif == 'Alta' and AsaltoRoboDif == 'Alta'):
	    nivsMemInseguridad[3] = nivMemInseguridad

	elif ((drogArmasDif == 'Alta' or homicidioDif == 'Alta') and secVioAcoDif == 'Alta' and AsaltoRoboDif == 'Alta'):
	    nivsMemInseguridad[3] = nivMemInseguridad

	return nivsMemInseguridad[posNivMemMayor(nivsMemInseguridad)]

def desfuzzificar(inseguridadDifuso, nivMemInseguridad):
	if inseguridadDifuso == "Baja":
		return nivMemInseguridad * 25
	elif inseguridadDifuso == "Media":
		return nivMemInseguridad * 50
	elif inseguridadDifuso == "Alta":
		return nivMemInseguridad * 75
	elif inseguridadDifuso == "Critica":
		return nivMemInseguridad * 100
	else:
		return 0.0
