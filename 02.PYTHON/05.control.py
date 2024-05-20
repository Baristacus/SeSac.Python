# 반복문
# while
print("while")
count = 0
while count < 5:  # 이 조건이 True인 동안 반복
    print(count)
    count = count + 1

# for
print("for")
for i in range(10):  # 특정 범위내에서 반복
    print(i)


users = ["park", "lee", "kim"]
for user in users:
    print(user)


for i in range(1, 8):
    print(i)

for i in range(1, 10, 2):
    print(i)

# --------------------------------------------------

# 조건문
# if
x = 10
if x < 10:
    print("x가 10보다 작음")
else:
    print("x가 10보다 큼")


score = 70
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(grade)
print("Score: {}, Grade: {}".format(score, grade))
print(f"니 점수는 {score}, 학점은 {grade}!")


math = 90
eng = 80

if math >= 90 and eng >= 90:
    print("졸업가능!")
else:
    print("졸업불가!")


if math >= 90 or eng >= 90:
    print("졸업가능!")
else:
    print("졸업불가!")
