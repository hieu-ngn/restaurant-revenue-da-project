# KPI Definitions

Công thức trọng tâm xuyên suốt dự án:

```
Revenue = Number of Orders × AOV
AOV = Total Revenue / Total Orders
```

---

## A. KPI cho Chowdeck (dataset chính)

| #  | KPI                                              | Công thức                                                             | Cột dữ liệu dùng                             | Ghi chú                                                                                                                                                         |
| -- | ------------------------------------------------ | ----------------------------------------------------------------------- | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1  | **Total Orders**                           | Đếm số dòng                                                         | `revenue` (đếm count)                        | Đã lọc chỉ còn Food/Drinks & Beverages/Pastries                                                                                                             |
| 2  | **Total Revenue (nhà hàng)**             | `Σ Sub Total`                                                        | `revenue` (= Sub Total)                        | Doanh thu thực của nhà hàng, KHÔNG gồm phí ship/dịch vụ                                                                                                 |
| 3  | **AOV (nhà hàng)**                       | Total Revenue / Total Orders                                            | `revenue`                                      | Dùng cho công thức Revenue = Orders × AOV                                                                                                                    |
| 4  | **AOV (khách hàng)**                     | `mean(Total)`                                                         | `Total`                                        | Số tiền khách thực trả trung bình/đơn (gồm phí) — dùng riêng khi phân tích trải nghiệm khách hàng, KHÔNG dùng để tính Revenue nhà hàng |
| 5  | **Revenue theo Nhà hàng**                | `groupby(Shop Name)['revenue'].sum()`                                 | `Shop Name`, `revenue`                       | Trả lời BQ#1                                                                                                                                                   |
| 6  | **Revenue theo Nhóm món**                | `groupby(Order Category)['revenue'].sum()`                            | `Order Category`, `revenue`                  | Trả lời BQ#2                                                                                                                                                   |
| 7  | **Revenue theo Khu vực**                  | `groupby(Delivery Location)['revenue'].sum()`                         | `Delivery Location`, `revenue`               | Trả lời BQ#5                                                                                                                                                   |
| 8  | **Revenue theo Giờ/Ngày**                | `groupby(order_hour / order_dayofweek)['revenue'].sum()`              | `order_hour`, `order_dayofweek`, `revenue` | Trả lời BQ#6                                                                                                                                                   |
| 9  | **Rating trung bình**                     | `mean(Rating)` — tính chung hoặc theo nhóm (nhà hàng, category) | `Rating`                                       |                                                                                                                                                                  |
| 10 | **Thời gian chuẩn bị món (Prep Time)** | `mean(prep_time_min)`                                                 | `prep_time_min`                                | = Order Ready − Preparing Order                                                                                                                                 |
| 11 | **Thời gian giao hàng (Delivery Time)**  | `mean(delivery_time_min)`                                             | `delivery_time_min`                            | = Order Delivered − Order Received                                                                                                                              |
| 12 | **Độ trễ giao hàng (Delay)**           | `mean(delay_min)`, và `% đơn có delay_min > 0`                  | `delay_min`                                    | delay_min dương = giao trễ so với dự kiến                                                                                                                  |
| 13 | **Tỷ lệ dữ liệu timestamp hợp lệ**   | `% time_sequence_valid = True`                                        | `time_sequence_valid`                          | Chỉ số chất lượng dữ liệu — 71% hợp lệ, cần nêu rõ giới hạn                                                                                       |

---

## B. KPI cho Zomato (case study: Khuyến mãi)

> **Lưu ý quan trọng:** Toàn bộ KPI Revenue/AOV dưới đây chỉ tính trên đơn có `Order Status = "Delivered"` (loại bỏ đơn hủy/từ chối, theo xác nhận đã chốt ở Bước 4).

| #  | KPI                                                  | Công thức                                                        | Cột dữ liệu dùng        | Ghi chú                                                                                                                                                                                                                                                                                          |
| -- | ---------------------------------------------------- | ------------------------------------------------------------------ | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1  | **Total Orders (Delivered)**                   | Đếm dòng có`Order Status == 'Delivered'`                     | `Order Status`            |                                                                                                                                                                                                                                                                                                   |
| 2  | **Total Revenue**                              | `Σ Total` (đơn Delivered)                                     | `Total`                   | `Total` ở Zomato là số tiền khách trả **sau** khuyến mãi — dùng làm proxy cho doanh thu; giới hạn: một phần khuyến mãi có thể do nền tảng (Zomato) tài trợ chứ không phải nhà hàng tự chịu, nên đây là ước lượng, không phải số chính xác 100% |
| 3  | **AOV**                                        | Total Revenue / Total Orders (Delivered)                           | `Total`                   |                                                                                                                                                                                                                                                                                                   |
| 4  | **Tỷ lệ đơn có khuyến mãi**             | `% has_discount == True` (đơn Delivered)                       | `has_discount`            | Trả lời BQ#7                                                                                                                                                                                                                                                                                    |
| 5  | **AOV theo có/không khuyến mãi**           | `groupby(has_discount)['Total'].mean()`                          | `has_discount`, `Total` | Trả lời BQ#8                                                                                                                                                                                                                                                                                    |
| 6  | **Tổng khuyến mãi trung bình/đơn**       | `mean(total_discount)`                                           | `total_discount`          |                                                                                                                                                                                                                                                                                                   |
| 7  | **Tương quan Khuyến mãi vs Bill subtotal** | `corr(total_discount, Bill subtotal)`                            |                             | Đo mức độ khuyến mãi "ăn theo" giá trị đơn                                                                                                                                                                                                                                             |
| 8  | **Thời gian chuẩn bị món (KPT)**           | `mean(KPT duration (minutes))`, theo `Order Status`            | `KPT duration (minutes)`  | Trả lời BQ#9                                                                                                                                                                                                                                                                                    |
| 9  | **Tỷ lệ đơn theo trạng thái**            | `value_counts(Order Status, normalize=True)`                     | `Order Status`            | % Delivered, Rejected, Returned, Timed out                                                                                                                                                                                                                                                        |
| 10 | **Rating trung bình (có giới hạn)**        | `mean(Rating)` chỉ trên subset `df_rating` (11.7% dữ liệu) | `Rating`                  | **Không dùng để kết luận mạnh** — nêu rõ cỡ mẫu nhỏ                                                                                                                                                                                                                            |

---

## C. Bảng KPI so sánh liên thị trường (dùng ở Power BI trang tổng hợp)

File: `outputs/kpi_summary/chowdeck_kpi_summary.csv` + `zomato_kpi_summary.csv` — đã được 2 notebook tự động tính và xuất sẵn.

| Chỉ số                 | Chowdeck                   | Zomato               |
| ------------------------ | -------------------------- | -------------------- |
| Market                   | Nigeria                    | India (Delhi NCR)    |
| Total Orders             | (xem file summary)         | (xem file summary)   |
| Total Revenue            | ₦ ...                     | ₹ ...               |
| AOV                      | ₦ ...                     | ₹ ...               |
| % đơn có khuyến mãi | N/A (không có dữ liệu) | ... %                |
| Rating trung bình       | đầy đủ                 | chỉ 11.7% dữ liệu |

**Không so sánh số tuyệt đối Revenue/AOV giữa 2 thị trường** (khác tiền tệ, khác sức mua) — chỉ so sánh **xu hướng/tỷ lệ %** (vd: tỷ lệ đơn có khuyến mãi, chiều tương quan Rating-Orders...).
