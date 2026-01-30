import mediapipe as mp
import os

try:
    print("--- KẾT QUẢ ĐIỀU TRA ---")
    # In ra đường dẫn của file mediapipe mà Python đang dùng
    print(f"Đường dẫn file: {mp.__file__}")
    
    # Kiểm tra xem nó có nằm trong site-packages (nơi cài thư viện chuẩn) không
    if "site-packages" in mp.__file__:
        print("✅ Đường dẫn: Hợp lệ (Nằm trong thư viện cài đặt).")
    else:
        print("❌ Đường dẫn: BẤT THƯỜNG (Đây chính là kẻ mạo danh!)")
        
    # Kiểm tra thuộc tính solutions
    print(f"Kiểm tra solutions: {mp.solutions}")

except AttributeError:
    print("\n❌ LỖI: Module này không có 'solutions'.")
    print("👉 KẾT LUẬN: Bạn đang import nhầm file hoặc thư mục khác, hoặc bản cài đặt bị hỏng.")
except Exception as e:
    print(f"Lỗi khác: {e}")