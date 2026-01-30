import cv2
import os

def main():
    # 1. Lấy đường dẫn file mô hình có sẵn trong thư viện cv2
    face_cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(face_cascade_path)

    cap = cv2.VideoCapture(0)
    print("Đang chạy chế độ Haar Cascade (OpenCV thuần)... Nhấn 'q' để thoát.")

    while True:
        success, img = cap.read()
        if not success: break

        # 2. Chuyển sang ảnh xám để nhận diện (OpenCV yêu cầu)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 3. Phát hiện khuôn mặt
        # scaleFactor: độ thu nhỏ ảnh, minNeighbors: số láng giềng tối thiểu
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # 4. Vẽ khung chữ nhật quanh mặt
        for (x, y, w, h) in faces:
            # Vẽ hình chữ nhật màu xanh lá (0, 255, 0), độ dày 2
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(img, "Face", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        cv2.imshow('Simple Face Detection', cv2.flip(img, 1))
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()