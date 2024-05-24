"""
try
실행하려는 명령

except
실행하려는 명령에 오류가 발생했을때

else(option)
실행하려는 명령이 성공했을때

finally(option)
실행하려는 명령의 성공여부와 상관없이 실행
"""

# ---------------------------------------------

try:
    with open("file.txt", "r") as file:
        contents = file.read()

    print(contents)
except FileNotFoundError:
    print("No File")
except PermissionError:
    print("No Permission")
