msg1="Hello Welcome to File Input & Output\n"
msg2="Lets Start the Lecture\n"
msg3="We'll go from Starting Onwards\n"
f=open('messages','w')
f.write(msg1)
f.write(msg2)
f.write(msg3)
f=open('messages','r')
data=f.read()
print(data)
f.close()
#######################################################################################################
msg="Hello This is Pavan"
f=open(msg,"w")
f.write(msg)
f=open(msg,"r")
data=f.read()
print(data)
f.close()