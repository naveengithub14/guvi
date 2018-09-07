lower_limit,upper_limit = map(int,input().split())
lower_limit = int(lower_limit)
upper_limit = int(upper_limit)
for i in range(lower_limit+1,upper_limit+1):
	if(i%2 != 0):
		print(i)
