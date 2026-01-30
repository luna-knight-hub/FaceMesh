import cv2
from cvzone.FaceMeshModule import FaceMeshDetector

def main():
    # 1. Mở Camera
    cap = cv2.VideoCapture(0)
    
    # 2. Khởi tạo bộ phát hiện (Dòng 11 chuẩn)
    # Lưu ý: Chỉ dùng tham số maxFaces cho đơn giản lúc đầu
    detector = FaceMeshDetector(maxFaces=1)

    print("Đang chạy cvzone... Nhấn 'q' để thoát.")

    while True:
        success, img = cap.read()
        
        # Kiểm tra nếu không đọc được camera thì bỏ qua vòng lặp này
        if not success:
            continue

        # 3. Tìm và vẽ khung xương
        # Hàm này trả về 2 giá trị: hình ảnh đã vẽ và danh sách các khuôn mặt
        img, faces = detector.findFaceMesh(img, draw=True)

        # Hiển thị
        cv2.imshow("Image", cv2.flip(img, 1))
        
        # Nhấn 'q' để thoát
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()