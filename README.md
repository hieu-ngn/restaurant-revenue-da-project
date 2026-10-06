
# Analysis of Factors Affecting Restaurant Revenue on Food Delivery Platforms

### Phân tích các yếu tố ảnh hưởng đến doanh thu nhà hàng trên nền tảng giao đồ ăn

## Mục tiêu dự án

Phân tích dữ liệu đơn hàng để khám phá các yếu tố có mối liên hệ với doanh thu nhà hàng trên nền tảng giao đồ ăn, từ đó đưa ra đề xuất kinh doanh dựa trên dữ liệu.

Chi tiết: xem [`docs/project_objectives.md`](docs/project_objectives.md) và [`docs/business_questions.md`](docs/business_questions.md).

## Dataset sử dụng (2 dataset)

| Dataset                         | Thị trường        | Vai trò                                                                                     | Nguồn                                                                                |
| ------------------------------- | -------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Chowdeck Order Delivery Details | Nigeria              | Phân tích chính: Revenue, AOV, Rating, thời gian giao hàng, khu vực, khung giờ        | Nội bộ project                                                                      |
| Zomato Order History            | Ấn Độ (Delhi NCR) | Phân tích bổ sung: tác động của khuyến mãi lên số đơn & AOV, trạng thái đơn | [Kaggle](https://www.kaggle.com/datasets/sujalsuthar/food-delivery-order-history-data) |

Chi tiết cấu trúc dữ liệu: `docs/data_dictionary_chowdeck.md`, `docs/data_dictionary_zomato.md`.

## Cấu trúc thư mục

```
├── data/
│   ├── raw/        # Dữ liệu gốc, không chỉnh sửa
│   └── clean/      # Dữ liệu sau khi làm sạch (output từ notebooks/)
├── notebooks/      # 8 notebook Jupyter, tách riêng từng giai đoạn (xem mục "Thứ tự chạy" bên dưới)
├── docs/           # Business questions, objectives, data dictionary, cleaning plan, KPI, ML summary, giải thích code
├── outputs/
│   ├── charts/         # Biểu đồ EDA + ML (PNG)
│   └── kpi_summary/    # Bảng KPI tổng hợp mỗi dataset
├── powerbi/        # File dashboard Power BI (.pbix) — đang cập nhật
└── report/         # Báo cáo & slide thuyết trình cuối — đang cập nhật
```

## Thứ tự chạy notebook

Mỗi dataset được tách thành các notebook riêng theo đúng từng bước của quy trình (Cleaning → EDA → KPI → Machine Learning). **Phải chạy đúng thứ tự** vì notebook sau đọc file do notebook trước tạo ra:

| # | Notebook                        | Việc làm                                                     | Output                                           |
| - | ------------------------------- | -------------------------------------------------------------- | ------------------------------------------------ |
| 1 | `01a_chowdeck_cleaning.ipynb` | Làm sạch dữ liệu Chowdeck                                  | `data/clean/chowdeck_clean.csv`                |
| 2 | `01b_chowdeck_eda.ipynb`      | EDA, trả lời BQ#1–6                                         | Biểu đồ trong`outputs/charts/`              |
| 3 | `01c_chowdeck_kpi.ipynb`      | Tính KPI chính thức                                         | `outputs/kpi_summary/chowdeck_kpi_summary.csv` |
| 4 | `02a_zomato_cleaning.ipynb`   | Làm sạch dữ liệu Zomato                                    | `data/clean/zomato_clean.csv`                  |
| 5 | `02b_zomato_eda.ipynb`        | EDA, trả lời BQ#7–9 (khuyến mãi)                          | Biểu đồ trong`outputs/charts/`              |
| 6 | `02c_zomato_kpi.ipynb`        | Tính KPI chính thức                                         | `outputs/kpi_summary/zomato_kpi_summary.csv`   |
| 7 | `03_chowdeck_ml.ipynb`        | Model dự đoán đơn giá trị cao + Cross-Validation + SHAP | Biểu đồ ML trong`outputs/charts/`           |
| 8 | `04_zomato_ml.ipynb`          | Model dự đoán đơn giá trị cao + Cross-Validation + SHAP | Biểu đồ ML trong`outputs/charts/`           |

Cài thư viện 1 lần trước khi chạy:

```bash
pip install pandas numpy matplotlib seaborn openpyxl scikit-learn shap
```

Mở từng notebook trong Jupyter/VS Code, bấm **Run All** theo đúng thứ tự 1→8. Notebook tự tìm đúng đường dẫn `data/raw/` và `data/clean/` dù mở/chạy từ đâu. Biểu đồ vừa hiện ngay dưới mỗi cell, vừa lưu file PNG vào `outputs/charts/`.

**Làm việc nhóm 2 người:** có thể chia — 1 người phụ trách các file `01x_chowdeck_*` + `03_chowdeck_ml`, 1 người phụ trách các file `02x_zomato_*` + `04_zomato_ml` — không đụng file của nhau.

## KPI chính

```
Revenue = Number of Orders × AOV
AOV (nhà hàng) = Total Revenue / Total Orders
```

Chowdeck tách riêng **AOV nhà hàng** (từ `Sub Total`) và **AOV khách hàng** (từ `Total`, gồm phí ship/dịch vụ) — xem chi tiết `docs/kpi_definitions.md`.

## Machine Learning

2 model Random Forest Classifier (1 cho mỗi dataset) dự đoán đơn hàng thuộc nhóm "giá trị cao" hay "giá trị thấp", dùng Feature Importance + SHAP Values để xác định đa biến yếu tố nào thực sự ảnh hưởng đến giá trị đơn hàng — bổ sung bằng chứng cho phần phân tích tương quan ở EDA. Đã kiểm định bằng Cross-Validation 5-fold để đảm bảo kết quả ổn định, không phụ thuộc may rủi khi chia dữ liệu. Chi tiết: `docs/ml_summary.md`, giải thích code từng dòng: `docs/Giai_thich_code_ML_Chowdeck.docx`, `docs/Giai_thich_code_ML_Zomato.docx`.

## Tiến độ hiện tại

- [X] Business questions & objectives
- [X] Data dictionary
- [X] Data cleaning plan
- [X] Data cleaning + EDA bằng Python (Chowdeck, Zomato)
- [X] Định nghĩa KPI chính thức (`docs/kpi_definitions.md`)
- [X] Machine Learning: dự đoán đơn giá trị cao, Cross-Validation, SHAP (`docs/ml_summary.md`)
- [ ] Power BI dashboard
- [ ] Key insights & Business recommendations
- [ ] Báo cáo & thuyết trình cuối cùng

## Giới hạn dữ liệu (Limitations)

- Chowdeck: 29% đơn có thứ tự timestamp giao hàng không hợp lệ (đã đánh dấu bằng cột `time_sequence_valid`, không xóa). Không có dữ liệu khuyến mãi/số lượng review. Đã lọc bỏ nhóm Groceries/Medications, chỉ giữ Food/Drinks & Beverages/Pastries.
- Zomato: Rating thiếu 88.3% (không điền giá trị giả). Chỉ 6 nhà hàng. Dữ liệu chỉ trong 5 tháng (09/2024–01/2025). Revenue/AOV chỉ tính trên đơn `Delivered`.
- Không gộp 2 dataset ở tầng dữ liệu thô (khác tiền tệ, khác thị trường) — chỉ so sánh ở mức KPI tổng hợp.
- Model Machine Learning dùng để xếp hạng mức độ quan trọng tương đối giữa các yếu tố, KHÔNG dùng để dự đoán chính xác giá trị từng đơn hàng trong thực tế vận hành.
- Mọi kết luận chỉ dừng ở mức tương quan (correlation), không khẳng định quan hệ nhân quả (causation).

## Thành viên nhóm

- Nguyễn Minh Hiếu
- Trần Thị Huyền Trang
