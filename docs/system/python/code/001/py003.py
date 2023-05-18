# 位置参数
def test(a,b):
    print(a)
    print(b)

test("a",2)

def test(a,b):
    print(f"多个相同名字函数{a+b}")

test(3,3)


# 关键字参数
def test(c,d):
    print(c)
    print(d)
test(c=5,d=6)

# 缺省参数 (默认值)
# 定义函数的时候给默认值
def user_info(name,age,sex="男"):
    print(name,age,sex)

user_info(name="小明",age=18)
user_info(name="小红",age=18 ,sex='女')


# 不定参数：补丁长参数也叫可变参数。用于不确定调用的时候会传递多少各参数

# 不定参数 -位置不定长 * 号 即位置传递

def user_info(*args):
    # args :元组
    print(args)
user_info("a",23,2432,"bb","cc")

# 不定长  --关键字不定长  ** 号  即关键字传递

def user_info(**kwargs):
    # kwargs : 字典
    print(f"我是关键字不定长：{kwargs}")

#{'name':'tome','age':18,'id':55}
user_info(name='tone',age= 18,id = 55)

# 终极函数
def user_info(*args,**kwargs):
    print(f"元组{args}")
    print(f"字典{kwargs}")

user_info('2222',432,432, age ="2" ,sex="4")





