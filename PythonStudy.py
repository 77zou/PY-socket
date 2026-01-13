#1. 打印一个Hello程序
print('Hello,PyCharm')

#2. 列表List（可以增删改查）
fruits = ['apple', 'banana', 'orange']
print(fruits)
# 查询列表元素
print(fruits[0])
# 输出‘apple','banana',因为list[a,b]是左闭右开！
print(fruits[1:2])
# 增加/删除列表元素
fruits.append('mango')
fruits.remove('mango')
# 修改列表元素
fruits[0] = '桃子'
print(fruits[0])

#3. 注释快捷键：ctrl + / = "#"

#4. 元组Tuple（不可以增删改）
vegetables = ('tomato','potato','onion')
print(vegetables)

#5. for循环
num = [1,2,3,4,5,6,7,8,9,10]
total = 0
for n in num :
    total += n
    print('循环后,' , total)
for f in fruits:
    print(f)
for r in range(10):
    print(r)
    print(r**2)

#6. if语句
age = 15
if age < 18:
    print('未成年')
elif age < 65:
    print('中年人')
else :
    print('老年人')

#7. 创建类,数据结构字典（键值对）
class Student:
    def __init__(self,name,student_ID):
        self.name = name
        self.student_ID = student_ID
        self.grades = {'语文': 0, '数学' : 0, '英语' : 0}
    def changeGrade(self,course,new_grade):
        if course in self.grades:
            self.grades[course] = new_grade
    def Print(self):
        print(f"学生 {self.name} (学号为:{self.student_ID}) 的成绩为:")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}分")
s1 = Student("小明",1)
s1.changeGrade("语文",100)
print(s1.name)
print(s1.grades)
s1.Print()

#8. ***学会读文件——三种方法
f = open("./file.txt","r",encoding="utf-8")
read1 = f.read()
print(read1)
   # f.seek(0)是重置指针的意思，因为每读一次都会向后移一位！
f.seek(0)
read2 = f.readline()
print(read2)
f.close()

with open("./file.txt",encoding="utf-8") as f:
    read3 = f.readlines()
    for l in read3:
        print(l)

#9. 写入文件
with open("./poem.txt","w",encoding="utf-8") as f:
    f.write("我欲乘风归去，\n又恐琼楼玉宇，\n高处不胜寒。\n")

with open("poem.txt","a",encoding="utf-8") as f:
    f.write("起舞弄清影,\n何似在人间。\n")

#10. 异常捕捉
try:
    user_weight = float(input("请输入你的体重（单位：Kg）："))
    user_height = float(input("请输入你的身高（单位：cm）："))
except ValueError:
    print("请输入合理数字！")
except ZeroDivisionError:
    print("请输入不为零的身高！")
except:
    print("发生未知错误，请重新运行！")
else:
    print("您的BMI值为：。。。")
finally:
    print('程序结束运行')