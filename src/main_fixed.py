import cv2
# THAY ĐỔI QUAN TRỌNG: Import trực tiếp module, không thông qua mp.solutions
from mediapipe.python.solutions import face_mesh
from mediapipe.python.solutions import drawing_utils
from mediapipe.python.solutions import drawing_styles

def main():
    # Cấu hình camera
    cap = cv2.VideoCapture(0)

    # Khởi tạo Face Mesh bằng cách gọi trực tiếp class
    # Lưu ý: Không còn dùng mp.solutions.face_mesh nữa
    with face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as mesh:
        
        print("Đang chạy chế độ Import Trực Tiếp... Nhấn 'q' để thoát.")

        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Không đọc được camera")
                break

            # Xử lý hình ảnh
            image.flags.writeable = False
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = mesh.process(image_rgb)

            # Vẽ kết quả
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    # Vẽ lưới
                    drawing_utils.draw_landmarks(
                        image=image,
                        landmark_list=face_landmarks,
                        connections=face_mesh.FACEMESH_TESSELATION,
                        landmark_drawing_spec=None,
                        connection_drawing_spec=drawing_styles
                        .get_default_face_mesh_tesselation_style())
                    
                    # Vẽ viền
                    drawing_utils.draw_landmarks(
                        image=image,
                        landmark_list=face_landmarks,
                        connections=face_mesh.FACEMESH_CONTOURS,
                        landmark_drawing_spec=None,
                        connection_drawing_spec=drawing_styles
                        .get_default_face_mesh_contours_style())

            cv2.imshow('Face Mesh Fixed', cv2.flip(image, 1))
            
            if cv2.waitKey(5) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()