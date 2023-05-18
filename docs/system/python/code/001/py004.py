# 函数作为参数传递


#标记1
def test_func(compute):
    result = compute(1,2)
    print(result)

def compute(x,y):
    return x + y

test_func(compute)




"""
函数compute 作为参数，传入了 test_func 函数中使用
test_func 需要一个函数作为参数传入，这个函数需要接收两个数字进行计算，计算逻辑由这个被传入函数决定
compute 函数接收两个数字对其进行计算，compute 函数作为参数，传递给了 test_func 函数使用
最终，在test_func 函数内部，由传入的compute 函数，完成了对数字的计算

所以这是一种，计算逻辑的传递，而非数据的传递

就像上述代码那样，不仅仅是相加，相减，相除等任何逻辑都可以自定定义并作为函数传入

"""

# 标记2
def add(x,y):
    return x+y

# 标记1 的函数是数据确定(1,2)确定，但逻辑不确定
# 标记2 的函数是 逻辑确定，但数据不确定
# lambda 函数


"""
def 关键字，可以定义带有名称的函数 可重复使用
lanmbda 关键字，可以定义匿名函数（五名称） 只是用一次

匿名函数定义语法

lambda 传入参数：函数体(一行代码)

lambda 是关键字，表示定义匿名函数
传入参数表示匿名函数的形式参数 如 x,y 表示接口收两个形式参数
函数体就是函数的执行逻辑，要注意：智能写一行，无法多写代码



"""

def test_func(compute):
    result = compute(1,2)
    print(result)
test_func(lambda x,y : x+y)

print("其他模块如果调用不当，我也会输出，见py007.py")

if __name__ == '__main__':
    print("我只会在我这个文件运行的时候打印，其他文件引入我这个模块是不会运行的。见PY007.PY")

