# Business Questions

**Project:** Analysis of Factors Affecting Restaurant Revenue on Food Delivery Platforms
**Phân tích các yếu tố ảnh hưởng đến doanh thu nhà hàng trên nền tảng giao đồ ăn**

Dự án dùng 2 dataset, phân tích **riêng biệt** (không gộp dữ liệu thô do khác thị trường, tiền tệ và cấu trúc):

- **Dataset chính:** Chowdeck Order Delivery Details (Nigeria) — sau khi lọc còn 3,061 đơn thuộc nhóm Food / Drinks & Beverages / Pastries
- **Phân tích bổ sung:** Zomato Order History (Delhi NCR, Ấn Độ, 21,321 đơn, 6 nhà hàng) — trọng tâm: khuyến mãi

---

## Phần chính — Chowdeck (Nigeria)

| # | Business Question | Loại yếu tố |
|---|---|---|
| 1 | Nhà hàng nào tạo ra doanh thu cao nhất và AOV cao nhất? | Trực tiếp |
| 2 | Nhóm món (Order Category) nào đóng góp doanh thu nhiều nhất? | Trực tiếp |
| 3 | Rating có mối liên hệ với số lượng đơn hàng hoặc AOV không? | Gián tiếp |
| 4 | Thời gian giao hàng / thời gian chuẩn bị món có liên quan đến Rating không? | Gián tiếp |
| 5 | Khu vực giao hàng (Delivery Location) nào có doanh thu và mật độ đơn cao nhất? | Gián tiếp |
| 6 | Khung giờ / ngày trong tuần nào tạo ra doanh thu cao nhất? | Gián tiếp |

## Phân tích bổ sung — Zomato Delhi NCR (Khuyến mãi)

| # | Business Question | Loại yếu tố |
|---|---|---|
| 7 | Đơn có khuyến mãi (Promo / Flat off / Gold / Brand pack) có số lượng nhiều hơn đơn không khuyến mãi không? | Gián tiếp |
| 8 | Đơn có khuyến mãi có AOV thấp hơn đơn không khuyến mãi không? | Gián tiếp |
| 9 | Đơn bị hủy / từ chối / timeout có liên quan đến thời gian chuẩn bị món (KPT) không? | Gián tiếp (vận hành) |

---

## Yếu tố trực tiếp và gián tiếp

- **Trực tiếp tạo nên doanh thu:** số lượng đơn hàng, AOV, giá món, số lượng món mỗi đơn (Revenue = Orders × AOV).
- **Gián tiếp có liên hệ với doanh thu:** Rating, thời gian giao hàng / chuẩn bị, khu vực, khung giờ, khuyến mãi, trạng thái đơn.
- **Ảnh hưởng đến lợi nhuận thay vì doanh thu** (chi phí nguyên liệu, nhân sự, phí nền tảng...): nằm ngoài phạm vi dự án vì hai dataset không có dữ liệu chi phí.

## Giới hạn cần nêu trong báo cáo

- Chowdeck không có dữ liệu khuyến mãi và không có số lượng review.
- Chowdeck có 29% đơn với thứ tự timestamp không hợp lệ (đã đánh dấu bằng cột `time_sequence_valid`, không xóa).
- Zomato: Rating thiếu 88.3%, chỉ 6 nhà hàng, dữ liệu 5 tháng (09/2024 – 01/2025).
- Chỉ so sánh 2 thị trường ở mức xu hướng và tỷ lệ %, không so sánh số tuyệt đối do khác tiền tệ.

**Lưu ý phương pháp luận:** Mọi kết luận chỉ dừng ở mức **tương quan (correlation)**, không khẳng định **quan hệ nhân quả (causation)**.
