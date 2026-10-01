# Business Questions

**Project:** Analysis of Factors Affecting Restaurant Revenue on Food Delivery Platforms
**Phân tích các yếu tố ảnh hưởng đến doanh thu nhà hàng trên nền tảng giao đồ ăn**

Dự án sử dụng 3 dataset, phân tích **riêng biệt** (không gộp raw data do khác thị trường/tiền tệ/cấu trúc):

- **Dataset chính:** Chowdeck Order Delivery Details (Nigeria, 5,000 đơn, 25 nhà hàng)
- **Case study #1:** Zomato Order History (Delhi NCR, Ấn Độ, 21,321 đơn, 6 nhà hàng) — trọng tâm: khuyến mãi

---

## Phần chính — Chowdeck (Nigeria)

| # | Business Question | Loại yếu tố |
|---|---|---|
| 1 | Nhà hàng nào tạo ra doanh thu cao nhất và AOV cao nhất? | Trực tiếp |
| 2 | Nhóm món ăn (Order Category) nào đóng góp doanh thu nhiều nhất? | Trực tiếp |
| 3 | Rating có mối liên hệ với số lượng đơn hàng hoặc AOV không? | Gián tiếp |
| 4 | Thời gian giao hàng / thời gian chuẩn bị món có liên quan đến Rating hoặc số lượng đơn không? | Gián tiếp |
| 5 | Khu vực giao hàng (Delivery Location) nào có doanh thu và mật độ đơn cao nhất? | Gián tiếp |
| 6 | Khung giờ / ngày trong tuần nào tạo ra doanh thu cao nhất? | Gián tiếp |

## Case study phụ #1 — Zomato Delhi NCR (Khuyến mãi)

| # | Business Question | Loại yếu tố |
|---|---|---|
| 7 | Khuyến mãi (Promo / Flat off / Gold discount) có làm tăng số lượng đơn hàng không? | Gián tiếp |
| 8 | Khuyến mãi có làm giảm AOV không (đánh đổi giữa số lượng đơn và giá trị đơn)? | Gián tiếp |
| 9 | Đơn hàng bị hủy / từ chối (Rejected, Timed out) có liên quan đến thời gian chuẩn bị (KPT duration) không? | Gián tiếp (ảnh hưởng vận hành, gián tiếp tới doanh thu) |

## Câu hỏi so sánh liên thị trường (dựa trên bảng KPI tổng hợp, không dùng raw data gộp)

| # | Business Question |
|---|---|
| 10 | Xu hướng tương quan giữa Rating và số lượng đơn có nhất quán giữa Chowdeck và Zomato không? |
| 111 | Tác động của khuyến mãi lên hành vi đặt hàng (nếu có dữ liệu tương đương) có giống nhau giữa các thị trường không? |

---

**Lưu ý phương pháp luận:** Mọi kết luận trong dự án chỉ dừng ở mức **tương quan (correlation)**, không khẳng định **quan hệ nhân quả (causation)**, trừ khi có thiết kế thử nghiệm (A/B test) hỗ trợ.
