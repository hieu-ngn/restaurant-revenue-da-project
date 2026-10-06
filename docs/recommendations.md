# Business Recommendations

> **Đọc trước:** các đề xuất dưới đây dựa trên mối liên hệ (correlation) trong `docs/key_insights.md`, không dựa trên bằng chứng nhân quả. Vì vậy mỗi đề xuất được ghi rõ là **hành động nên làm ngay**, **giả thuyết cần thử nghiệm** hay **dữ liệu cần thu thập**. Đối tượng: chủ nhà hàng và quản lý vận hành trên nền tảng giao đồ ăn.

## Tổng quan

| # | Đề xuất | Dựa trên | Loại | Ưu tiên |
|---|---|---|---|---|
| 1 | Tăng giá trị mỗi đơn (combo, bán kèm) thay vì tăng số đơn ở nhóm AOV thấp | Insight 2 | Giả thuyết cần thử nghiệm | Cao |
| 2 | Theo dõi hằng tháng cấu phần Orders × AOV | Insight 1 | Hành động ngay | Cao |
| 3 | Thử nghiệm có đối chứng trước khi mở rộng khuyến mãi | Insight 8, 9 | Giả thuyết cần thử nghiệm | Cao |
| 4 | Chuẩn bị năng lực bếp cho khung 18–21h | Insight 9, 10 | Hành động ngay | Trung bình |
| 5 | Chăm sóc nhóm khách chi tiêu cao | Insight 6, 11 | Giả thuyết cần thử nghiệm | Trung bình |
| 6 | Không đầu tư theo khu vực, giờ hay Rating khi chưa có thêm dữ liệu | Insight 3, 4 | Hành động ngay (tránh lãng phí) | Trung bình |
| 7 | Giảm phụ thuộc vào một nhà hàng chủ lực | Insight 7 | Quản trị rủi ro | Thấp–Trung bình |
| 8 | Cải thiện chất lượng dữ liệu | Insight 5, 11 | Dữ liệu cần thu thập | Cao |

---

## Chi tiết

### 1. Tăng giá trị mỗi đơn ở nhóm AOV thấp *(giả thuyết cần thử nghiệm)*
- **Căn cứ:** số đơn giữa 3 nhóm món gần bằng nhau (985–1.051), nhưng AOV chênh nhau tới 2,1 lần (Food ₦11.040, Drinks ₦5.263). Doanh thu mỗi đơn gần như hoàn toàn do giá món × số lượng quyết định.
- **Hành động đề xuất:** thử combo đồ uống + bánh, mức "mua kèm" gợi ý khi đặt Drinks, hoặc ngưỡng giá trị đơn tối thiểu để được ưu đãi.
- **Cách đo:** so AOV, tỷ lệ đơn có từ 2 món trở lên và doanh thu trên mỗi 100 đơn giữa nhóm thử nghiệm và nhóm đối chứng trong ít nhất 4 tuần.
- **Giới hạn:** dữ liệu chỉ cho thấy nhóm món khác nhau về AOV, không cho biết khách có sẵn sàng mua thêm hay không. Cần thử nghiệm để biết.

### 2. Theo dõi Orders × AOV hằng tháng *(hành động ngay)*
- **Căn cứ:** doanh thu Chowdeck giảm 12,7% từ 2023 sang 2024 (số đơn −7,9%, AOV −5,2%) rồi hồi 5,0% năm 2025, nhưng chênh lệch giữa các năm chưa có ý nghĩa thống kê (p = 0,44).
- **Hành động:** thêm vào dashboard biểu đồ doanh thu theo tháng cùng phần phân rã Orders và AOV; đặt ngưỡng cảnh báo khi cả hai cùng giảm.
- **Giới hạn:** không có dữ liệu về thay đổi giá, chiến dịch hay mùa vụ để giải thích nguyên nhân.

### 3. Thử nghiệm khuyến mãi có đối chứng trước khi mở rộng *(giả thuyết cần thử nghiệm)*
- **Căn cứ (Zomato):** 61,1% đơn có khuyến mãi; mỗi đơn có khuyến mãi khách trả trung bình thấp hơn khoảng 6,3% (₹665 so với ₹710), dù hóa đơn gốc lớn hơn (₹797 so với ₹676).
- **Hành động:** thay vì áp khuyến mãi đại trà, chạy thử nghiệm A/B hoặc chia theo thời gian (có và không khuyến mãi cùng khung giờ, cùng món). Đo **số đơn tăng thêm** và **lợi nhuận trên mỗi đơn**, không chỉ doanh thu.
- **Giới hạn:** không có nhóm đối chứng nên chưa biết khuyến mãi tạo thêm đơn hay chỉ giảm giá cho khách vốn đã mua. Không có dữ liệu chi phí, nên không biết khuyến mãi lãi hay lỗ.

