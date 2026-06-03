# lưu list object ra file json rồi đọc lại và in ra (sử dụng serialize, deserialize)

import json

students: list[dict[str, str | int | list[str]]] = [
    {"ten": "Nguyễn Văn A", "tuoi": 20, "mon": ["Python", "OOP"]},
    {"ten": "Nguyễn Văn B", "tuoi": 21, "mon": ["Python"]},
]

# serialize
with open("students.json", "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=2)

# deserialize
with open("students.json", "r", encoding="utf-8") as f:
    data: list[dict[str, str | int | list[str]]] = json.load(f)

for sv in data:
    print(sv)
