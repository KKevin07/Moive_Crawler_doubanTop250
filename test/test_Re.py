#正则表达式： 字符串的规定,字符串的模式
#可用于判断字符串的模式，判断字符串是否符合一定的标准

'''   正则表达式的常用操作符

.        表示任何单个字符
[]       字符集，对单个字符给出取值范围
[^ ]     非字符集，对单个字符给出排除范围
*        前一个字符0次或无限次扩展
+        前一个字符1次或无限次扩展
?        前一个字符0次或1次扩展
|        左右表达式任意一个
{m}      扩展前一个字符m次
{m,n}    扩展前一个字符m至n次（含n）
^        匹配字符串的开头
$        匹配字符串的结尾
()       分组标记，内部只能使用 | 操作符
\d       数字，等价于[0-9]
\w       单词字符，等价于[A-Za-z0-9_]   包含‘A-Z’  ‘a-z’  ‘0-9’  ‘_’
'''

'''
re库主要功能函数

   re.search()       在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
*  re.march()        从一个字符串的开始位置起匹配正则表达式，返回match对象
*  re.findall()      搜索字符串，以列表类型返回全部能匹配的子串
   re.split()        将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
   re.finditer()     搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
*  re.sub()          在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串

'''

'''
正则表达式可以包含一些可选标志修饰符来控制匹配的模式。
修饰符被指定为一个可选的标志。
多个标志可以通过按位OR(|)来指定，如re.I | re.M被设置成I和M的标志

*   re.I    使匹配对大小写不敏感
    re.L    做本地化识别（locale-aware）匹配
    re.M    多行匹配，影响^和$
*   re.S    使'.'匹配包括换行在内的所有字符
    re.U    根据Unicode字符集解析字符。这个标志影响\w,\W,\b,\B
    re.X    该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解

'''














