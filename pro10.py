class Demo():
  def __init__(self,a,b):
    self.a=a
    self.b=b
    c=a+b
    print(c)
  def display(self):
    print("value of a is",self.a)
    print("value of b is",self.b)

obj=Demo(10,20)
obj.display()
