account_amout = 0 # 账户余额

def atm(num,deposit=True):
    global  account_amout
    if deposit:
        account_amout+=num
        print(f"存款+{num},账户余额:{account_amout}")
    else:
        account_amout-=num
        print(f"取款:-{num},账户余额:{account_amout}")


# 简单闭包

def outer(logo):  # logo 外部变量不会被外界所修改,只会被该方法才使用
    def inner(msg):  # 内部函数,依赖外部变量
        print(f"{logo}>{msg}<{logo}")
    return inner

fn1=outer("test")  # fn1 是一个函数 ,return 返回的函数.
fn1("大家好1")
fn1("大家好2")


"""
test>大家好1<test
test>大家好2<test
"""
# 使用nonlocal 关键字修改外部函数的值


def outer(num1):
    print(f"ss{num1}",num1)
    def inner(num2):
        nonlocal  num1
        num1 += num2
        print(num1)
    return inner;

fn=  outer(10)
fn(10)
fn(10)




# 使用闭包实现ATM小案例

# 不需要全局的外部变量


# 优点:
# 无需定义全局变量即可实现通过函数,持续的访问,修改某个值
#闭包使用的变量所在于函数内,难以被错误的调用修改

#缺点:
#由于内部函数持续引用外部函数的值,所以会导致这一部分内存空间不被释放,一直被占用
def account_create(initial_amount=0):
    def atm (num,deposit=True):
        nonlocal  initial_amount
        if deposit:
            initial_amount += num
            print(f"存款{num},账号余额{initial_amount}")
        else:
            initial_amount -=num
            print(f"取款{num},账号余额{initial_amount}")

    return atm

atm= account_create()
atm(10,True)
atm(20,False)

