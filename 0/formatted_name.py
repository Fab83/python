def get_formatted_name(first_name, last_name, country=''):
	full_name=f"{first_name} {last_name}"
	if country:
		full_name += f" born in {country}"
	return full_name.title()

musician=get_formatted_name('jimi', 'hendrix')
print(musician)

musician=get_formatted_name('jimmy', 'page', 'usa')
print(musician)