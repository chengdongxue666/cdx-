class People():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self,food):
        print(self.name+'喜欢吃'+food)
a = People("小明","12")
a.eat("香蕉")
