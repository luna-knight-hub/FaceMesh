import mediapipe as mp
import os

print("--- THÔNG TIN MODULE ---")
try:
    print(f"1. Đường dẫn file: {mp.__file__}")
except AttributeError:
    print("1. Đường dẫn file: (Không xác định - Module này không có file nguồn!)")

print("\n--- DANH SÁCH CÁC THUỘC TÍNH BÊN TRONG ---")
# Lấy tất cả thuộc tính
all_attributes = dir(mp)

# Lọc bỏ các thuộc tính hệ thống (bắt đầu bằng __) để dễ nhìn
public_attributes = [a for a in all_attributes if not a.startswith("__")]

if public_attributes:
    for attr in public_attributes:
        print(f"  - {attr}")
else:
    print("  (Rỗng) Không tìm thấy thuộc tính công khai nào!")

print("\n--- PHÂN TÍCH ---")
if "solutions" in all_attributes:
    print("✅ CÓ 'solutions': Thư viện cài đặt chuẩn.")
else:
    print("❌ KHÔNG CÓ 'solutions': Đây là nguyên nhân gây lỗi!")
    if "cv2" in all_attributes or "cap" in all_attributes:
        print("👉 CẢNH BÁO: Có vẻ bạn đang import nhầm file code của chính bạn (Shadowing).")