#动态添加实例方法需要使用types
import types
def dymicMethed(self):
    print('{}的体重是{}kg，在{}读大学'.format(self.name,self.weight,Student.shcools))
    pass

class Student:
     def __init__(self,name,age):
         self.name=name
         self.age=age
     pass
     def __str__(self):
         return '{}今天{}岁'.format(self.name,self.age)
     pass
zyh=Student('张艳华','20')
print(zyh)
zyh.weight=50#动态添加实例属性
print('-------------动态添加实例方法----------------')
zyh.printInfo=types.MethodType(dymicMethed,zyh)#动态绑定方法

# print(zyh.weight)
# print('-------------另外一个实例对象 张明----------------')
# zm=Student('张明','20')

print('-------------给类对象添加属性----------------')
Student.shcools='北京邮电大学'
print(zyh.shcools)

zyh.printInfo() #调用动态绑定的方法


