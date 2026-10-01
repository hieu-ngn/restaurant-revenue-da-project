# Analysis of Factors Affecting Restaurant Revenue on Food Delivery Platforms
### Phân tích các yếu tố ảnh hưởng đến doanh thu nhà hàng trên nền tảng giao đồ ăn

## Mục tiêu dự án
Phân tích dữ liệu đơn hàng để khám phá các yếu tố có mối liên hệ với doanh thu nhà hàng trên nền tảng giao đồ ăn, từ đó đưa ra đề xuất kinh doanh dựa trên dữ liệu.

<<<<<<< HEAD
Chi tiết mục tiêu và câu hỏi kinh doanh: xem [`docs/project_objectives.md`](docs/project_objectives.md) và [`docs/business_questions.md`](docs/business_questions.md).

## Dataset sử dụng

| Dataset | Thị trường | Vai trò | Nguồn |
|---|---|---|---|
| Chowdeck Order Delivery Details | Nigeria | Phân tích chính (Revenue, AOV, Rating, thời gian giao hàng...) | Nội bộ project |
| Zomato Order History | Ấn Độ (Delhi NCR) | Case study bổ sung: tác động của khuyến mãi | [Kaggle](https://www.kaggle.com/datasets/sujalsuthar/food-delivery-order-history-data) |

Xem chi tiết cấu trúc dữ liệu tại `docs/data_dictionary_*.md`.
=======
Chi tiết: xem [`docs/project_objectives.md`](docs/project_objectives.md) và [`docs/business_questions.md`](docs/business_questions.md).

## Dataset sử dụng (2 dataset)

| Dataset | Thị trường | Vai trò | Nguồn |
|---|---|---|---|
| Chowdeck Order Delivery Details | Nigeria | Phân tích chính: Revenue, AOV, Rating, thời gian giao hàng, khu vực, khung giờ | Nội bộ project |
| Zomato Order History | Ấn Độ (Delhi NCR) | Phân tích bổ sung: tác động của khuyến mãi lên số đơn & AOV, trạng thái đơn | [Kaggle](https://www.kaggle.com/datasets/sujalsuthar/food-delivery-order-history-data) |

Chi tiết cấu trúc dữ liệu: `docs/data_dictionary_chowdeck.md`, `docs/data_dictionary_zomato.md`.
>>>>>>> d5c21e95157aa28085175faf9d1a3c833c2cf774

## Cấu trúc thư mục

```
├── data/
│   ├── raw/        # Dữ liệu gốc, không chỉnh sửa
│   └── clean/      # Dữ liệu sau khi làm sạch (output từ notebooks/)
<<<<<<< HEAD
├── notebooks/      # Script Python: cleaning + EDA
├── docs/           # Business questions, objectives, data dictionary, cleaning plan
├── outputs/
│   ├── charts/        # Biểu đồ EDA (PNG)
│   └── kpi_summary/   # Bảng KPI tổng hợp mỗi dataset
=======
├── notebooks/      # 2 notebook Jupyter: cleaning + EDA (biểu đồ hiện inline khi chạy)
├── docs/           # Business questions, objectives, data dictionary, cleaning plan, KPI, giải thích code
├── outputs/
│   ├── charts/         # Biểu đồ EDA (PNG)
│   └── kpi_summary/    # Bảng KPI tổng hợp mỗi dataset
>>>>>>> d5c21e95157aa28085175faf9d1a3c833c2cf774
├── powerbi/        # File dashboard Power BI (.pbix) — đang cập nhật
└── report/         # Báo cáo & slide thuyết trình cuối — đang cập nhật
```

## Tiến độ hiện tại
- [x] Business questions & objectives
- [x] Data dictionary
- [x] Data cleaning plan
<<<<<<< HEAD
- [x] Data cleaning + EDA bằng Python (Chowdeck, Zomato)
- [ ] Tính toán KPI chính thức
=======
- [x] Data cleaning + EDA bằng Python (2 notebook)
- [x] Định nghĩa KPI chính thức (`docs/kpi_definitions.md`)
>>>>>>> d5c21e95157aa28085175faf9d1a3c833c2cf774
- [ ] Power BI dashboard
- [ ] Key insights & Business recommendations
- [ ] Machine Learning (nếu phù hợp)
- [ ] Báo cáo & thuyết trình cuối cùng

<<<<<<< HEAD
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
- [Tên bạn]
- [Tên bạn cùng làm]
=======
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
- Nguyễn Minh Hiếu
- Trần Thị Huyền Trang
>>>>>>> d5c21e95157aa28085175faf9d1a3c833c2cf774
