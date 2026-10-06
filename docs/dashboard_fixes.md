# Hướng dẫn sửa dashboard Power BI

> File `.pbix` là file nhị phân nên không thể sửa từ bên ngoài. Các bước dưới đây cần làm trực tiếp trong Power BI Desktop. Tên bảng/cột trong DAX (`chowdeck_clean`, `zomato_clean`...) là **giả định**, hãy đổi cho khớp với data model thực tế của bạn.

---

## A. Sửa bảng "Key Drivers of Revenue" (nội dung)

Các số liệu bên dưới đã được kiểm tra lại trên `data/clean/chowdeck_clean.csv` và `zomato_clean.csv`. Hai hàng **Khu vực** và **Khung giờ / Ngày** đang ghi sai so với dữ liệu.

| Yếu tố | Loại | Mức độ liên hệ | Bằng chứng trong dữ liệu | Diễn giải |
|---|---|---|---|---|
| Rating | Gián tiếp | Rất yếu / Không rõ ràng | Tương quan cấp nhà hàng: 0,05 với số đơn, 0,14 với AOV | Dữ liệu không ủng hộ giả thuyết "rating cao → bán chạy hơn" ở dataset này |
| Khung giờ / Ngày trong tuần | Gián tiếp | **Không có bằng chứng rõ ràng** | Khác biệt giá trị đơn giữa các giờ (ANOVA p = 0,56) và giữa các thứ (p = 0,50) không có ý nghĩa thống kê; kiểm soát nhóm món vẫn p > 0,6 | Dao động giữa các giờ/thứ nằm trong mức biến động ngẫu nhiên; chưa đủ cơ sở kết luận có "đỉnh doanh thu" hay ngày nào nhỉnh hơn |
| Khu vực giao hàng | Gián tiếp | **Không có bằng chứng rõ ràng** | ANOVA p = 0,55; khu vực cao nhất chỉ gấp ≈ 1,2 lần khu vực thấp nhất; không khác biệt trong từng nhóm món (p > 0,19) | Chênh lệch giữa các khu vực chưa vượt quá mức dao động ngẫu nhiên |
| Nhà hàng (Shop Name) | Gián tiếp (qua giá/AOV) | **Yếu khi đã kiểm soát nhóm món** | Trong từng nhóm món, các shop không khác nhau về giá trị đơn (ANOVA p = 0,67 Food; 0,70 Drinks; 0,69 Pastries); thêm Shop Name vào mô hình chỉ tăng R² từ 9,0% lên 9,2% | Chênh lệch doanh thu giữa các shop chủ yếu do mỗi shop thuộc một nhóm món khác nhau. Bản cũ ghi "Mạnh" là sai (p < 0,001 trước đó chỉ phản ánh hiệu ứng nhóm món) |
| Nhóm món (Order Category) | Gián tiếp (qua giá/AOV) | Mạnh nhất trong các yếu tố có sẵn (nhưng chỉ giải thích ≈ 9% biến thiên giá trị đơn) | Số đơn mỗi nhóm gần bằng nhau (985–1.051) nhưng AOV khác xa: Food ₦11.040, Pastries ₦8.605, Drinks ₦5.263; Food chiếm 43% doanh thu | Chênh lệch doanh thu giữa các nhóm đến chủ yếu từ AOV, không phải số đơn |
| Khuyến mãi (Zomato) | Gián tiếp | Có liên hệ, chưa rõ nhân quả | 61,1% đơn có khuyến mãi; AOV thực nhận ₹665 so với ₹710; hóa đơn gốc trung bình ₹797 so với ₹676 | Đơn có khuyến mãi đi cùng hóa đơn gốc lớn hơn nhưng doanh thu thực nhận mỗi đơn thấp hơn. Chưa thể kết luận khuyến mãi tạo thêm đơn vì không có nhóm đối chứng; tương quan 0,50 giữa tiền giảm và hóa đơn một phần mang tính cơ học |

**Gỡ bỏ** các câu (và sửa dòng "Nhà hàng = Mạnh" như bảng trên): "Khuyến mãi kéo thêm đơn", "Food áp đảo hoàn toàn", "các khu vực top đầu (Ikeja, Mushin) áp đảo", "nhỉnh hơn vào Thứ Tư, Thứ Năm".

Lưu ý về phân loại: trong khung bài của bạn, yếu tố **trực tiếp** là Số đơn, AOV, giá món. Nhóm món và nhà hàng tác động đến doanh thu **thông qua** giá/AOV nên nên xếp là gián tiếp.

---

## B. Sửa lỗi biểu đồ

### B1. "Sum of ..." → Average hoặc Don't summarize

Các biểu đồ đang dùng `Sum of Rating`, `Sum of order_hour`, `Sum of delivery_time_min`, `Sum of delay_min`, `Sum of Quantity`.

