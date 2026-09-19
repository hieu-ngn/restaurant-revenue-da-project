# Data Cleaning Plan — Zomato Delhi (Case study: Khuyến mãi)

## 1. Tình trạng hiện tại
21,321 dòng, 29 cột, một số cột thiếu rất nhiều (>95%), cột `Distance` ở dạng text, `Order Placed At` cần parse datetime.

## 2. Các bước làm sạch cụ thể

| # | Bước | Chi tiết | Lý do |
|---|---|---|---|
| 1 | Loại cột thiếu quá nhiều | Bỏ: `Instructions` (96.6%), `Review` (98.6%), `Cancellation/Rejection reason` (99.1%), `Restaurant compensation (Cancellation)` (99.4%), `Restaurant penalty (Rejection)` (100%), `Customer complaint tag` (97.8%) | Thiếu quá nhiều, không đủ tin cậy để phân tích |
| 2 | Xử lý cột `Rating` (thiếu 88.3%) | **Không điền giá trị giả**. Tạo riêng `df_rating = df[df['Rating'].notna()]` để phân tích Rating tách biệt, và ghi rõ trong báo cáo là kết quả dựa trên ~11.7% mẫu có rating | Tránh làm sai lệch kết quả nếu impute bằng trung bình |
| 3 | Parse thời gian | Chuyển `Order Placed At` sang `datetime`; tạo `order_hour`, `order_dayofweek` | Phục vụ phân tích theo thời gian, đồng bộ cách làm với Chowdeck |
| 4 | Chuẩn hóa cột `Distance` | Chuyển text ("3km", "<1km", "7.5km"...) sang số (km). Quy ước: "<1km" → 0.5km (ghi rõ giả định này trong báo cáo) | Cần dạng số để tính tương quan, vẽ biểu đồ |
| 5 | Xử lý cột `Discount construct` (thiếu 25.8%) | Missing ở đây nhiều khả năng nghĩa là **"không áp dụng khuyến mãi"** → điền `"No Discount"` thay vì bỏ trống | Missing có ý nghĩa (not random), cần xử lý đúng bản chất |
| 6 | Tạo cột tổng khuyến mãi | `total_discount` = tổng của `Restaurant discount (Promo)` + `Restaurant discount (Flat offs, Freebies & others)` + `Gold discount` + `Brand pack discount` | Phục vụ trực tiếp câu hỏi #7, #8 (tác động khuyến mãi) |
| 7 | Tạo cờ `has_discount` | `has_discount` = True nếu `total_discount > 0`, ngược lại False | Dễ dàng so sánh nhóm có/không khuyến mãi (t-test, so sánh trung bình) |
| 8 | Xử lý `Order Status` | Giữ nguyên toàn bộ trạng thái (Delivered, Rejected, Returned, Timed out...) nhưng khi tính Revenue/AOV, **chỉ dùng đơn `Delivered`** (đơn hủy/từ chối không tạo doanh thu thực) | Tránh tính doanh thu ảo từ đơn không thành công |
| 9 | Loại cột không có biến thiên | `City` (chỉ có "Delhi NCR"), `Delivery` (chỉ có "Zomato Delivery"), `Restaurant penalty (Rejection)` | Không có giá trị phân tích khi chỉ có 1 giá trị duy nhất |
| 10 | Kiểm tra outlier | Xem describe/boxplot cho `Bill subtotal`, `Total`, `KPT duration`, `Rider wait time` | Phát hiện giá trị bất thường (vd KPT quá dài do lỗi ghi nhận) |

## 3. Output sau khi làm sạch
File `zomato_clean.csv` gồm dữ liệu đã lọc cột, đã có `total_discount`, `has_discount`, `order_hour`, `order_dayofweek`, `Distance` dạng số — sẵn sàng cho bước EDA và trả lời các câu hỏi #7–#9.
