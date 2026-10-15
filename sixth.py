print("=== while 循环 ===")
计数 = 1
while 计数 <=5:
 print("while:" + str(计数))
 计数 = 计数 + 1

print("")

print("=== for 循环 ===")
for 数字 in range(1,6):
 print("for:" + str(数字))

print("")
 
print("=== for 循环（列表）===")
水果 = ["苹果","香蕉","橙子"]
for 水果名 in 水果:
 print("我喜欢:" + 水果名)

print("")

print("=== 嵌套循环 ===")
for i in range(1,4):
 for j in range(1,4):
  print(str(i) + " x " + str(j) + " = " + str(i * j))
 print("")
