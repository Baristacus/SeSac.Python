# 문자열의 글자 수 세기
words = ["apple", "banana", "cherry", "dragonfruit"]
words_lengths = [len(x) for x in words]
print(words_lengths)
# 출력: [5, 6, 6, 11]


# 문자열 리스트에서 길이가 3 이하인 단어들만 선택하기
words = ["apple", "banana", "cherry", "dragonfruit", "egg"]
short_words = [x for x in words if len(x) <= 3]
print(short_words)
# 출력: ["egg"]


# 중첩 리스트 펼치기
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [x for y in nested_list for x in y]
print(flattened_list)
# 출력: [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 특정 조건(5보다 큰것)을 만족하는 요소 필터링
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
greater_than_five = [x for x in numbers if x > 5]
print(greater_than_five)
# 출력: [6, 7, 8, 9, 10]


# 문자열 리스트에서 첫 글자가 모음인 단어들 선택하기
words = ["apple", "banana", "cherry", "apricot", "egg"]
vowel_starting_words = [x for x in words if x.startswith(("a", "e", "i", "o", "u"))]
print(vowel_starting_words)
# 출력: ["apple", "apricot", "egg"]
