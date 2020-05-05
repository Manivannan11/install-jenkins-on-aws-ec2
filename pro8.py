import sys
print(sys.version)
a=str(input('enter a keyword:'))
f=open("/home/ec2-user/man/install-jenkins-on-aws-ec2/sample.txt","r+,w+")
count=0
for line in f.readlines():
   count+=1
   print(line)
   if a in line:
      print("keyword found in the line:",count)
f.close()
