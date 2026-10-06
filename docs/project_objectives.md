# Project Objectives

**Tên đề tài (EN):** Analysis of Factors Affecting Restaurant Revenue on Food Delivery Platforms
**Tên đề tài (VN):** Phân tích các yếu tố ảnh hưởng đến doanh thu nhà hàng trên nền tảng giao đồ ăn

## 1. Mục tiêu tổng thể

Phân tích dữ liệu đơn hàng từ hai nền tảng giao đồ ăn (Chowdeck – Nigeria, Zomato – Ấn Độ) nhằm:

1. Khám phá các yếu tố có mối liên hệ với doanh thu nhà hàng.
2. Phân biệt yếu tố **trực tiếp** tạo nên doanh thu (số đơn, AOV, giá món) với yếu tố **gián tiếp** có liên hệ (Rating, thời gian giao hàng, khu vực, khung giờ, khuyến mãi).
3. So sánh xu hướng giữa hai thị trường ở mức KPI tổng hợp.
4. Đưa ra đề xuất kinh doanh dựa trên dữ liệu, nêu rõ giới hạn về tương quan và nhân quả.

## 2. Phạm vi dự án

| Thành phần | Dataset | Vai trò |
|---|---|---|
| Phân tích chính | Chowdeck (Nigeria) | Revenue, AOV, Rating, thời gian giao hàng, khu vực, nhà hàng, khung giờ |
| Phân tích bổ sung | Zomato Delhi NCR (Ấn Độ) | Tác động của khuyến mãi lên số đơn và AOV; trạng thái đơn và thời gian chuẩn bị |

**Nguyên tắc xử lý:** hai dataset được làm sạch và phân tích riêng biệt. Chỉ so sánh ở tầng KPI/insight đã tổng hợp, không gộp dữ liệu thô.

**Các quyết định đã chốt:**
- Revenue của nhà hàng (Chowdeck) = `Sub Total`; AOV nhà hàng = Revenue / số đơn; AOV khách hàng (từ `Total`) tính riêng.
- Chowdeck chỉ giữ nhóm Food, Drinks & Beverages, Pastries (loại Groceries và Medications).
- Zomato: Revenue/AOV chỉ tính trên đơn `Delivered`; Rating thiếu 88.3% không điền giá trị giả; `<1km` quy ước là 1km.

## 3. Ngoài phạm vi (Out of scope)

- Phân tích lợi nhuận (Profit) và cơ cấu chi phí: hai dataset không có dữ liệu chi phí.
- Khuyến mãi trên Chowdeck (không có cột này).
- Quy đổi tiền tệ giữa hai dataset.
- Kết luận nhân quả khi chỉ có dữ liệu quan sát.

## 4. Đầu ra dự kiến

- Business questions, objectives, data dictionary, data cleaning plan
- 2 Python notebook (cleaning + EDA) và bảng KPI tổng hợp
- KPI definitions
- Model Machine Learning nhỏ (Random Forest) để xếp hạng mức độ quan trọng giữa các yếu tố
- Power BI dashboard (trang Chowdeck, trang Zomato, trang so sánh)
- Key insights, business recommendations
- Báo cáo, outline thuyết trình, README GitHub

## 5. Đối tượng sử dụng kết quả

Chủ nhà hàng / quản lý vận hành trên nền tảng giao đồ ăn, muốn hiểu yếu tố nào có liên hệ với doanh thu để tối ưu vận hành.
