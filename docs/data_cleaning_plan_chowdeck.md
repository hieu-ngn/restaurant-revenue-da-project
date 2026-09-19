# Data Cleaning Plan — Chowdeck

## 1. Tình trạng hiện tại
- 5,000 dòng, 27 cột, 0% missing, 0 dòng trùng → nền tảng khá sạch, không cần xử lý missing/duplicate.
- Các cột datetime đã đúng kiểu `datetime64` khi đọc bằng pandas.

## 2. Các bước làm sạch cụ thể

| # | Bước | Chi tiết | Lý do |
|---|---|---|---|
| 1 | Chuẩn hóa tên cột | Đổi `'Total '` (có khoảng trắng thừa) → `'Total'`; đặt tên cột theo snake_case nếu muốn (tùy chọn) | Tránh lỗi khi code gọi tên cột |
| 2 | Kiểm tra tính logic thời gian | Kiểm tra thứ tự: `Order Received ≤ Preparing Order ≤ Rider Accepted ≤ Order Ready ≤ Rider At Vendor ≤ Rider Picked Up ≤ Order Arrived ≤ Order Delivered`. Đánh dấu (flag) dòng nào vi phạm thứ tự này | Dữ liệu timestamp sai thứ tự sẽ cho ra thời gian âm, làm sai KPI |
| 3 | Kiểm tra outlier | Xem boxplot/describe cho `Unit Price`, `Distance (km)`, `Total`, `Delivery Fee`. Xác định ngưỡng bất thường (vd: Distance > 50km, Total quá cao/thấp) | Outlier có thể là lỗi nhập liệu hoặc case đặc biệt cần loại khi tính trung bình |
| 4 | Kiểm tra Rating hợp lệ | Đảm bảo Rating nằm trong khoảng hợp lý (vd 1.0–5.0), không có giá trị âm hay > 5 | Đảm bảo tính đúng của yếu tố Rating |
| 5 | Tạo cột phái sinh: thời gian | - `prep_time_min` = (Order Ready − Preparing Order).minutes<br>- `delivery_time_min` = (Order Delivered − Order Received).minutes<br>- `delay_min` = (Order Delivered − Expected Delivery Time).minutes (dương = giao trễ, âm = giao sớm) | Phục vụ câu hỏi #4 (thời gian giao hàng/chuẩn bị) |
| 6 | Tạo cột phái sinh: thời điểm | - `order_hour` = giờ trích từ `Order Received`<br>- `order_dayofweek` = thứ trong tuần<br>- `order_month`, `order_year` (vì dữ liệu trải 3 năm) | Phục vụ câu hỏi #6 (khung giờ/ngày) |
| 7 | Xác định cột Revenue chuẩn | Dùng `Sub Total` làm Revenue của nhà hàng (không dùng `Total` vì gồm cả Delivery Fee + Service Fee không thuộc nhà hàng) | Tránh tính sai KPI Revenue |
| 8 | Loại cột không phục vụ phân tích | `Delivery PIN`, `Url`, `Wallet Balance`, `Account` (giữ lại nếu cần phân tích khách hàng, nếu không thì loại) | Giảm nhiễu, gọn dữ liệu |
| 9 | Cân nhắc phạm vi Order Category | Nếu muốn giữ đúng tên đề tài "Restaurant", cân nhắc lọc bỏ nhóm *Groceries* và *Medications*, chỉ giữ Food/Drinks & Beverages/Pastries — **cần bạn xác nhận có lọc hay giữ nguyên để phân tích toàn nền tảng** | Order Category hiện có cả sản phẩm phi ẩm thực |
| 10 | Kiểm tra kiểu dữ liệu cuối cùng | In lại `.dtypes` và `.describe()` sau khi làm sạch để xác nhận | Đảm bảo sẵn sàng cho EDA |

## 3. Output sau khi làm sạch
File `chowdeck_clean.csv` gồm dữ liệu gốc + các cột phái sinh (`prep_time_min`, `delivery_time_min`, `delay_min`, `order_hour`, `order_dayofweek`, `order_month`), sẵn sàng cho bước EDA.
