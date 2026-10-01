# Project Objectives

**Tên đề tài (EN):** Analysis of Factors Affecting Restaurant Revenue on Food Delivery Platforms
**Tên đề tài (VN):** Phân tích các yếu tố ảnh hưởng đến doanh thu nhà hàng trên nền tảng giao đồ ăn

## 1. Mục tiêu tổng thể

Phân tích dữ liệu đơn hàng và thông tin nhà hàng từ nhiều nền tảng giao đồ ăn (Chowdeck – Nigeria, Zomato – Ấn Độ, và một nhà hàng độc lập tại Anh) nhằm:

1. Khám phá các yếu tố có mối liên hệ với doanh thu nhà hàng (Revenue).
2. Phân biệt rõ giữa:
   - Yếu tố **trực tiếp tạo nên doanh thu** (ví dụ: số lượng đơn hàng, giá món, AOV)
   - Yếu tố **gián tiếp có liên hệ với doanh thu** (ví dụ: Rating, thời gian giao hàng, khu vực, khung giờ)
   - Yếu tố **ảnh hưởng đến lợi nhuận (Profit)** nhưng không nhất thiết ảnh hưởng doanh thu (ví dụ: chi phí nguyên liệu, kênh bán hàng)
3. So sánh insight ở mức KPI tổng hợp giữa các thị trường khác nhau, để xem các phát hiện có tính nhất quán hay đặc thù theo từng thị trường.
4. Đưa ra đề xuất kinh doanh dựa trên dữ liệu (data-driven), có nêu rõ giới hạn về tính tương quan/nhân quả.

## 2. Phạm vi dự án

| Thành phần | Dataset | Vai trò |
|---|---|---|
| Phân tích chính | Chowdeck Order Delivery Details | Phân tích đầy đủ nhất: Revenue, AOV, Rating, thời gian giao hàng, khu vực, nhà hàng |
| Case study phụ #1 | Zomato Order History (Delhi NCR) | Tập trung vào tác động của khuyến mãi/discount và trạng thái đơn hàng |
| Case study phụ #2 | Anonymized Restaurant Sales Data (UK) | Tập trung vào phân biệt yếu tố ảnh hưởng Revenue vs Profit |

**Nguyên tắc xử lý:** 3 dataset được làm sạch và phân tích **riêng biệt** (khác đơn vị tiền tệ, khác thị trường, khác cấu trúc dữ liệu). Chỉ so sánh ở tầng kết quả KPI/insight đã tổng hợp, không gộp dữ liệu thô.

## 3. Ngoài phạm vi (Out of scope)

- Không phân tích khuyến mãi trên Chowdeck (dataset không có cột này).
- Không phân tích Rating / thời gian giao hàng / khoảng cách trên dataset UK (không có các cột này).
- Không phân tích yếu tố "Nhà hàng" (so sánh nhiều nhà hàng) trên dataset UK (chỉ có 1 nhà hàng).
- Không quy đổi tiền tệ giữa các dataset để so sánh số tuyệt đối.
- Không đưa ra kết luận nhân quả (causation) nếu chỉ có dữ liệu quan sát (observational data) mà không có thử nghiệm đối chứng.

## 4. Đầu ra dự kiến của toàn bộ dự án

- Business questions & objectives (tài liệu này)
- Data dictionary chuẩn hóa cho từng dataset
- Data cleaning plan cho từng dataset
- Python EDA notebook cho từng dataset (3 notebook)
- Bảng KPI tổng hợp (`summary_metrics.csv`) dùng để so sánh liên thị trường
- Power BI dashboard: 3 trang riêng theo dataset + 1 trang so sánh tổng hợp
- Key insights & Business recommendations
- Project report & Presentation outline
- README cho GitHub

## 5. Đối tượng sử dụng kết quả

Chủ nhà hàng / quản lý vận hành trên nền tảng giao đồ ăn, muốn hiểu yếu tố nào tác động đến doanh thu để tối ưu vận hành (giá, khuyến mãi, thời gian giao hàng, chất lượng dịch vụ).
