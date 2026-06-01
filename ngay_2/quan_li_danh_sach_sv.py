sv = {"name": "An", "age": 20}
print(sv["name"])     # An
sv["age"] = 21        # cập nhật
sv["email"] = "a@x"  # thêm key
 
for k, v in sv.items():
    print(k, v)
 
tags = {1, 2, 2, 3}   # set -> {1,2,3}
print(tags)
# dùng dict vì dict có dạng kiểu key-value ánh xạ, phù hợp cho việc matching và quản lí dữ liệu hơn là khi dùng list.