1. Chọn biểu đồ, mở ngăn **Visualizations**.
2. Ở ô chứa trường (Values / Y axis / X axis), bấm mũi tên cạnh tên trường.
3. Chọn:
   - **Average** cho Rating, thời gian giao, thời gian chuẩn bị, độ trễ.
   - **Don't summarize** cho `order_hour` khi dùng làm **trục** (đây là hạng mục, không phải giá trị cần cộng). Nếu vẫn bị cộng, chọn cột → **Column tools** → đổi **Summarization** thành *Don't summarize*.
4. Với scatter "Rating vs Số đơn": đặt **Details** = `Shop Name`, **X** = Count of Order (số đơn), **Y** = Average of Rating.

### B2. Thẻ KPI hiển thị `1`, `0.43`, `0.26`

Chọn thẻ/measure → **Measure tools** → **Format: Percentage** → 1 chữ số thập phân. Ví dụ measure (đổi tên bảng cho đúng):

```DAX
% Timestamp hợp lệ =
DIVIDE(
    COUNTROWS(FILTER(chowdeck_clean, chowdeck_clean[time_sequence_valid] = TRUE())),
    COUNTROWS(chowdeck_clean)
)

% Đơn có khuyến mãi =
DIVIDE(
    COUNTROWS(FILTER(zomato_clean, zomato_clean[has_discount] = TRUE())),
    COUNTROWS(zomato_clean)
)
```

Giá trị đúng phải ra: **71,6%** (timestamp hợp lệ), **61,1%** (đơn có khuyến mãi), **42,7%** (đơn giao trễ), **26%** (tỷ trọng top 3 shop).

### B3. Thẻ "Rating trung bình = 3,92" khác dữ liệu (3,897)

Tôi đã thử các cách tính (toàn bộ 3.061 đơn: **3,897**; toàn bộ 5.000 đơn gốc: 3,900; chỉ đơn có timestamp hợp lệ: 3,991) và **không cách nào ra 3,92**. Cách tìm nguyên nhân:

1. Chọn thẻ → mở **Filters**, kiểm tra filter ở cấp visual, page và report.
2. Kiểm tra measure đang dùng `AVERAGE(chowdeck_clean[Rating])` hay đang trung bình của một measure khác.
3. Kiểm tra bảng nạp vào Power BI là `chowdeck_clean.csv` (3.061 dòng), không phải bản khác.

Với dữ liệu hiện tại, thẻ phải hiển thị **3,90** (3,897).

> Quan sát thêm: nhóm đơn có timestamp không hợp lệ (29%) có Rating trung bình thấp hơn đáng kể (3,66 so với 3,99). Khi diễn giải Rating và thời gian giao hàng, nên nêu rõ tập dữ liệu nào đang được dùng.

### B4. Trang "So sánh liên thị trường": dòng Total `Sum of AOV = 8.923,67`

Dòng này cộng AOV của ₦ (Nigeria) và ₹ (Ấn Độ), vô nghĩa và mâu thuẫn với ghi chú "không so sánh số tuyệt đối". Cách sửa: chọn bảng → **Format → Cell elements/Totals** → tắt **Row totals**. Chỉ giữ so sánh tỷ lệ % (tỷ lệ đơn trễ, tỷ lệ có khuyến mãi, tỷ lệ thành công...), không so sánh số tuyệt đối khác đơn vị tiền.

### B5. Thêm ghi chú phạm vi lọc (trang Chowdeck)

Thêm text box: *"Chowdeck: chỉ gồm nhóm Food, Drinks & Beverages, Pastries (đã loại Groceries và Medications). Revenue = Sub Total."*

---

## C. Nên bổ sung (vì đề tài nói về `Revenue = Orders × AOV`)

1. **Biểu đồ doanh thu theo thời gian** (line chart theo tháng hoặc quý, trục X = Year-Month dạng *Don't summarize*).
2. **Phân rã Orders × AOV theo năm**, ví dụ bảng/combo chart gồm Số đơn, AOV, Doanh thu theo `order_year`. Tham khảo số liệu thật (Chowdeck, đã lọc): doanh thu 2023 ≈ ₦9,04 triệu, 2024 ≈ ₦7,90 triệu, 2025 ≈ ₦8,29 triệu, số đơn mỗi năm khoảng 1.000.

```DAX
Total Orders = COUNTROWS(chowdeck_clean)
Total Revenue = SUM(chowdeck_clean[Sub Total])
AOV = DIVIDE([Total Revenue], [Total Orders])
```

## D. Checklist

- [ ] Sửa bảng Key Drivers (mục A)
- [ ] Đổi Sum → Average / Don't summarize (B1)
- [ ] Định dạng % cho các thẻ KPI (B2)
- [ ] Kiểm tra thẻ Rating = 3,90 (B3)
- [ ] Tắt dòng Total ở trang so sánh (B4)
- [ ] Thêm text box phạm vi lọc (B5)
- [ ] Thêm biểu đồ xu hướng và phân rã Orders × AOV (C)
- [ ] Xuất lại PDF và ảnh chụp, chép vào `powerbi/`
