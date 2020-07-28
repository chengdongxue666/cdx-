#私有化属性
# class Person(object):
#       __age = 18


#私有化方法
class Animal:
    def __eat(self):
        print('吃东西')
    pass
    def run(self):
        self.__eat()#在类的内部可以调用私有化方法
        pass
class Bird(Animal):
        pass

b1=Bird()
b1.run()