import re

#--------------- |匹配左右任意一个表达式（从左往右）实际上是一个或的关系
string = 'cdcdcedcf8888'
result=re.match('(cdcdcedcf|cdcdcedcf8888)',string)
print(result.group())



#---------------- （ab）将括号中的字符作为一个组
#例如匹配电话号码    xxxx-123456789
res=re.match('([0-9]*)-\d*','0355-11132323')
print(res.group(0))#group默认为0，整体组
print(res.group(1))
print(res.group(2))

#----------------- /num 引用分组num匹配到的字符串
htmlTag='<html><h1>测试数据</h1></html>'
res=re.match(r'<(.+)><(.+)>(.+)</\2></\1>',htmlTag)
print(res.group(1))
print(res.group(2))
print(res.group(3))
