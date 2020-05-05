f=open("/home/ec2-user/man/install-jenkins-on-aws-ec2/sample.txt","r+")
a=[]
for line in f.readlines():
   print(line)
   value=line.split()
   a.append([value[0],value[1],value[2]])
print(a)
f.close()
print(a[0][1])
