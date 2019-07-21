n=input()
arr=list(map(int, input().split()))
arr.sort()
arr.reverse()
for i in arr:
	print(i,end="")
