# Key Insights

> **Nguyên tắc đọc tài liệu này:** mọi con số đều tính từ `data/clean/chowdeck_clean.csv` và `data/clean/zomato_clean.csv`. Tất cả kết quả chỉ là **mối liên hệ (correlation)** trong dữ liệu quan sát, không khẳng định quan hệ nhân quả. Hai dataset khác thị trường và khác tiền tệ (₦ và ₹) nên **không cộng hay so sánh số tuyệt đối** giữa chúng.

**Phạm vi:** Chowdeck = 3.061 đơn (Food, Drinks & Beverages, Pastries), Revenue = `Sub Total`. Zomato = 21.131 đơn `Delivered`, Revenue = `Total`.

---

## 1. Tóm tắt: yếu tố nào có liên hệ với doanh thu?

Doanh thu = Số đơn × AOV. Nhóm yếu tố được phân loại theo cách chúng tác động tới công thức này.

| Yếu tố | Loại | Kết quả | Mức tin cậy |
|---|---|---|---|
| Giá món × Số lượng | **Trực tiếp** (cấu thành AOV) | Giải thích ≈ 89% biến thiên giá trị đơn Chowdeck (gần như là định nghĩa) | Rất cao, nhưng hiển nhiên |
| Số đơn | **Trực tiếp** | Số đơn mỗi nhóm món và mỗi shop gần bằng nhau, nên không phải nguồn chênh lệch giữa các nhóm | Cao |
| Nhóm món | Gián tiếp (qua giá/AOV) | Yếu tố duy nhất khác biệt rõ (p < 0,001), nhưng chỉ giải thích ≈ 9% | Cao |
| Nhà hàng | Gián tiếp | **Không** khác nhau trong cùng nhóm món (p = 0,67–0,70) | Cao |
| Rating | Gián tiếp | Hầu như không liên hệ (Chowdeck r = 0,05–0,14 cấp shop; Zomato r = 0,06 cấp đơn, nhưng chỉ 11,8% đơn có rating) | Trung bình |
| Khu vực, thứ, khung giờ (Chowdeck) | Gián tiếp | Không có khác biệt đáng kể (p = 0,55; 0,50; 0,56), kể cả sau khi kiểm soát nhóm món (p > 0,6) | Cao |
| Khuyến mãi (Zomato) | Gián tiếp / ảnh hưởng **lợi nhuận** | Đi cùng hóa đơn gốc lớn hơn nhưng số tiền khách trả mỗi đơn thấp hơn; chưa xác định được nhân quả | Thấp–Trung bình |
| Thời gian chuẩn bị, giao hàng | Gián tiếp / ảnh hưởng **lợi nhuận và trải nghiệm** | Hóa đơn lớn đi cùng thời gian chuẩn bị lâu hơn (r = 0,38); chưa có bằng chứng ảnh hưởng doanh thu | Trung bình |
| Chi phí, biên lợi nhuận | Lợi nhuận | **Không có dữ liệu** nên không đánh giá được | , |

**Thông điệp chính:** trong dữ liệu có sẵn, doanh thu chủ yếu do **giá trị mỗi đơn (giá món × số lượng)** quyết định. Các yếu tố ngữ cảnh (nhà hàng, khu vực, giờ, thứ, rating) hầu như không giải thích thêm được điều gì.

---

## 2. Chowdeck (Nigeria)

### Insight 1: Doanh thu giảm 2023→2024 rồi hồi nhẹ; cả số đơn và AOV cùng đóng góp
| Năm | Số đơn | AOV (₦) | Doanh thu (₦) |
|---|---|---|---|
| 2023 | 1.067 | 8.473 | 9.041.000 |
| 2024 | 983 | 8.032 | 7.895.500 |
| 2025 | 1.011 | 8.199 | 8.289.500 |

- 2023→2024: doanh thu −12,7% (số đơn −7,9%, AOV −5,2%). 2024→2025: +5,0% (số đơn +2,8%, AOV +2,1%).
- **Thận trọng:** khác biệt giá trị đơn giữa các năm **không có ý nghĩa thống kê** (p = 0,44). Biến động này có thể chỉ là dao động ngẫu nhiên, không nên kể thành một "xu hướng".

