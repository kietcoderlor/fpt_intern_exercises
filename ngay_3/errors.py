def chia(a: int, b: int) -> float:
    try:
        return a / b
    except ZeroDivisionError: #xử lí chia cho 0
        print("Không thể chia cho 0") 
        return None
    except TypeError: #xử lí khi người dùng nhập sai kiểu dữ liệu
        print("Không thể chia cho chuỗi")
        return None
 
print(chia(10, 2))  
print(chia(10, 0))   