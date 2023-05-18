# 异常捕获

try:
    f= open("d:/abc.txt", "r", encoding="UTF-8")
except NameError as nameError:
    # 捕获单个异常
    print(nameError)
except (EOFError,TimeoutError) as multiError:
    # 捕获多个异常
    print("multiError")
except Exception as e:
    # 捕获所有异常
    print(e)
except:
    print("捕获所有异常，不需要异常信息")
else:
    print("如果没有出现异常我就会打印，并且else 是非必要写的。")
finally:
    f.close();
    print("无论是有没有出现异常，我百分百会打印，但finally 是非必要写的")



