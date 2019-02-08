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


### if elif(else if)


    if condition_is_true:
        do something

    if expression:
      do sommething
    elif expression:
      do something
    else:
      do something

user_input = input('input a number': )

**type(user_input) == 'str'**


### for, while loop

    while expression:
      do something

as long as expression is true, execute continue

    for num in nums:
      print(num)

 iterate all the elements


    for year in (2000, 2019):
      print(%s 'year is %s year' %(year, chinese_zodiacs(year % 12)))

    for i in range(10):
      print(i)
    
    alist = []

    for i in range(10):
      if(i % 2 == 0):
        alist.append(i*i)
    
    blist =[ i*i for i in range(10) if i % 2 == 0]



### dictionary

    {'hashValue': object}

    stat = {}
    for i in range(10):
      stat[i] = 0
    
    stat = { i: 0 for i in range(10)}

## File handling

### open

    open()  open takes two parameters; filename, and mode.
> "r" - Read - Default value. Opens a file for reading, error if the file does not exist

> "a" - Append - Opens a file for appending, creates the file if it does not exist

> "w" - Write - Opens a file for writing, creates the file if it does not exist

> "x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

> "t" - Text - Default value. Text mode
> "b" - Binary - Binary mode (e.g. images)

    f = open("demofile.txt") == f = open("demofile.txt", "rt")

> The open() function returns a file object, which has a read() method for reading the content of the file:
    f = open("demofile.txt", "r")
    print(f.read())
>By default the read() method returns the whole text, but you can also specify how many character you want to return:

### read readline() readlines()

#### Return the 5 first characters of the file:
    f = open("demofile.txt", "r")
    print(f.read(5))
     f.close()
#### You can return one line by using the readline() method:

Read one line of the file:

    f = open("demofile.txt", "r")
    print(f.readline())
     f.close()
Loop through the file line by line:

    f = open("demofile.txt")
    for line in f.readlines():
      print(line)
     f.close()
### write

To write to an existing file, you must add a parameter to the open() function:

> "a" - Append - will append to the end of the file

> "w" - Write - will overwrite any existing content

Open the file "demofile.txt" and append content to the file:

    f = open("demofile.txt", "a")
    f.write("Now the file has one more line!")
     f.close()
Open the file "demofile.txt" and overwrite the content:

    f = open("demofile.txt", "w")
    f.write("Woops! I have deleted the content!")
    f.close()
### Create a New File
To create a new file in Python, use the open() method, with one of the following parameters:

> "x" - Create - will create a file, returns an error if the file exist

> "a" - Append - will create a file if the specified file does not exist

> "w" - Write - will create a file if the specified file does not exist

### delete file

> To delete a file, you must import the OS module, and run its os.remove() function:

    import os
    os.remove("demofile.txt")

### Check if File exist:
> To avoid getting an error, you might want to check if the file exist before you try to delete it:

    import os
    if os.path.exists("demofile.txt"):
      os.remove("demofile.txt")
    else:
      print("The file does not exist")

### Delete Folder
To delete an entire folder, use the os.rmdir() method:

    import os
    os.rmdir("myfolder")

### seek(offset, from_what) 

from_what: 0 beginning,  1 current position, 2 tail

when open a file, pointer is in the beginning


### close()

always close the file after operation

## Try Except

    try:
      # monitor
    except Exception[, reason]:
      # handle
    finally:
      # do something
### SyntaxError SameError IndexError KeyError ValueError AtrtributeError ZeroDivisionError ....

    try: 
      a = '123'
      a.append('4')
    except AttributeError:
      print('Can not append to str object')
  
      try: 
        print(1/0)
      except ZeroDivisionError as e:
        print('0 can no be divided %s' %e)

### Exception

    try: 
      print(1/0)
    except Exception as e:
      print(e))
### customize Error

    try: 
      raise NameError('helloError')
    except Exception as e:
      print(e))
### finally

    try:
      f = open('noexist.txt')
    except Exception as e:
      print(e)
    finally:
      f.close()

## function

    def my_func(name = 'John'):
      # do something
    
    my_func('Jen')
    my_func()

### Python Lambda
> lambda arguments : expression

    x = lambda a : a + 10
    print(x(5)) # 15

    x = lambda a, b : a * b
    print(x(5, 6)) # 30

### keywords argument

    def foo(*positional, **keywords):
        print "Positional:", positional
        print "Keywords:", keywords

> The *positional argument will store all of the positional arguments passed to foo(), with no limit to how many you can provide:

    >>> foo('one', 'two', 'three')
    Positional: ('one', 'two', 'three')
    Keywords: {}

> The **keywords argument will store any keyword arguments:

    >>> foo(a='one', b='two', c='three')
    Positional: ()
    Keywords: {'a': 'one', 'c': 'three', 'b': 'two'}

