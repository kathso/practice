from animal import Animal

def main():
	generic_animal = Animal()
	generic_animal.set_legs(4)
	generic_animal.set_tail(True)
	print('Our generic animal has [{}] legs'.format(generic_animal.get_legs()))
	print('Our generic animal has [{}] tail'.format(generic_animal.get_tail()))


if "__name__" == main():
	main()




