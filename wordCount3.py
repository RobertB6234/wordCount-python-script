def wordcount(filename, listwords):
	try:
		file = open(filename, "r")
		read = file.readlines()
		file.close()
		for word in listwords:
			lower = word.lower()
			count = 0
			for sentance in read:
				line = sentance.split()
				for each in line:
					line2 = each.lower()
					line2 = line2.strip("!@#$%^&*()_-+=")
					if lower == line2:
						count += 1
			print(lower, ":", count)
	except FileExistsError:
		print("This file is not there")
		
wordcount("CustReviews.csv", ['smell'])