### Insight 2: Chênh lệch giữa các nhóm món đến từ AOV, không phải số đơn
| Nhóm món | Số đơn | AOV (₦) | Tỷ trọng doanh thu |
|---|---|---|---|
| Food | 985 | 11.040 | 43,1% |
| Pastries | 1.025 | 8.605 | 35,0% |
| Drinks & Beverages | 1.051 | 5.263 | 21,9% |

- Drinks có **nhiều đơn nhất** nhưng doanh thu thấp nhất; Food có ít đơn nhất nhưng doanh thu cao nhất.
- Nhóm món giải thích ≈ 9% biến thiên giá trị đơn, tức phần lớn biến thiên còn lại nằm ở giá từng món và số lượng, không phải ở các yếu tố ngữ cảnh trong dữ liệu.

### Insight 3: Giữa các nhà hàng cùng nhóm món gần như không có khác biệt
- Trong từng nhóm, ANOVA giữa các shop cho p = 0,67 (Food), 0,70 (Drinks), 0,69 (Pastries). Thêm `Shop Name` vào mô hình sau khi đã có nhóm món chỉ tăng R² từ 9,0% lên 9,2%.
- Doanh thu cấp shop tương quan 0,98 với AOV của shop và **−0,26 với số đơn**: shop xếp trên do bán món đắt hơn, không phải do bán nhiều đơn hơn.
- Mô tả (không có ý nghĩa thống kê): trong Pastries, Sunrise Bakery thấp nhất (₦1,41 triệu, 182 đơn, AOV ₦7.720).

### Insight 4: Rating, khu vực, giờ và thứ không liên hệ rõ với giá trị đơn
- Mỗi yếu tố riêng lẻ giải thích dưới 1% biến thiên giá trị đơn (khu vực 0,3%, thứ 0,2%, giờ 0,7%, Rating ≈ 0%).
- Số đơn theo 4 khung giờ (0–5h, 6–11h, 12–17h, 18–23h) khá đều: 745, 740, 799, 777 đơn.

### Insight 5: Vận hành, nhưng cần dữ liệu đáng tin hơn
- Thời gian chuẩn bị trung bình ≈ 10,5 phút; thời gian giao ≈ 61,3 phút (tính trên đơn timestamp hợp lệ).
- **≈ 28% đơn (870/3.061) có timestamp sai thứ tự.** Ở nhóm này `delay_min` bằng đúng 0 ở 99,4% dòng (giờ giao trùng giờ dự kiến), nên không phản ánh độ trễ thật. Các KPI độ trễ cũ (42,7% đơn trễ, trễ trung bình 3,95 phút) bị **pha loãng** bởi nhóm này.
- **Trên đơn có timestamp hợp lệ (2.191 đơn): 59,6% giao sau thời điểm dự kiến, trễ trung bình 5,5 phút (trung vị 3 phút).** Đây là con số nên dùng.
- Trên đơn hợp lệ, tương quan của thời gian giao, thời gian chuẩn bị và độ trễ với Rating đều gần 0 (0,02; −0,02; 0,06).
- **Bất thường cần kiểm tra:** trong các đơn có timestamp hợp lệ, đơn giao trễ lại có Rating **cao hơn** (4,10) đơn không trễ (3,82). Điều này trái trực giác nên **không dùng làm insight**; có thể do cách tính `delay_min` hoặc do dữ liệu mô phỏng.

### Insight 6: Doanh thu tập trung vào một nhóm nhỏ tài khoản
- 181 tài khoản; nhóm 10% cao nhất (18 tài khoản) tạo ra **42,5% doanh thu**. Trung vị mỗi tài khoản có 11 đơn.
- Chỉ là mô tả; dataset không có ngày đăng ký nên không phân tích được khách mới và khách quay lại.

---

## 3. Zomato (Delhi NCR)

### Insight 7: Số liệu tổng bị chi phối bởi một nhà hàng
- Chỉ 6 nhà hàng. **Aura Pizzas** chiếm 68,2% số đơn và 73,8% doanh thu. KPI tổng chủ yếu phản ánh Aura, và kết luận khó khái quát cho "nhà hàng trên nền tảng" nói chung.

