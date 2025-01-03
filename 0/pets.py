def describe_pet(animal_type, pet_name):
	print(f"\nJ'ai un {animal_type}.")
	print(f"Mon {animal_type} s'appelle {pet_name.title()}")
	
describe_pet(animal_type='chien', pet_name='simba')