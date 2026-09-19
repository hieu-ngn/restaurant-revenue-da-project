# Data Dictionary — Chowdeck Order Delivery Details

Nguồn: `Chowdeck_Order_Delivery_Details.xlsx` (Sheet1) | 5,000 dòng × 27 cột | 0% missing | 0 dòng trùng
Đơn vị tiền tệ: **₦ (Naira, Nigeria)** | 1 dòng = 1 đơn hàng

| Cột | Kiểu dữ liệu | Ý nghĩa | Vai trò trong phân tích |
|---|---|---|---|
| Account | string | Mã tài khoản khách hàng | Định danh khách hàng |
| Delivery PIN | int | Mã PIN xác nhận giao hàng | Không dùng cho phân tích |
| Delivery Location | string | Khu vực giao hàng | Yếu tố gián tiếp (khu vực) |
| Shop Location | string | Khu vực đặt của cửa hàng | Yếu tố gián tiếp (khu vực) |
| Order Category | string | Nhóm sản phẩm (Food, Drinks & Beverages, Pastries, Groceries, Medications...) | Yếu tố trực tiếp/gián tiếp (nhóm món) — **lưu ý: không chỉ có đồ ăn** |
| Item Ordered | string | Tên món/sản phẩm được đặt | Mô tả, dùng để nhóm phân tích theo món |
| Shop Name | string | Tên cửa hàng/nhà hàng (25 giá trị duy nhất) | Yếu tố trực tiếp (Nhà hàng) |
| Unit Price | int | Đơn giá sản phẩm | Yếu tố trực tiếp (Giá món) |
| Quantity | int | Số lượng sản phẩm trong đơn | Dùng tính Sub Total |
| Distance (km) | float | Khoảng cách giao hàng | Yếu tố gián tiếp |
| Sub Total | int | Tổng tiền hàng trước phí (= Unit Price × Quantity) | Thành phần tính Revenue |
| Delivery Fee | int | Phí giao hàng | Không tính vào Revenue của nhà hàng (thường thuộc nền tảng) |
| Service Fee | int | Phí dịch vụ | Không tính vào Revenue của nhà hàng |
| **Total** | int | Tổng tiền khách trả (Sub Total + Delivery Fee + Service Fee) | **Dùng thận trọng — cần tách Sub Total ra để tính Revenue thực của nhà hàng** |
| Payment Method | string | Phương thức thanh toán | Yếu tố mô tả |
| Rating | float | Đánh giá đơn hàng (thang điểm) | Yếu tố gián tiếp |
| Order Received | datetime | Thời điểm nhà hàng nhận đơn | Mốc thời gian giao hàng |
| Preparing Order | datetime | Thời điểm bắt đầu chuẩn bị món | Dùng tính thời gian chuẩn bị |
| Rider Accepted | datetime | Thời điểm tài xế nhận đơn | Mốc thời gian giao hàng |
| Order Ready | datetime | Thời điểm món ăn sẵn sàng | Dùng tính thời gian chuẩn bị (Preparing → Order Ready) |
| Rider At Vendor | datetime | Thời điểm tài xế đến cửa hàng | Mốc thời gian giao hàng |
| Rider Picked Up | datetime | Thời điểm tài xế lấy hàng | Mốc thời gian giao hàng |
| Expected Delivery Time | datetime | Thời gian giao hàng dự kiến | Dùng so sánh với thời gian giao thực tế → tính độ trễ |
| Order Arrived | datetime | Thời điểm tài xế đến điểm giao | Mốc thời gian giao hàng |
| Order Delivered | datetime | Thời điểm giao hàng hoàn tất | Dùng tính tổng thời gian giao hàng (Order Received → Order Delivered) |
| Wallet Balance | int | Số dư ví khách hàng | Không liên quan trực tiếp đến Revenue nhà hàng |
| Url | string | Link ảnh minh họa món ăn | Không dùng cho phân tích |

## Ghi chú quan trọng
- **Không có cột khuyến mãi/discount** → không phân tích được yếu tố này trên dataset chính.
- **Không có số lượng review** (chỉ có Rating đơn lẻ theo từng đơn hàng).
- **Không có OrderID riêng** — xác nhận qua kiểm tra: gần như mỗi dòng là 1 đơn hàng độc lập (chỉ 3 cặp Account + Order Received trùng nhau trong 5,000 dòng).
- **Revenue của nhà hàng nên tính từ `Sub Total`**, không phải `Total` (vì Total gồm cả phí giao hàng/dịch vụ vốn không thuộc doanh thu nhà hàng).
- Order Category gồm cả *Groceries* và *Medications* — cần cân nhắc lọc lại nếu muốn giữ đúng phạm vi "restaurant/food".
