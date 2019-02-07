### data types

    int 1
    float 1.0
    str '1'
    bool True, False

### check data type with:
    type('1')
    > 'str'
    type(True)
    > 'bool'

### change data type  

    int('1') >> 1
    str(123) >> '123'
    bool(non-zero) >> True
    bool(0) >> False

## sequence

Tuple, List, range

**Common operations**

    'abc'[0] = 'a'; (a,b,c)[0] = 'a'; [a,b,c][0] = 'a'

> slice. 

    'abc'[0:2] = 'ab', ['a','b','c'][0:2] = ['a','b'], ('a', 'b','c')[0:2] = ('a', 'b')

> +, *

    'a' + 'b' = 'ab'
    'a' * 3 = 'aaa'
    ['a'] = ['a', 'a', 'a']

> in, not in

    'a' in 'abc' >> True
    'd' not in 'abc' >> True
    'c' in ['a', 'b'] >> False

> len(), max(), min()

    len('ab') >> 2
    len([1,3,'axb']) >> 3
    max('abc) >> 'c'
    max([1,2,3,'abc']) >> TypeError: '>' not supported between instances of 'str' and 'int'

    min([1,2,4]) >> 1
> AScii location
    ord('w') >> 119
    ord(1) >> TypeError: ord() expected string of length 1, but int found

> s.index(x, [, i[, j]])
Index of the first occurrence of x in s (at or after index i and before index j)


> s.count(x) total number of occurrences of x in s 


> string(text sequence type),  tuple, range are immutable. 



### string
    s = 'abc'

    s.lower()
    s.upper()
    s.swapcase()      
    s.capitalize()

    s.ljust(width[,fillchar])    #输出width个字符，左对齐，不足部分用fillchar填充，默认为空格
    s.rjust(width[,fillchar])    #右对齐，同上
    s.center(width[,fllchar])    #中间对齐，同上
    s.zfill(width)               #把s变为width长，不足部分0不足

    s.find(substr[,start[,end]])  #返回s中substr第一次出现的索引，若s中没有substr则返回-1
    s.index(substr[,start[,end]])   #与find相同，只是若s中若没有substr怎么返回一个错误
    s.rfind(substr[,start[,end]])    #从右边开始找，返回第一个，若无则返回-1
    s.rindex(substr[,start[,end]])   #同上
    s.count(substr[,start[,end]])   #返回s中substr的个数
    s.replace(old,new[,count])   #替换，count为替换次数
    s.strip([char])   #把s首尾空格符去掉，若char不为空，则把s中的char去掉
    s.rstrip([char])   #同上
    s.lstrip([char])   #同上
    s.expandtabs([tabsize])  #把s中一个tab字符替换为tabsize个空格字符

    s.split([sep[,maxlist]])  #以sep为分隔符切割s并返回一个list，maxlist表示分割次数，默认sep为空白字符
    s.rsplit([sep[,maxlist]])  #同上
    sep.join(sequence)  #把sequence用sep字符连接起来
    s.maketrans(from,to)  #返回一个256个字符组成的翻译表，其中from中的字符被一一对应的转换为to中的字符，故from须与to等长
    s.tanslate(table[,deletechars]) 
    #字符串中的一些判断函数
    s.startswith(str[,start[,end]])   #判断s是否以str开头
    s.endwith(str[,start[,end]])   #同上
    s.isalnum()   #是否全为数字或者字母
    s.isalpha(), s.isdigit(),s.isspace(), s.islower(), s.isupper(), s.istitle()(是否首字母大写)

### list

    list.append()  #把一个元素添加到列表的结尾
    list.extend()  #将一个给定列表中的所有元素都添加到另一个列表中
    list.insert(i,x)   #在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前,而 a.insert(len(a), x) 相当于 a.append(x)
    list.remove(x)  #删除列表中值为 *x* 的第一个元素。如果没有这样的元素，就会返回一个错误
    list.pop([i])  #从列表的指定位置删除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素
    list.clear()  #从列表中删除所有元素,相当于 del a[:]
    list.index(x)  #返回列表中第一个值为 *x* 的元素的索引,如果没有匹配的元素就会返回一个错误
    list.count(x)  #统计x出现的次数
    list.sort()  #对列表中的元素就地进行排序,改变原列表
    list.reverse()  #就地倒排列表中的元素,改变原序列
    list.copy()  #返回列表的一个浅拷贝,等同于 a[:]

### Chinese Zodiacs (example of string operation)

chinese_zodiacs = '猴鸡狗猪鼠牛虎兔龙蛇马羊‘
this_year = 2019;
print(chinese_zodiacs[this_year % 12]);






