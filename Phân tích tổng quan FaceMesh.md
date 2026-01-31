**Phân tích tổng quan & Đặt câu hỏi**

**1. Thu thập yêu cầu tổng quát (Identify Stakeholders & Objectives)**

Bước đầu tiên là hiểu mục tiêu kinh doanh hoặc mục đích cuối cùng của dự
án. 

**Câu hỏi tổng quát:**

-   **Mục đích cuối cùng:** một đồ án nghiên cứu

-   **Ai là người dùng cuối?** Cá nhân

-   **Môi trường triển khai?** - Phần mềm chạy trên Windows cá nhân. -
    Cấu hình máy tính người dùng không có GPU 

**2. Đào sâu phân tích kỹ thuật (Requirements Analysis & Modeling)**

Yêu cầu chức năng (**Functional Requirements**) và phi chức năng
(**Non-functional Requirements**). 

**Nhiệm vụ (1) Đọc video trực tiếp từ camera:**

-   **Chất lượng video yêu cầu?** \"Cần độ phân giải 1080p)? Tốc độ
    khung hình (FPS) 30 FPS là tối thiểu để xử lý mượt mà

-   **Đồng bộ hóa âm thanh?** - Cần xử lý âm thanh từ microphone cùng
    lúc

-   **Xử lý đa nền tảng?** \"Phần mềm có cần hoạt động với nhiều loại
    camera khác nhau (webcam tích hợp, camera USB rời, IP camera)
    không?\" 

**Nhiệm vụ (2) Vẽ khung xương mặt (Facial Landmark Detection/Pose
Estimation):**

-   **Độ chính xác yêu cầu?** \"Khung xương cần 68 điểm mốc. - Độ chính
    xác cần thiết cho việc phân tích cảm xúc.

-   **Điều kiện môi trường?** \"Hệ thống có phải xử lý trong điều kiện
    thiếu sáng, góc quay nghiêng, hay khi có vật cản (ví dụ: đeo khẩu
    trang)\"

-   **Thư viện và thuật toán?** \"Không ràng buộc về việc sử dụng thư
    viện cụ thể"

**Nhiệm vụ (3) Phát video trực tiếp:**

-   **Độ trễ (Latency) chấp nhận được?** \"Độ trễ giữa hành động của
    người dùng và hình ảnh hiển thị lại là bao nhiêu 100mili giây\"

-   **Đầu ra hiển thị ở đâu?** \"Hiển thị trong cửa sổ ứng dụng
    desktop\"

-   **Khả năng lưu trữ?** \"Video sau khi xử lý không cần lưu lại file

**Giải pháp đề xuất (Sử dụng Python)**

Dựa trên các phân tích trên, một giải pháp khả thi sử dụng Python như
sau:

-   **Công nghệ lõi:** Sử dụng **OpenCV** để đọc/ghi video và hiển thị
    cơ bản, kết hợp với thư viện chuyên dụng cho thị giác máy tính.

-   **Thư viện đề xuất:** **MediaPipe** (của Google) là một lựa chọn
    tuyệt vời vì nó tích hợp cả ba nhiệm vụ trong một framework tối ưu
    cho thời gian thực. 

**Quy trình triển khai:**

1.  **Cài đặt:**

> bash
>
> pip install opencv-python mediapipe
>
> Hãy thận trọng khi sử dụng mã.

2.  **Logic xử lý (Mô hình):**

    1.  Sử dụng cv2.VideoCapture() để đọc frame từ camera.

    ```{=html}
    <!-- -->
    ```
    1.  Đưa frame qua mô hình mp.solutions.face_mesh của MediaPipe để
        > phát hiện các điểm mốc và vẽ khung xương mặt.

    ```{=html}
    <!-- -->
    ```
    1.  Sử dụng cv2.imshow() để hiển thị frame đã xử lý.
