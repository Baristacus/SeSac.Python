s = " Hello W  orld   "
s2 = "apple, banana,cheery"
l = "hello"
u = "HELLO"
print(s)
print(s.lower())
print(s.upper())
print(s.capitalize())

print(type(s))


print(s.strip())  # 앞 뒤의 공백만 제거
print(s2.split(","))


s2_list = s2.split(",")
s2_list2 = []


# list coprehension

s3_list = [fruit.strip() for fruit in s2.split(",")]
print(s3_list)
