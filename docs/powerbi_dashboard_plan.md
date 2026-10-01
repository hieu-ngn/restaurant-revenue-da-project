# Power BI Dashboard Plan

## 1. Nguồn dữ liệu import vào Power BI

| File | Vào Power BI làm bảng | Dùng cho |
|---|---|---|
| `data/clean/chowdeck_clean.csv` | `Chowdeck` | Trang 1, 2 |
| `data/clean/zomato_clean.csv` | `Zomato` | Trang 3 |
| `outputs/kpi_summary/chowdeck_kpi_summary.csv` | `Chowdeck_KPI` | Trang 4 (so sánh) |
| `outputs/kpi_summary/zomato_kpi_summary.csv` | `Zomato_KPI` | Trang 4 (so sánh) |

**Cách import:** Home → Get Data → Text/CSV → chọn từng file → Load (không cần Transform gì thêm vì dữ liệu đã làm sạch sẵn ở Python).

**Lưu ý kiểu dữ liệu sau khi import** (Power BI đôi khi nhận sai kiểu):
- Cột `Order Received`, `Order Delivered`, `Order Placed At`... → đổi kiểu **Date/Time**
- Cột `revenue`, `Total`, `Sub Total`, `Bill subtotal`... → **Decimal Number**
- Cột `has_discount`, `time_sequence_valid` → **True/False**

## 2. Data Model — KHÔNG tạo quan hệ (relationship) giữa các bảng

4 bảng trên **để rời nhau, không kéo dây nối** trong tab Model — vì Chowdeck và Zomato khác thị trường/tiền tệ/cấu trúc, không có khóa chung, nối sai sẽ làm sai lệch toàn bộ số liệu (đúng nguyên tắc đã thống nhất từ đầu dự án).

## 3. Cấu trúc Dashboard — 5 trang

---

### 🔴 Trang 0: Key Drivers of Revenue (trang mở đầu — quan trọng nhất cho báo cáo)

**Mục đích:** trả lời thẳng câu hỏi trong tên đề tài — "yếu tố nào ảnh hưởng đến doanh thu" — bằng 1 trang duy nhất, không bắt người xem tự suy ra từ nhiều biểu đồ rời rạc.

**Bảng tổng hợp mức độ liên hệ (Table visual, tạo thủ công từ kết quả đã tính):**

| Yếu tố | Loại | Bằng chứng trong dữ liệu | Mức độ liên hệ | Diễn giải |
|---|---|---|---|---|
| Nhà hàng (Shop Name) | Trực tiếp | Chênh lệch doanh thu giữa các nhà hàng rất lớn (xem Trang 1) | **Mạnh** | Khác biệt vận hành/menu giữa các nhà hàng là yếu tố tách bạch rõ nhất |
| Nhóm món (Order Category) | Trực tiếp | Doanh thu chênh lệch rõ giữa Food/Drinks/Pastries | **Mạnh** | |
| Khuyến mãi (Zomato) | Gián tiếp | Tương quan 0.504 với giá trị hóa đơn; AOV giảm khi có khuyến mãi (665 vs 710 ₹) | **Trung bình** | Khuyến mãi kéo thêm đơn nhưng đổi lại AOV thấp hơn — đánh đổi rõ ràng |
| Khung giờ / Ngày trong tuần | Gián tiếp | Xem biểu đồ Trang 1 (chênh lệch theo giờ/thứ) | Tùy kết quả thực tế — điền sau khi xem chart | |
| Khu vực giao hàng | Gián tiếp | Xem biểu đồ Trang 1 | Tùy kết quả thực tế — điền sau khi xem chart | |
| Rating | Gián tiếp | Tương quan 0.05 với số đơn, 0.14 với AOV | **Rất yếu / không rõ ràng** | Dữ liệu KHÔNG ủng hộ giả thuyết "rating cao → bán chạy hơn" ở dataset này |
| Thời gian giao hàng | Gián tiếp | Tương quan 0.046 với Rating | **Rất yếu / không rõ ràng** | |
| Thời gian chuẩn bị món | Gián tiếp | Tương quan -0.017 với Rating | **Không liên quan** | |