### 4. Chuẩn bị năng lực bếp cho khung 18–21h *(hành động ngay)*
- **Căn cứ:** 43,5% số đơn Zomato rơi vào 18–21h với AOV cao nhất (₹734); hóa đơn lớn đi cùng thời gian chuẩn bị lâu hơn (r = 0,38).
- **Hành động:** bố trí nhân sự, chuẩn bị nguyên liệu trước giờ cao điểm; theo dõi KPT theo từng khung giờ.
- **Giới hạn:** chưa chứng minh được KPT chậm làm mất đơn hay giảm Rating.

### 5. Chăm sóc nhóm khách chi tiêu cao *(giả thuyết cần thử nghiệm)*
- **Căn cứ:** Chowdeck: 10% tài khoản cao nhất tạo 42,5% doanh thu. Zomato: 10% khách cao nhất tạo 37% doanh thu; 33,4% khách đặt từ 2 đơn trở lên.
- **Hành động:** thử chương trình ưu đãi cho khách đặt thường xuyên (tích điểm, ưu đãi theo số đơn) và đo tỷ lệ quay lại.
- **Giới hạn:** doanh thu tập trung cũng là rủi ro, nếu mất vài khách lớn thì doanh thu giảm rõ. Account Chowdeck có thể là dữ liệu mô phỏng.

### 6. Không đầu tư theo khu vực, giờ hay Rating khi chưa có thêm dữ liệu *(tránh lãng phí)*
- **Căn cứ:** sau khi kiểm soát nhóm món, khu vực, thứ, khung giờ và Rating đều không liên hệ với giá trị đơn (p > 0,6); mỗi yếu tố giải thích dưới 1% biến thiên.
- **Hành động:** không dồn ngân sách quảng cáo theo khu vực/giờ hay theo đuổi tăng Rating **với mục tiêu tăng doanh thu** chỉ dựa trên dữ liệu này.
- **Giới hạn:** "không thấy liên hệ" khác với "không có tác động". Rating vẫn có thể quan trọng cho uy tín dài hạn, chỉ là dataset này không cho thấy.

### 7. Giảm phụ thuộc vào một nhà hàng chủ lực *(quản trị rủi ro)*
- **Căn cứ:** Aura Pizzas chiếm 68,2% số đơn và 73,8% doanh thu Zomato.
- **Hành động:** theo dõi tỷ trọng doanh thu top 1 và top 3 trên dashboard; nếu là nền tảng, hỗ trợ nhà hàng nhỏ.
- **Giới hạn:** chỉ 6 nhà hàng trong 5 tháng, chưa rõ có điển hình hay không.

### 8. Cải thiện chất lượng dữ liệu *(dữ liệu cần thu thập)*
| Thiếu gì | Vì sao quan trọng |
|---|---|
| Timestamp đúng thứ tự (Chowdeck lỗi 29%) | Phân tích thời gian giao hàng và độ trễ đáng tin cậy |
| Rating cho nhiều đơn hơn (Zomato chỉ 11,8%) | Đánh giá được mối liên hệ Rating và doanh thu |
| Chi phí, hoa hồng, chi phí khuyến mãi | Chuyển từ phân tích doanh thu sang **lợi nhuận** |
| Nhóm đối chứng và thông tin chiến dịch | Đánh giá nhân quả của khuyến mãi |
| Ngày đăng ký khách hàng | Phân biệt khách mới và khách quay lại |
| Số lượng review | Đúng với phạm vi đề tài ban đầu nhưng dataset không có |

---

## Thứ tự triển khai gợi ý
1. **Ngay:** đề xuất 2 (theo dõi Orders × AOV) và 8 (làm sạch dữ liệu).
2. **Thử nghiệm 4–8 tuần:** đề xuất 1 và 3, kèm đo lợi nhuận.
3. **Vận hành:** đề xuất 4, 5, 7.

## File liên quan
`docs/key_insights.md`, `docs/kpi_definitions.md`, `docs/dashboard_fixes.md`.
