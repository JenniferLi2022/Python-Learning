print("=== 基本操作 ===")
学生 = ["小明","小红","小李"]
print("列表：" + str(学生))
print("第一个学生：" + 学生[0])
print("列表长度：" + str(len(学生)))

print("")

print("=== 添加元素 ===")
学生.append("小王")
print("添加后：" + str(学生))

学生.insert(1,"小张")
print("在索引 1 插入：" + str(学生))

print("")

print("=== 修改元素 ===")
学生[0] = "大明"
print("修改后：" + str(学生))

print("")

print("=== 删除元素 ===")
del 学生[2]
print("删除索引 2 后：" + str(学生))

学生.remove("小王")
print("删除小王后：" + str(学生))

print("")

print("=== 遍历列表 ===")
for 名字 in 学生:
    print("学生：" + 名字)

print("")

print("=== 列表切片 ===")
数字 = [1,2,3,4,5,6,7,8,9,10]
print("愿列表：" + str(数字))
print("前 3 个：" + str(数字[0:3]))
print("第 3 到 6 个：" + str(数字[2:6]))
print("最后 3 个：" + str(数字[-3:]))
