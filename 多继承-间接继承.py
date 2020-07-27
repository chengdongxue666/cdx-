
class GrandFather:
    def eat(self):
        print("吃的方法")
        pass
    pass
class Father(GrandFather):
    pass
class Son(Father):
    pass

son=Son()
son.eat()