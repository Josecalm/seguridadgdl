from sys import argv
from app.sistemaFuzzy import *

def generate_fuzzy_values(assaults, homicides, sexualCrimes, weaponDrugsPos):

	# Valores Nitidos
	asaltosRobosNit = float(assaults)
	homicidiosNit = float(homicides)
	secuestrosNit = float(sexualCrimes)
	drogasArmasNit = float(weaponDrugsPos)

	# Valores fuzzificados
	asaltosRobosDif = fuzzyAsaltoRobo(asaltosRobosNit)
	homicidiosDif = fuzzyHomic(homicidiosNit)
	secuestrosDif = fuzzySecVioAcos(secuestrosNit)
	drogasArmasDif = fuzzyDrogArmas(drogasArmasNit)

	# Resultados Fuzzy
	# print "Asaltos = " + str(asaltosRobosNit) + " corresponde " + str(asaltosRobosDif)
	# print "Homicidios = " + str(homicidiosNit) + " corresponde " + str(homicidiosDif)
	# print "Secuestros = " + str(secuestrosNit) + " corresponde " + str(secuestrosDif)
	# print "Drogas/Armas = " + str(drogasArmasNit) + " corresponde " + str(drogasArmasDif)

	# Inferencia Cualitativa
	inseguridadDif = inferenciaCualitativa(asaltosRobosDif, homicidiosDif, secuestrosDif,
						drogasArmasDif)
	# print "El nivel de inseguridad de la zona es: " + inseguridadDif
	# Nivel de certeza
	nivMemInseguridad = inferenciaCuantitativa(asaltosRobosDif, homicidiosDif, secuestrosDif,
						drogasArmasDif)
	# print "Con una certeza de: " + str(nivMemInseguridad)

	# Desfuzzificacion
	inseguridadNit = desfuzzificar(inseguridadDif, nivMemInseguridad)
	# print "El valor de la desfuzzificacion es: " + str(inseguridadNit)

	return inseguridadDif