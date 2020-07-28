#单例模式，是一种常用的软件设计模式，目的是确保某一个类只有一个实例存在
#创建一个单例模式，基于__new__去实现

class DataBaseClass(object):
    def __new__(cls, *args, **kwargs):


#判断这个对象实例是否存在，如果存在就不创建了
        if not hasattr(cls,'_instance'):
            cls._instance=super().__new__(cls,*args,**kwargs)
        return cls._instance
    pass
db1 = DataBaseClass()
