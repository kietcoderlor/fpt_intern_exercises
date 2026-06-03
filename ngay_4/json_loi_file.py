#bắt lỗi khi file json ko tồn tại
import json
try:
    with open("students.json", "r", encoding="utf-8") as f: 
        data: list[dict[str, str | int | list[str]]] = json.load(f)
    print(data)
except FileNotFoundError:
    print("file students.json bạn tìm không tồn tại")