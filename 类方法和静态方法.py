class People:
    country ='china'#类属性的值为china
    #类方法  用 classmethod来进行修饰
    @classmethod
    def get_country(self):
        return self.country#访问类属性
        pass
    # 在类方法里修改类属性的值
    @classmethod
    def change_country(self,data):
        self.country=data
        pass
    pass
print(People.get_country())#通过类对象去引用类方法
p=People()
print('实例对象访问  %s'%p.get_country())#通过实例对象去引用类方法



print('---------------修改之后的数据---------------')
# 在类方法里修改类属性
People.change_country('英国')
print(People.get_country())
