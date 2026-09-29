# Analysis of Factors Affecting Restaurant Revenue on Food Delivery Platforms
### Phân tích các yếu tố ảnh hưởng đến doanh thu nhà hàng trên nền tảng giao đồ ăn

## Mục tiêu dự án
Phân tích dữ liệu đơn hàng để khám phá các yếu tố có mối liên hệ với doanh thu nhà hàng trên nền tảng giao đồ ăn, từ đó đưa ra đề xuất kinh doanh dựa trên dữ liệu.

Chi tiết: xem [`docs/project_objectives.md`](docs/project_objectives.md) và [`docs/business_questions.md`](docs/business_questions.md).

## Dataset sử dụng (2 dataset)

| Dataset | Thị trường | Vai trò | Nguồn |
|---|---|---|---|
| Chowdeck Order Delivery Details | Nigeria | Phân tích chính: Revenue, AOV, Rating, thời gian giao hàng, khu vực, khung giờ | Nội bộ project |
| Zomato Order History | Ấn Độ (Delhi NCR) | Phân tích bổ sung: tác động của khuyến mãi lên số đơn & AOV, trạng thái đơn | [Kaggle](https://www.kaggle.com/datasets/sujalsuthar/food-delivery-order-history-data) |

Chi tiết cấu trúc dữ liệu: `docs/data_dictionary_chowdeck.md`, `docs/data_dictionary_zomato.md`.

## Cấu trúc thư mục

```
├── data/
│   ├── raw/        # Dữ liệu gốc, không chỉnh sửa
│   └── clean/      # Dữ liệu sau khi làm sạch (output từ notebooks/)
├── notebooks/      # 2 notebook Jupyter: cleaning + EDA (biểu đồ hiện inline khi chạy)
├── docs/           # Business questions, objectives, data dictionary, cleaning plan, KPI, giải thích code
├── outputs/
│   ├── charts/         # Biểu đồ EDA (PNG)
│   └── kpi_summary/    # Bảng KPI tổng hợp mỗi dataset
├── powerbi/        # File dashboard Power BI (.pbix) — đang cập nhật
└── report/         # Báo cáo & slide thuyết trình cuối — đang cập nhật
```

## Tiến độ hiện tại
- [x] Business questions & objectives
- [x] Data dictionary
- [x] Data cleaning plan
- [x] Data cleaning + EDA bằng Python (2 notebook)
- [x] Định nghĩa KPI chính thức (`docs/kpi_definitions.md`)
- [ ] Power BI dashboard
- [ ] Key insights & Business recommendations
- [ ] Machine Learning (nếu phù hợp)
- [ ] Báo cáo & thuyết trình cuối cùng

## Cách chạy lại notebook
Mở trong Jupyter/VS Code, chọn kernel đã cài sẵn thư viện, rồi **Run All**:
```bash
pip install pandas numpy matplotlib seaborn openpyxl
```
Notebook tự tìm đúng đường dẫn `data/raw/` dù mở/chạy từ đâu. Biểu đồ vừa hiện ngay dưới mỗi cell, vừa lưu file PNG vào `outputs/charts/`.

## KPI chính
```
Revenue = Number of Orders × AOV
AOV (nhà hàng) = Total Revenue / Total Orders
```
Chowdeck tách riêng **AOV nhà hàng** (từ `Sub Total`) và **AOV khách hàng** (từ `Total`, gồm phí ship/dịch vụ) — xem chi tiết `docs/kpi_definitions.md`.

## Giới hạn dữ liệu (Limitations)
- Chowdeck: 29% đơn có thứ tự timestamp giao hàng không hợp lệ (đã đánh dấu bằng cột `time_sequence_valid`, không xóa). Không có dữ liệu khuyến mãi/số lượng review. Đã lọc bỏ nhóm Groceries/Medications, chỉ giữ Food/Drinks & Beverages/Pastries.
- Zomato: Rating thiếu 88.3% (không điền giá trị giả). Chỉ 6 nhà hàng. Dữ liệu chỉ trong 5 tháng (09/2024–01/2025). Revenue/AOV chỉ tính trên đơn `Delivered`.
- Không gộp 2 dataset ở tầng dữ liệu thô (khác tiền tệ, khác thị trường) — chỉ so sánh ở mức KPI tổng hợp.
- Mọi kết luận chỉ dừng ở mức tương quan (correlation), không khẳng định quan hệ nhân quả (causation).

## Thành viên nhóm
- [Tên bạn]
- [Tên bạn cùng làm]
