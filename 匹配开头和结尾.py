import re

#-------------- ^匹配字符串开头
# result=re.match('^P.*','Python  is langage')
# print(result.group())


#-------------- $匹配字符串结尾
regexMail=re.match('[\w]{5,15}@[\w]{2,3}.com$','dewdee233@163.com')
print(regexMail.group())
