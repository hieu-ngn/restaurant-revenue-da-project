# Data Dictionary — Zomato Order History (Case study #1: Khuyến mãi)

Nguồn: `order_history_kaggle_data.csv` | 21,321 dòng × 29 cột | 6 nhà hàng, 1 thành phố (Delhi NCR)
Đơn vị tiền tệ: **₹ (Rupee, Ấn Độ)** | 1 dòng = 1 đơn hàng | Kênh giao: 100% "Zomato Delivery"

| Cột | Kiểu dữ liệu | % Missing | Ý nghĩa | Vai trò trong phân tích |
|---|---|---|---|---|
| Restaurant ID | int | 0% | Mã nhà hàng | Định danh |
| Restaurant name | string | 0% | Tên nhà hàng (6 giá trị) | Yếu tố trực tiếp (Nhà hàng) |
| Subzone | string | 0% | Khu vực nhỏ | Yếu tố gián tiếp (khu vực) |
| City | string | 0% | Thành phố (chỉ có "Delhi NCR") | Không có biến thiên — không dùng để so sánh thành phố |
| Order ID | int | 0% | Mã đơn hàng | Khóa chính |
| Order Placed At | string (cần parse) | 0% | Thời điểm đặt hàng | Dùng phân tích theo giờ/ngày |
| Order Status | string | 0% | Trạng thái đơn: Delivered, Rejected, Returned, Return cancelled, Picked up, Timed out | Yếu tố trạng thái đơn hàng |
| Delivery | string | 0% | Đơn vị giao hàng (chỉ có "Zomato Delivery") | Không có biến thiên |
| Distance | string (dạng "3km", "<1km") | 0% | Khoảng cách giao hàng | Yếu tố gián tiếp — **cần làm sạch thành số trước khi phân tích** |
| Items in order | string | 0% | Danh sách món trong đơn (dạng text gộp) | Cần tách chuỗi nếu muốn phân tích theo món |
| Instructions | string | 96.6% | Ghi chú của khách | Bỏ qua (thiếu quá nhiều) |
| Discount construct | string | 25.8% | Mô tả chương trình khuyến mãi áp dụng | Yếu tố khuyến mãi (mô tả) |
| Bill subtotal | float | 0% | Tổng tiền hàng trước chiết khấu | Thành phần tính Revenue |
| Packaging charges | float | 0% | Phí đóng gói | Không thuộc doanh thu món ăn |
| Restaurant discount (Promo) | float | 0% | Số tiền giảm giá do nhà hàng chạy promo | **Yếu tố khuyến mãi chính** |
| Restaurant discount (Flat offs, Freebies & others) | float | 0% | Giảm giá dạng flat/freebie khác | Yếu tố khuyến mãi |
| Gold discount | float | 0% | Giảm giá cho thành viên Zomato Gold | Yếu tố khuyến mãi |
| Brand pack discount | float | 0% | Giảm giá gói thương hiệu | Yếu tố khuyến mãi |
| **Total** | float | 0% | Tổng tiền khách trả sau chiết khấu | Dùng tính Revenue thực nhận |
| Rating | float | **88.3%** | Đánh giá đơn hàng (1–5) | ⚠️ Quá thưa — chỉ phân tích mang tính tham khảo, không kết luận mạnh |
| Review | string | 98.6% | Nhận xét text | Bỏ qua (thiếu quá nhiều) |
| Cancellation / Rejection reason | string | 99.1% | Lý do hủy/từ chối | Chỉ áp dụng cho nhóm đơn bị hủy |
| Restaurant compensation (Cancellation) | float | 99.4% | Bồi thường khi hủy | Bỏ qua |
| Restaurant penalty (Rejection) | float | 100% | Phạt khi từ chối đơn | **Cột rỗng hoàn toàn — loại bỏ** |
| KPT duration (minutes) | float | 1.4% | Thời gian bếp chuẩn bị món (Kitchen Prep Time) | Yếu tố gián tiếp (thời gian chuẩn bị) |
| Rider wait time (minutes) | float | 0.8% | Thời gian tài xế chờ lấy hàng | Yếu tố vận hành |
| Order Ready Marked | string | 0% | Đơn được đánh dấu sẵn sàng đúng hạn hay không | Yếu tố vận hành |
| Customer complaint tag | string | 97.8% | Nhãn khiếu nại | Bỏ qua (thiếu quá nhiều) |
| Customer ID | string (hash) | 0% | Mã khách hàng đã ẩn danh | Định danh khách hàng |

## Ghi chú quan trọng
- **Rating thiếu 88.3%** → đây là hạn chế lớn nhất, phải nêu rõ trong báo cáo, không dùng để kết luận chắc chắn.
- **Chỉ 6 nhà hàng** → không đủ mẫu để phân tích sâu yếu tố "loại hình nhà hàng", chỉ dùng để minh họa case study khuyến mãi.
- Cột `Restaurant penalty (Rejection)` thiếu 100% → loại bỏ khỏi phân tích.
- `Distance` là dạng text ("3km", "<1km") cần chuẩn hóa thành số (float, đơn vị km) khi làm sạch dữ liệu.
- Không có Total Delivery Fee / Service Fee tách riêng như Chowdeck.
