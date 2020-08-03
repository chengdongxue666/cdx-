import re
#------------------- *匹配前一个字符出现0次或者无限次 可有可无
# res=re.match('[A-Z][a-z]*','Mya')
# print(res.group())


#-------------------  +匹配前一个字符出现1次或者无限次  即至少有一次
#例如匹配符合规范：不能以数字开头,只能包含数字、字母、下划线
# result=re.match('[a-zA-Z]+','name')
# print(result.group())

#------------------- ?匹配前一个字符出现一次或者0次，即要么有一次要么有没有
#？告诉引擎匹配前导字符0次或一次
# result=re.match('[a-zA-Z][0-9]?','ncme')
# print(result.group())


#-------------------{m}匹配前导字符出现m次
# result=re.match('\d{3}','123')
# print(result.group())


#-------------------{m，}匹配前一个字符至少出现m次
# result=re.match('\d{2,}','1234567')
# print(result.group())


#-------------------{n，m}匹配前一个字符出现n到m次
# result=re.match('\d{2,9}','1234567')
# print(result.group())


#-------------------匹配一个163后缀的邮箱
regexMail=re.match('[a-zA-Z0-9]{6,11}@163.com','dewdee233@163.com')
print(regexMail.group())