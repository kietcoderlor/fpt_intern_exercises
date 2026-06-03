#xây class student và course với phương thức hợp lý
class Course:
    def __init__(self, ten: str, tin_chi: int) -> None:
        self.ten = ten
        self.tin_chi = tin_chi

    def show(self) -> None:
        print(f"{self.ten} - {self.tin_chi} tín chỉ")


class Student:
    def __init__(self, ten: str, tuoi: int) -> None:
        self.ten = ten
        self.tuoi = tuoi
        self.mon_hoc: list[Course] = []

    def dang_ky(self, course: Course) -> None:
        self.mon_hoc.append(course)

    def show(self) -> None:
        print(f"{self.ten}, {self.tuoi} tuổi")
        for mon in self.mon_hoc:
            mon.show()

#note: luôn nhớ sử dụng type hints