**KPI Card nổi bật nhất trang này:** đặt số liệu ấn tượng nhất lên đầu, ví dụ "Top 3 nhà hàng chiếm X% tổng doanh thu" (tính bằng DAX, xem mục 5 bên dưới) — đây là câu mở đầu tốt cho phần thuyết trình.

**Text box bắt buộc trên trang này** (để không bị hiểu nhầm là khẳng định nhân quả):
> "Các mức độ liên hệ trên dựa trên hệ số tương quan (correlation) từ dữ liệu quan sát được, KHÔNG khẳng định quan hệ nhân quả. Yếu tố có tương quan yếu không có nghĩa là hoàn toàn không ảnh hưởng, mà nghĩa là dữ liệu hiện có chưa cho thấy bằng chứng đủ mạnh."

---

### 🟢 Trang 1: Chowdeck — Tổng quan Doanh thu

**KPI Cards (hàng trên cùng):**
| Card | Công thức DAX |
|---|---|
| Total Orders | `COUNTROWS(Chowdeck)` |
| Total Revenue | `SUM(Chowdeck[revenue])` |
| AOV (nhà hàng) | `DIVIDE([Total Revenue], [Total Orders])` |
| Rating trung bình | `AVERAGE(Chowdeck[Rating])` |

**Biểu đồ:**
| Biểu đồ | Loại | Trục/Giá trị |
|---|---|---|
| Top 10 Nhà hàng theo Doanh thu | Bar chart ngang | Axis: `Shop Name`, Value: `SUM(revenue)`, lọc Top 10 |
| Doanh thu theo Nhóm món | Donut/Bar chart | Legend: `Order Category`, Value: `SUM(revenue)` |
| Doanh thu theo Khung giờ | Line chart | Axis: `order_hour`, Value: `SUM(revenue)` |
| Doanh thu theo Thứ trong tuần | Bar chart | Axis: `order_dayofweek` (sắp xếp lại thứ tự thủ công: Sort by Column) |
| Doanh thu theo Khu vực | Bar chart hoặc Map (nếu có tọa độ) | Axis: `Delivery Location`, Value: `SUM(revenue)` |

**Slicer (bộ lọc):** `Shop Name`, `Order Category`, `Delivery Location`, `order_month`

---

### 🟢 Trang 2: Chowdeck — Rating & Thời gian giao hàng

**KPI Cards:**
| Card | Công thức DAX |
|---|---|
| Thời gian chuẩn bị TB | `AVERAGE(Chowdeck[prep_time_min])` |
| Thời gian giao hàng TB | `AVERAGE(Chowdeck[delivery_time_min])` |
| % đơn giao trễ | `DIVIDE(COUNTROWS(FILTER(Chowdeck, Chowdeck[delay_min]>0)), [Total Orders])` |
| % dữ liệu timestamp hợp lệ | `AVERAGE(Chowdeck[time_sequence_valid])` (đổi True/False → 1/0 trước) |

**Biểu đồ:**
| Biểu đồ | Loại | Trục/Giá trị |
|---|---|---|
| Rating vs Số đơn (theo nhà hàng) | Scatter chart | X: `Rating` trung bình, Y: `Số đơn`, mỗi điểm = 1 Shop Name |
| Thời gian giao hàng vs Rating | Scatter chart | X: `delivery_time_min`, Y: `Rating` |
| Phân bố độ trễ giao hàng | Histogram (dùng visual "Histogram" từ AppSource, hoặc Bar chart theo nhóm delay_min) | `delay_min` |

**Slicer:** `Shop Name`, `order_dayofweek`

---

### 🟠 Trang 3: Zomato — Tác động của Khuyến mãi

**KPI Cards:**
| Card | Công thức DAX |
|---|---|
| Total Orders (Delivered) | `CALCULATE(COUNTROWS(Zomato), Zomato[Order Status]="Delivered")` |
| Total Revenue | `CALCULATE(SUM(Zomato[Total]), Zomato[Order Status]="Delivered")` |
| AOV | `DIVIDE([Total Revenue Zomato], [Total Orders Zomato])` |
| % đơn có khuyến mãi | `CALCULATE(AVERAGE(Zomato[has_discount]), Zomato[Order Status]="Delivered")` |

