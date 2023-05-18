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

# 使用闭包实现ATM小案例

