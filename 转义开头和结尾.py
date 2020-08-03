#-------------用\作为转义字符开头
import re
# mypath='G:\\py资料\\1-上课资料\\4-正则表达式课件'
# print(mypath)

#-------------路径进行转义，需要把每个斜杠加一个斜杠
# print(re.match('c:\\\\a.txt','c:\\a.txt').group())


#-------------不进行转义加r，表示使用原生字符串
print(re.match(r'c:\\a.txt','c:\\a.txt').group())