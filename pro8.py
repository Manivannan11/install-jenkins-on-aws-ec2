a=raw_input('enter a keyword:')
f=open("/home/ec2-user/man/install-jenkins-on-aws-ec2/sample.txt","r+,w+")
count=0
for line in f.readlines():
   count+=1
   if a in line:
      print("keyword found in the line:",count)
f.close()
