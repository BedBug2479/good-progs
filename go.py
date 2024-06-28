w=int(input("Enter window size "))
w=(2**w)-1
f=int(input("Enter Frame Size "))
print("Enter {} frames ".format(f))
frames=input().split(" ")
i=0
j=1
while j+i<=f:
	if j%w==0:
		print(frames[i+j-1])
		ack=int(input("Enter last Acknowledgement recieved "))
		i=i+ack+1
		j=0
	else:
		print(frames[i+j-1],end=' ')
	if (i+j-1)==f:
		break
	j=j+1
print("")
print("All frames are sent")
