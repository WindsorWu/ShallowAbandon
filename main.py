import random
import time

# 获取用户输入的时间（毫秒）
c = int(input("你有多少时间（ms）？："))

while True:
    # 生成一个 0 到 c 之间的随机整数
    b = random.randint(0, c)
    # 提示用户输入问题
    a = input("向DeepSeek提问吧: ")
    # 检查是否输入了退出指令
    if a == "exit":
        break
    print("思考中", end="", flush=True)
    # 程序暂停 b 毫秒
    time.sleep(b / 1000)
    print("\n服务器繁忙，请稍后重试。")
