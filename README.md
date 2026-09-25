# Analysis of Factors Affecting Restaurant Revenue on Food Delivery Platforms
### Phân tích các yếu tố ảnh hưởng đến doanh thu nhà hàng trên nền tảng giao đồ ăn

## Mục tiêu dự án
Phân tích dữ liệu đơn hàng để khám phá các yếu tố có mối liên hệ với doanh thu nhà hàng trên nền tảng giao đồ ăn, từ đó đưa ra đề xuất kinh doanh dựa trên dữ liệu.

Chi tiết mục tiêu và câu hỏi kinh doanh: xem [`docs/project_objectives.md`](docs/project_objectives.md) và [`docs/business_questions.md`](docs/business_questions.md).

## Dataset sử dụng

| Dataset | Thị trường | Vai trò | Nguồn |
|---|---|---|---|
| Chowdeck Order Delivery Details | Nigeria | Phân tích chính (Revenue, AOV, Rating, thời gian giao hàng...) | Nội bộ project |
| Zomato Order History | Ấn Độ (Delhi NCR) | Case study bổ sung: tác động của khuyến mãi | [Kaggle](https://www.kaggle.com/datasets/sujalsuthar/food-delivery-order-history-data) |

Xem chi tiết cấu trúc dữ liệu tại `docs/data_dictionary_*.md`.

## Cấu trúc thư mục

```
├── data/
│   ├── raw/        # Dữ liệu gốc, không chỉnh sửa
│   └── clean/      # Dữ liệu sau khi làm sạch (output từ notebooks/)
├── notebooks/      # Script Python: cleaning + EDA
├── docs/           # Business questions, objectives, data dictionary, cleaning plan
├── outputs/
│   ├── charts/        # Biểu đồ EDA (PNG)
│   └── kpi_summary/   # Bảng KPI tổng hợp mỗi dataset
├── powerbi/        # File dashboard Power BI (.pbix) — đang cập nhật
└── report/         # Báo cáo & slide thuyết trình cuối — đang cập nhật
```

## Tiến độ hiện tại
- [x] Business questions & objectives
- [x] Data dictionary
- [x] Data cleaning plan
- [x] Data cleaning + EDA bằng Python (Chowdeck, Zomato)
- [ ] Tính toán KPI chính thức
- [ ] Power BI dashboard
- [ ] Key insights & Business recommendations
- [ ] Machine Learning (nếu phù hợp)
- [ ] Báo cáo & thuyết trình cuối cùng

## Cách chạy lại code
```bash
pip install pandas numpy matplotlib seaborn openpyxl
python notebooks/01_chowdeck_cleaning_eda.py
python notebooks/02_zomato_cleaning_eda.py
```
Script cần chạy từ thư mục có sẵn file dữ liệu gốc trong `data/raw/`, hoặc chỉnh lại đường dẫn trong code trước khi chạy.

## Giới hạn dữ liệu (Limitations)
- Chowdeck: 29% đơn hàng có thứ tự timestamp giao hàng không hợp lệ (đã được đánh dấu, chưa loại bỏ).
- Chowdeck: không có dữ liệu khuyến mãi/số lượng review.
- Zomato: cột Rating thiếu 88.3%, chỉ 6 nhà hàng, dữ liệu chỉ trong 5 tháng (09/2024–01/2025).
- Mọi kết luận chỉ dừng ở mức tương quan (correlation), không khẳng định quan hệ nhân quả (causation).

## Thành viên nhóm
- Nguyễn Minh Hiếu
- Trần Thị Huyền Trang