**Biểu đồ:**
| Biểu đồ | Loại | Trục/Giá trị |
|---|---|---|
| AOV: Có vs Không khuyến mãi | Bar chart (chỉ lọc Delivered) | Axis: `has_discount`, Value: `AVERAGE(Total)` |
| Số đơn: Có vs Không khuyến mãi | Bar chart | Axis: `has_discount`, Value: Count |
| Khuyến mãi vs Giá trị hóa đơn gốc | Scatter chart | X: `total_discount`, Y: `Bill subtotal` |
| KPT theo Trạng thái đơn | Bar chart | Axis: `Order Status`, Value: `AVERAGE(KPT duration)` |
| Phân bố Order Status | Donut chart | Legend: `Order Status`, Value: Count (%) |

**Slicer:** `Order Status`, `order_dayofweek`, `Restaurant name`

**Lưu ý hiển thị trên trang này:** thêm 1 text box ghi chú "Rating chỉ có ở 11.7% đơn hàng — không dùng để kết luận" vì Rating quá thưa, tránh người xem hiểu nhầm nếu vô tình thêm visual liên quan Rating.

---

### 🔵 Trang 4: So sánh liên thị trường

**Bảng (Table visual)** từ `Chowdeck_KPI` + `Zomato_KPI` (Append Queries trong Power Query thành 1 bảng chung trước, đặt tên `KPI_Comparison`, vì 2 bảng KPI gốc có cột tên khác nhau — cần chuẩn hóa lại tên cột cho khớp trước khi gộp).

| Chỉ số hiển thị | Nguồn |
|---|---|
| Market | dataset/market |
| Total Orders | total_orders / total_orders_delivered |
| AOV | aov_restaurant / aov |
| % đơn có khuyến mãi | N/A (Chowdeck) / pct_orders_with_discount (Zomato) |
| % Rating có dữ liệu | 100% (Chowdeck) / pct_rating_available (Zomato) |

**Text box ghi chú bắt buộc trên trang này:** "Không so sánh số tuyệt đối Revenue/AOV giữa 2 thị trường do khác tiền tệ (₦ vs ₹). Chỉ so sánh xu hướng/tỷ lệ %."

---

## 4. Thứ tự dựng dashboard đề xuất
1. Import 4 file → chỉnh kiểu dữ liệu
2. Viết các DAX measure cơ bản trước (Total Revenue, Total Orders, AOV...) thay vì dùng trực tiếp cột — để khi thêm slicer, số liệu tự động cập nhật đúng
3. **Dựng Trang 1, 2, 3 TRƯỚC** (Chowdeck, Zomato) — vì phải xem biểu đồ thực tế mới điền được đầy đủ bảng "mức độ liên hệ" ở Trang 0 (2 dòng "Khung giờ/Ngày" và "Khu vực" đang để trống, cần xem chart xong mới kết luận được)
4. Dựng Trang 0 (Key Drivers) sau cùng, dựa trên kết quả đã thấy ở Trang 1–3
5. Dựng Trang 4 (So sánh liên thị trường)
6. Thêm Title, format màu sắc đồng bộ (gợi ý: tông xanh lá cho Chowdeck, tông cam cho Zomato)
7. **Trước khi coi là xong:** đọc lại toàn bộ text box/chú thích trên mọi trang — đảm bảo không có câu nào lỡ khẳng định nhân quả (vd tránh viết "Khuyến mãi LÀM TĂNG đơn hàng", nên viết "Đơn có khuyến mãi ghi nhận số lượng nhiều hơn")

## 5. DAX measure gợi ý cho Trang 0 (Top nhà hàng chiếm bao nhiêu % doanh thu)

```dax
Revenue Top3 Shops =
CALCULATE(
    [Total Revenue],
    TOPN(3, ALL(Chowdeck[Shop Name]), CALCULATE([Total Revenue]), DESC)
)

% Revenue Top3 Shops = DIVIDE([Revenue Top3 Shops], [Total Revenue])
```
Đây là loại số liệu "gây ấn tượng" tốt để mở đầu phần thuyết trình — ví dụ nếu ra 45%, câu mở đầu có thể là: "45% doanh thu chỉ đến từ 3/25 nhà hàng — đây là dấu hiệu cho thấy [X, Y, Z] là yếu tố phân hóa mạnh nhất."
