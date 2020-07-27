class Animal:
    def eat(self):
        print('吃饭了')
        pass
    def drink(self):
        pass
class Dog(Animal):#继承父类Animal
    def wwj(self):
        print("小狗汪汪叫")

class Cat(Animal):
     def wwj(self):
        print("小猫喵喵叫")
d1=Dog()
d1.eat()