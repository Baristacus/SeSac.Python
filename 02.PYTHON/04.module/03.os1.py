import os

current_dir = os.getcwd()
print(current_dir)

new_dir = "폴더 만들기"
# os.mkdir(new_dir)

# os.rmdir(new_dir)  # 폴더 삭제


my_path = os.getenv("PATH")

my_dir = os.system("dir")
