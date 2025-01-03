def build_person(first_name, last_name, age=None):
	# dans condition, None=False
	"""renvoie un Dict d'infos sur une personne"""
	person={'first':first_name, 'last':last_name}
	if age:
		person['age']=age
	return person

musician=build_person('jimi', 'hendrix')
print(musician)
musician=build_person('aretha', 'franklin', age=87)
print(musician)