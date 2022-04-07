import re

newList = []

with open('preproinsulin.txt') as file:
	for line in file:
		for i in line:
			if i != " " and i != "\n" and i != "/": # and islower(i)
				newList.append(i)
	print(newList)


old_string = "".join(newList)
new_string1 = re.sub(r"[ORIGIN16]", "", old_string)


if (len(new_string1)) == 110:
	print(new_string1)
else:
	print("Not there yet")

with open('isinsulin.txt', 'w') as file1:
	file1.write(new_string1[0:24])
	print(new_string1[0:24])
with open('binsulin.txt', 'w') as file2:
	file1.write(new_string1[24:54])
	print(new_string1[24:54])
with open('cinsulin.txt', 'w') as file3:
	file1.write(new_string1[54:89])
	print(new_string1[54:89])
with open('ainsulin.txt', 'w') as file4:
	file1.write(new_string1[89:110])
	print(new_string1[89:110])
