print("=== 简单嵌套 ===")
for i in range(1,4):
    print("外层 i = " + str(i))
    for j in range(1,4):
         print(" 内层 j = " + str(j))

print("")
print("=== 九九乘法表 ===")
for i in range(1,10):
    for j in range(1,10):
         print(str(i) + " x " + str(j) + " = " + str(i*j).ljust(3), end="")
    print("")

print("")
print("=== 打印星星 ===")
for i in range(1,5):
    for j in range(1,i+1):
         print("*",end="")
    print("")
