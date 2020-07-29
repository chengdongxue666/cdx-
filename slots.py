class Student(object):
    #声明了slots，就限制了属性，属性不在这个范围就不能添加
     __slots__ = ('name','age')
     def __str__(self):
        return '{}...{}'.format(self.name,self.age)

     pass
xw=Student()
xw.name="小王"
xw.age=20
#xw.score=100  这个属性添加后就会报错，因为没有在slots中声明
print(xw)
print(xw.__slots__)


#子类没有声明slots时，不会继承父类的slots属性声明限制
#子类声明slots时，将会继承父类的这个slots的范围，也就是子类slots的范围是其自身+父类的__slots__