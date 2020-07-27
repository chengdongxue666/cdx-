#孙悟空是神仙，并且也喜欢吃桃子
class shenxian:
    def fly(self):
        print('神仙都会飞')
    pass

class Monkey():
    def chitao(self):
        print("猴子喜欢吃桃子")
    pass
class Sunwokong(shenxian,Monkey):
     pass
swk=Sunwokong()
swk.chitao()
swk.fly()
