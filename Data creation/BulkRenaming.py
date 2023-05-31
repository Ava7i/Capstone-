import os

i = 1322
path="./Image/T/"
for filename in os.listdir(path):
	my_dest = "R_" + str(i) + ".jpg"
	my_source = path + filename
	my_dest = path + my_dest

	os.rename(my_source, my_dest)
	i += 1