# 일반 문자열 출력
print("Hello")

# f-문자열(f-string)
name = input()
print(f"Hello {name}")

# 문자열 포멧팅 {} 를 치환, {0} 순번 부여 가능
print("Hello, {}".format(name))

# 문자열 연결, 문자열 끝에는 기본으로 \n 이 있음
print("Hello", end=" ")
print("World")

# %연산자, %s는 문자열(string), %d는 숫자(decimal)
print("Hello %s" % name)
