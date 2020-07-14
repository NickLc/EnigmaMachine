from pprint import pprint
from string import ascii_uppercase

ROTOR_PERMUTATIONS = [  "EKMFLGDQVZNTOWYHXUSPAIBRCJ",  "AJDKSIRUXBLHWTMCQGZNPYFVOE",  "BDFHJLCPRTXVZNYEIWGAKMUSQO"]
REFLECTOR_PERMUTATION = "IXUHFEZDAOMTKQJWNSRLCYPBVG"



INDEXES_ROTOR_PERMUTATIONS = []

for permutation in ROTOR_PERMUTATIONS:
	string_permutation = list(map(lambda char : ascii_uppercase.find(char), permutation))
	INDEXES_ROTOR_PERMUTATIONS.append(string_permutation)


INDEX_REFLECTOR_PERMUTATION = list(map(lambda char : ascii_uppercase.find(char), REFLECTOR_PERMUTATION))

for index_permutation in INDEXES_ROTOR_PERMUTATIONS:
	print(index_permutation)
print(INDEX_REFLECTOR_PERMUTATION)