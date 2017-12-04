# -*- coding: utf-8 -*-
import re


#编译标志让你可以修改正则表达式的一些运行方式
#多个标志可以通过按位 OR-ing 它们来指定
#如 re.I | re.M 。flags都有两种形式，缩写和全写都可以
#
#
#flas:(部分)
#I  IGNORECASE  忽略字母大小写
#
#M  MULTILINE   多行匹配，影响^和$
#
#S  DOTALL      使.匹配包括换行在内的所有字符
#
#X 	VERBOSE     在 RE 字符串中的空白符被忽略，除非该空白符在字符类中或在反斜杠之后。
#				它也可以允许你将注释写入 RE，这些注释会被引擎忽略；注释用 “#”号 来标识，不过该符号不能在字符串或反斜杠之后。
#
#U 				根据Unicode字符集解析字符，这个标志影响\w,\W,\b,\B
	

#匹配语法：
#1、字符：
# .		匹配除‘\n’的字符(在DOTALL re.S模式中也能匹配换行符'\n')
# \		转义字符  
# [...] 字符集 对应位置可以是该字符集中的任意内容
# 		可以逐个列出 也可给出范围 如[abc] [a-c]
# 		第一个字符是^表示取反 如[^abc] 表示除abc的其他字符
# 		
#2、预定义字符集
# \d 	数字[0-9] 如a\dc 能匹配到 a1c
# \D    非数字：[^\d]  如a\Dc 能匹配到 abc
# \s    空白字符：[<space>\t\r\n\f\v] 如a\sc 能匹配到 a c 
# \S    非空白字符：[^<space>\t\r\n\f\v] 如a\Sc 能匹配到 abc 
# \w    单词字符及下划线[A-Za-z0-9_]
# \W    [^\w]
# 
# 3、数量词(用在字符或(...)后)
# *		匹配前一个字符0次或无限次	abc*		ab|abccc
# +		匹配前一个字符1次或无限次   abc+		abc|abccc
# ?		匹配前一个字符0次或1次		abc?		ab|abc
# {m}	匹配前一个字符m次			ab{3}c		abbbc
# {m,n}	匹配前一个字符m至n次		ab{1,2}c 	abc|abbc
# 
# [*+?{m}{m,n}]+?  	变成非贪婪模式
# 贪婪模式：	ab+   abbbc	 ->abbb
# 非贪婪模式:	ab+?  abbbc  ->ab
# 
# 
# 
#4、边界匹配(不消耗待匹配字符串中的字符)
# ^ 	匹配字符串开头 在多行模式(re.M)中匹配每一行的开头		^abc	abc
# $ 	匹配字符串末尾 在多行模式(re.M)中匹配每一行的末尾		abc$	abc
# \A 	仅匹配字符串开头										\Aabc	abc
# \Z 	仅匹配字符串末尾 										abc\Z 	abc
# \b    匹配\w和\W 之间 的字符									ve\b	give! up		ve	
# 																ve\b    giveup          无	
# 														
# \B 	[^\b]匹配\w和\W 之外 的字符								ab\B	abcd		    ab	
#
#5、逻辑 分组
# |			左右任意一个
# (...)		分组表达式 从表达式开始每遇到一个‘(’，编号+1 		(.*) am (.*)		I am boy 	  .group(1) =  I 
# 			可后接数量词															
#																								  .group(2) =  boy											
#																																										
#
#																																																																						
#Python 原生字符串																																																																																																																																												
#	r‘\b’ = '\\b'	
#	使表达式更自然																																																																																																																																																																																																																																																																																							ab\B    ab cd   		无




#re.match()		尝试从字符串的 起始位置匹配 若起始位置不符合 则返回None

'''
line = 'I am boy'
matchObj = re.match('.* am (.*)',line,re.I)
print(matchObj)
print(matchObj.group(1))
'''




#re.search()	扫描整个字符串并返回 第一个 成功的匹配   

'''
line = "www.baidu.comcom2"
print(re.search(r"com",line))
#<_sre.SRE_Match object; span=(10, 13), match='com'>
'''

#re.compile()	编译正则表达式模式，返回一个对象的模式
'''
line = "I am Boy I like Girl"
r 	 =re.compile(r'[A-Z]\w*')
print(r.findall(line))
'''


#re.findall()	遍历匹配 可以获取字符串中所有匹配的字符串 返回一个列表

line = "I am 353563Boy 564I l464ike 64Girl"
print(re.findall(r'36[A-Z]\w*',line))



#re.split()		按照能够匹配的子串将string分割后返回列表
'''
line = 'I_Am_Boy_I_Like_Girl'
print(re.split(r'[_]',line))
#OUT-> : ['I', 'Am', 'Boy', 'I', 'Like', 'Girl']
'''


