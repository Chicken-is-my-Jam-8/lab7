import random
two_d_list = []
for x in range(3):
	two_d_list.append([])
	for y in range(4):
		two_d_list[x].append(random.randrange(1, 100))
for z in range(3):
	print(str(two_d_list[z]).rstrip(','))
		
		
