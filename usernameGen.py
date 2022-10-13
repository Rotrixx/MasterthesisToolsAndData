import argparse

delimiter = ['', '.', '_', '+']

usernames = []

def genUsername(firstName, lastName, delim, uList):
	uList.append(f"{firstName}{delim}{lastName}")
	uList.append(f"{firstName[0]}{delim}{lastName}")
	uList.append(f"{firstName}{delim}{lastName[0]}")

if __name__=="__main__":
	parser = argparse.ArgumentParser(description='Generating username candidates.')
	parser.add_argument('-f', action='store')
	parser.add_argument('-l', action='store')
	parser.add_argument('-o', action='store', default="")

	args = parser.parse_args()

	for d in delimiter:
		genUsername(args.f.lower(), args.l.lower(), d, usernames)
		
	if args.o != "":
		with open(args.o, "w") as f:
                        for user in usernames:
                            f.write(user + "\n")
	else:
		for user in usernames:
			print(user)
