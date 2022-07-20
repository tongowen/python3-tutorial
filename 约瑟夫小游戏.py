# -*- coding UTF-8 -*-

people = {}

for i in range(1,31):
	people[i] = 1
	# print(people)

check = 0 # 代表报数报到几了，1-9
i = 1 # 代表当前报数的人，1-30
j = 0 # 代表已被踢出的人数

while i <= 31:
	if i == 31:
		i = 1
	elif j == 15:
		break
	else:
		if people[i] == 0: # 等于0代表已经下船了
			i += 1
			continue
		else:
			check += 1
			if check == 9:
				people[i] = 0
				check = 0
				print("{}号下船了" .format(i))
				j += 1
			else:
				i += 1
				continue
