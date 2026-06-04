import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

API_URL = "https://provinces.open-api.vn/api/?depth=1"


def goi_api(url: str) -> list[dict[str, str | int]]:
    try:
        with urlopen(url, timeout=10) as resp:
            data = json.load(resp)
        if not isinstance(data, list):
            raise ValueError("Dữ liệu API không đúng định dạng")
        return data
    except HTTPError as e:
        print(f"Lỗi HTTP khi gọi API: {e.code} {e.reason}")
        return []
    except URLError as e:
        print(f"Không kết nối được API (kiểm tra mạng): {e.reason}")
        return []
    except json.JSONDecodeError:
        print("API trả về không phải JSON hợp lệ")
        return []
    except TimeoutError:
        print("Gọi API quá thời gian chờ")
        return []
    except ValueError as e:
        print(e)
        return []

def hien_thi_danh_sach(tinh_thanh: list[dict[str, str | int]]) -> None:
    print(f"\n{'Mã':<6} {'Tên tỉnh/thành':<30} {'Loại'}")
    print("-" * 50)
    for item in tinh_thanh:
        ma = item.get("code", "")
        ten = item.get("name", "")
        loai = item.get("division_type", "")
        print(f"{ma:<6} {ten:<30} {loai}")


def tim_theo_ten( tinh_thanh: list[dict[str, str | int]], tu_khoa: str,) -> list[dict[str, str | int]]:
    tu_khoa = tu_khoa.strip().lower()
    if not tu_khoa:
        return []
    ket_qua: list[dict[str, str | int]] = []
    for item in tinh_thanh:
        ten = str(item.get("name", "")).lower()
        if tu_khoa in ten:
            ket_qua.append(item)
    return ket_qua


def main() -> None:
    print("=== Tra cứu tỉnh/thành Việt Nam")
    tinh_thanh = goi_api(API_URL)
    if not tinh_thanh:
        print("Không có dữ liệu để hiển thị.")
        return

    print(f"Đã tải {len(tinh_thanh)} tỉnh/thành.\n")
    print("1. Xem toàn bộ danh sách")
    print("2. Tìm theo tên")
    opt = input("Chọn (1 hoặc 2): ").strip()

    if opt == "1":
        hien_thi_danh_sach(tinh_thanh)
    elif opt == "2":
        tu_khoa = input("Nhập tên cần tìm (vd: Hà Nội, Đà Nẵng): ")
        ket_qua = tim_theo_ten(tinh_thanh, tu_khoa)
        if not ket_qua:
            print(f"Không tìm thấy tỉnh/thành nào chứa '{tu_khoa}'")
        else:
            print(f"\nTìm thấy {len(ket_qua)} kết quả:")
            hien_thi_danh_sach(ket_qua)
    else:
        print("Lựa chọn không hợp lệ")


if __name__ == "__main__":
    main()
