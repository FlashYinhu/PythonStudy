# input中的提示信息就相当于在前面提前打印了一个提示信息
# input语句将写入的数据当作字符串处理
name = input("Please tell me your name:\n")
print("Please confirm your name,you are %s, right?" % name)
age = input("if your name is correct, please tell me your age\n")
print("input输入的类型为:", type(age))
age = int(age)
print(f"Ok,Welcome!{name},{age}.", type(name), type(age))