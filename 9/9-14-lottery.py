from random import randint

result=[1,8,98,34,56,4,17,45,36,10,'p','u','e']


count=0
while count<4:
	x=randint(1,11)
	print(result[x])
	result.remove(result[x])
	count+=1

print(result)