> And of course, you can use both at the same time:

    >>> foo('one','two',c='three',d='four')
    Positional: ('one', 'two')
    Keywords: {'c': 'three', 'd': 'four'}
  
    def func(a,b, c):
      print('a'= %s' %a)
      print('b'= %s' %b)
      print('c'= %s' %c)

    func(1,2,3)
    a = 1
    b = 2
    c = 3

    func(1, c = 3, b =2)
    a = 1
    b = 2
    c = 3

### changeable
    def func(a, *others): # at least pass one argument
     return len(1 + len(ohters))
    
    func(1,2,3,4) ## return 4


### scope

    a = 123
    def func():
      a = 456
      print(a) # 456
    print(a) # 123

> if define a global variable inside a function
    a = 123
    def func():
      global a
      a = 456
      print(a) # 456
    print(a) # 456

## Iterator

    mytuple = ("apple", "banana", "cherry")
    myit = iter(mytuple)

    print(next(myit)) # 'apple'
    print(next(myit)) # 'banana'
    print(next(myit)) # 'cherry'

    mytuple = ("apple", "banana", "cherry")

    for x in mytuple:
      print(x) 
    'apple'
    'banana'
    'cherry'

    mystr = "apple"

    for x in mystr:
      print(x)

    'a'
    'p'
    'p'
    'l'
    'e'
### creat a iterator

    def frange(start, stop, step):
      x = start
      while(x < stop):
        yield x
        x += step
    for i in frange(10, 12, 0.5):
      print(x)
    
    10 / 10.5 /11 /11.5


## build-in function

### filter
    a = [1,2,3]
    list(filter(lambda x: x >= 3, a))
    # [3]

### map
     
    list(map(lambda x: x * 2, a))
    # [2,4,6]
### reduce
    reduce(lambda a, b:a +b, a)
    # 6
### zip
    dict(zip((1,2,3), (4,5,6)))
    # {1: 4, 2: 5, 3: 6}

    dic = {'a':1,'b':2,'c':3}
    dict(zip(dic.values(), dic.keys()))
    # {1: 'a', 2: 'b', 3: 'c'} # swap key-value pair

## closure

    def counter(start):
      count = [start]
      def add():
        count[0] += 1
        return count[0]
      return add
      
    sum = counter(5)

    print(sum()) #6
    print(sum()) #7

    def a_Line(a,b):
      return lambda x: a*x + b

    b = a_Line(2,0)
    print(b(2)) # 4

### Decorators

**without paramethers**
    def outer(func):
      def inner(a, b):
        print('started')
        func(a, b)
        print('stop')
      return inner

    @outer
    def add(a, b):
      print(a + b)

    @outer
    def sub(a, b):
      print(a - b)
    
    add(3,4)
    sub(8,1)

**with paramethers**
    def outer_outer(argv):
      def outer(func):
        def inner(a, b):
          print('started %s %s' %(argv, func.__name__))
          func(a, b)
          print('stop')
        return inner
      return outer

    @outer_outer('add_module')
    def add(a, b):
      print(a + b)

    @outer_outer('sub_module')
    def sub(a, b):
      print(a - b)

    add(4 ,5)
    sub(7, 1)
  
### “with” statement 

> The with statement creates a context manager and it will automatically close the file handler

We can also use with statement to open more than one file.

    with open(in_filename) as in_file, open(out_filename, 'w') as out_file:
      for line in in_file:
        ...
        ... 
        out_file.write(parsed_line)

### module

import module_name

    import os
    import time
    ...
    import module_name as new_name
    from time import sleep # not recommend
    sleep() ## use directly

**how define a module**

define func inside file_name.py 
import file_name in new file
call file_name.func()



## Class

    class Player(): ## define a class 
      def __init__(self, name, hp, accu): ## initialize a new instance
        self.__name = name # attribute # keep attribute private by adding '__'
        self.hp = hp
        self.accu = accu # add new attribute
      def print_role(self): ## inside func must have a self as the first parameter
        print('%s: %s' %(self.name, self.hp))

      def updateName(self, newName):
        self.name = newName

    class Monster():
      'defination of a monster'
      def __init__(self, hp=100):
        self.hp = hp 
      def run(self):
        print('run to somewhere')
      def whoami(self):
        print('I am a monster')

    class Animals(Monster):
      def __init__(self, hp =10): # inheritance
        super().__init__(hp)


    class Boss(Monster):
      def whoami(self): # override whoami method
        print('I am a boss')


    user1 = Player('tom', 100, 'soldier')
    user2 = Player('Jon', 99, 'master')

    user1.print_role()
    user2.print_role()


    m1 = Monster(100)
    print(m1.hp)


    m2 = Animals(1000)
    print(m2.hp)
    # print(m2.run())
    m2.whoami()

    m3 = Boss(9)
    print(m3.hp)
    m3.run()
    m3.whoami()
    m3.hp = 1
    print(m3.hp)

### with statement and class

    class with1():
      def __enter__(self):
        print('run')
      def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
          print('exit normally')
        else:
          print('An error %s' %exc_tb)

    with with1():
      print('tst is runing')
      raise NameError('testNameError')
  
###  Concurrency/ Threads
    // function
    import threading
    import time
    from threading import current_thread

    def my_thread(arg1, arg2):
      print(current_thread().getName(), 'start')
      print('%s %s' %(arg1, arg2))
      time.sleep(1)
      print(current_thread().getName(), 'stop')


    for i in range(1,6):
      t1 = threading.Thread(target=my_thread, args=(i, i + 1))
      t1.start()
    print(current_thread().getName(), 'end')

    // oop
    import threading
    from threading import current_thread


    class my_thread(threading.Thread):
      def run(self):
        print(current_thread().getName(), 'start')
        print('run')
        print(current_thread().getName(), 'stop')


    for i in range(10):
      t1 = my_thread()
      t1.run()
      t1.join()

    print(current_thread().getName(), 'end')

    > strat() Start the thread’s activity.
    It must be called at most once per thread object. It arranges for the object’s run() method to be invoked in a separate thread of control.


    > run() representing the thread’s activity.
  
  More(https://docs.python.org/3.7/library/threading.html)

  