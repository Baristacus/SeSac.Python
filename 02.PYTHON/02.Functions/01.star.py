"""아래 내용을 출력 하는 코드
*
**
***
****
*****
"""

# for star in range(5):
#     print("*")

# for i in range(1, 6):
#     print("*" * i)

# row = input("원하는 높이는?: ")
# for i in range(1, int(row) + 1):
#     print("*" * i)


"""아래 내용을 출력 하는 코드
    *
   **
  ***
 ****
*****
"""

# for i in range(1, 6):
#     print(" " * (), "*" * i)


"""아래 내용을 출력 하는 코드
    *
   ***
  *****
 *******
"""

# for i in range(1, 10, 2):
#     print(i * "*")


"""아래 내용을 출력 하는 코드
    *
   ***
  *****
 *******
  *****
   ***
    *
"""


n = 8  # 행의 수

for i in range(n):
    # 공백 출력
    for j in range(n - i - 1):
        print("", end=" ")

    # 별표 출력
    for j in range(i + 1):
        print(" ", end=" * ")

    print()  # 줄바꿈