### Insight 8: Khuyến mãi đi cùng hóa đơn lớn hơn nhưng khách trả ít hơn mỗi đơn
- 61,1% đơn có khuyến mãi. Số tiền khách trả (AOV theo `Total`): ₹665 (có khuyến mãi) so với ₹710 (không), thấp hơn ≈ 6,3%.
- Hóa đơn gốc (`Bill subtotal`) của đơn có khuyến mãi lại **cao hơn**: ₹797 so với ₹676. Xét riêng từng nhà hàng, chiều này đúng ở 4 trong 5 nhà hàng có cả hai nhóm (Aura 863 vs 709; Swaad 680 vs 570; Dilli Burger Adda 607 vs 510; Chicken Junction 451 vs 388); Masala Junction ngược lại (342 vs 368).
- **Chiều nhân quả chưa xác định:** có thể khuyến mãi khiến khách thêm món, hoặc ngược lại hóa đơn lớn mới đủ điều kiện được giảm giá. Không có nhóm đối chứng hay dữ liệu trước/sau nên **không kết luận được khuyến mãi tạo thêm đơn**.

### Insight 9: Cao điểm buổi tối, và khuyến mãi ít hơn vào giờ cao điểm
- 18–21h: 9.183 đơn (43,5% tổng), AOV cao nhất (₹734). Tỷ lệ đơn có khuyến mãi ở khung này thấp nhất (56%), trong khi 0–5h là 73%.
- Mô tả: nhu cầu giờ tối cao dù tỷ lệ khuyến mãi thấp hơn. Chưa có bằng chứng khuyến mãi là lý do tạo ra khác biệt giữa các khung giờ.

### Insight 10: Hóa đơn lớn đi cùng bếp chuẩn bị lâu hơn
- Thời gian chuẩn bị (KPT) tương quan 0,38 với giá trị hóa đơn gốc, thời gian tài xế chờ 0,19, khoảng cách 0,11. KPT là yếu tố quan trọng nhất trong model ML (50,4%).
- Đây là **hệ quả vận hành** (đơn lớn nấu lâu hơn), không phải nguyên nhân tạo doanh thu.

### Insight 11: Đơn giao thành công gần như tuyệt đối, và Rating quá thưa để kết luận
- 99,1% đơn `Delivered`; 0,74% bị `Rejected`.
- Chỉ 11,8% đơn có Rating (trung bình 4,36), tương quan 0,06 với hóa đơn. Mẫu quá thưa để rút ra kết luận.
- Đơn bị từ chối (`Rejected`) có thời gian chuẩn bị trung bình 15,5 phút (chỉ 61 đơn có dữ liệu KPT), **không dài hơn** đơn `Delivered` (17,3 phút). Không có bằng chứng bếp chậm đi cùng việc đơn bị từ chối, nhưng mẫu nhỏ.
- 33,4% khách hàng đặt từ 2 đơn trở lên trong 5 tháng; nhóm 10% khách chi nhiều nhất tạo 37% doanh thu.

---

## 4. Những điều dữ liệu KHÔNG cho phép kết luận

- Khuyến mãi có tạo thêm đơn hay không (thiếu nhóm đối chứng).
- Yếu tố nào ảnh hưởng đến **lợi nhuận** (thiếu dữ liệu chi phí, hoa hồng, chi phí khuyến mãi).
- Tác động của thời gian giao hàng lên Rating hoặc doanh thu (timestamp Chowdeck lỗi ≈ 28% và có kết quả bất thường).
- Tác động của số lượng review (không có cột này).
- Khách mới so với khách quay lại ở Chowdeck (không có ngày đăng ký).
- Kết luận chung cho các nhà hàng khác: Chowdeck chỉ có 15 shop, Zomato chỉ 6 nhà hàng trong 5 tháng.
- Rating Chowdeck chỉ có 5 mức (3,0–5,0) và dữ liệu có dấu hiệu có thể là mô phỏng, nên cần thận trọng khi diễn giải mọi kết quả.

## 5. File liên quan
`docs/recommendations.md`, `docs/kpi_definitions.md`, `docs/ml_summary.md`, `outputs/kpi_summary/`.
