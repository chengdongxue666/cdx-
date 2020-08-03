#--------------------.点的使用  【匹配除了换行符之外的字符
#例子1
import re
# data = 'a2aa'
# parrtern='..'
# res = re.match(parrtern,data)
# print(res.group())

# #例子2
# names = '李达','李明','张浩'
# parrtern='李.'
# for name in names:
#     res = re.match(parrtern,name)
#     if res:
#        print(res.group())

#------------------[]中括号的使用 匹配规则是：匹配括号中的任意一个字符
# str1='hello'
# res=re.match('[he]',str1)
# print(res.group())
#[abc]代表可以匹配a或者b或者c

#------------------\d匹配一个数字 0-9   一个\d表示匹配一位，需要匹配几位就加几个\d
# data='12345adcfrc'
# print(re.match('\d',data).group())

#------------------\D匹配非数字
# data='a12345adcfrc'
# print(re.match('\D',data).group())

#-------------------\s 匹配一个空白字符或者tab键
# data=' a12345adcfrc'
# print(re.match('\s',data).group())

#-------------------\S 匹配非空白字符
# data='a12345adcfrc'
# print(re.match('\S',data).group())

#--------------------\w匹配单词字符,即a-z A-Z 0-9 _  一个\w表示匹配一位，需要匹配几位就加几个\w
# data='a12345adcfrc'
# print(re.match('\w',data).group())


#--------------------\W匹配非单词字符
# data='  a12345adcfrc'
# print(re.match('\W',data).group())