class SgClass:
    def __init__(self,name,color):
        self.color=color
        self.name=name
        pass
    def __str__(self):
        return '%s 的颜色是 %s'%(self.name,self.color)
pg=SgClass('苹果','红色’)
print(pg)