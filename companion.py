import json
import os

DATA_FILE = "memory.json"

# 启动时加载历史：文件存在就读，不存在返回空列表
def load_history():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# 把对话写进 json
def save_history(history):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

print("你好呀，我是你的小伴侣，输入 exit 就能退出")

history = load_history()
print(f"已加载 {len(history)} 条历史对话")

while True:
    user_input = input("你：")
    if user_input == "exit":
        print("伴侣：再见，下次再聊")
        break

    history.append({"role": "user", "content": user_input})

    reply = f"你说的是「{user_input}」，我收到啦"
    print(f"伴侣：{reply}")

    history.append({"role": "companion", "content": reply})

    save_history(history)   # 每轮保存，实时持久化

print("对话已保存，下次打开还能看到")
