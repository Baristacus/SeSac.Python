# list comprehension 리스트 컴프리헨션

# []
# [표현식 for 항목 in 반복 (조건문)]
# [변수 for 항목 in 반목(조건문)]


# 1부터 10까지의 숫자를 담는 리스트 생성

nums = [num for num in range(1, 11)]

print(nums)


# 위 리스트의 각 숫자의 제곱

squares = [x**2 for x in range(1, 11)]

print(squares)


# 1부터 20까지 짝수 리스트
even_nums = [x for x in range(2, 21, 2)]
even_nums2 = [x for x in range(1, 21) if x % 2 == 0]

print(even_nums)
print(even_nums2)


# 1부터 20까지 홀수 리스트
odd_nums = [x for x in range(1, 21, 2)]
odd_nums2 = [x for x in range(1, 21) if x % 2 == 1]

print(odd_nums)
print(odd_nums2)


# 문자열의 각 글자를 대문자로 바꾼 리스트
word = "hello"

upper_letters = "".join([x.upper() for x in word])

print(upper_letters)
