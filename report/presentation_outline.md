# Outline thuyết trình

**Đề tài:** Analysis of Factors Affecting Restaurant Revenue on Food Delivery Platforms
**Thời lượng gợi ý:** 12 phút trình bày + 3–5 phút hỏi đáp (khoảng 12 slide, mỗi slide ≈ 1 phút)
**Thông điệp xuyên suốt:** *Doanh thu mỗi đơn chủ yếu do giá món × số lượng quyết định; nhiều yếu tố mà nhà hàng hay tin là quan trọng (Rating, khu vực, giờ) không cho thấy liên hệ trong dữ liệu này.*

> Nguyên tắc cho cả bài: mỗi slide chỉ **một ý chính**, mỗi ý có **một con số** và **một biểu đồ**. Luôn nói "có liên hệ" hoặc "đi cùng", không nói "gây ra".

---

## Slide 1: Tiêu đề (0:30)
- Tên đề tài (EN và VN), tên nhóm, ngày thuyết trình.
- **Nói:** giới thiệu ngắn đề tài và câu hỏi chính.

## Slide 2: Câu hỏi và vì sao quan trọng (1:00)
- Câu hỏi: *Yếu tố nào thật sự có liên hệ với doanh thu nhà hàng trên nền tảng giao đồ ăn?*
- Công thức: **Revenue = Orders × AOV**.
- 3 nhóm yếu tố: trực tiếp, gián tiếp, ảnh hưởng lợi nhuận.
- **Nói:** nhà hàng hay tập trung vào Rating, khuyến mãi, tốc độ giao; dự án kiểm tra điều đó bằng dữ liệu.

## Slide 3: Dữ liệu và phạm vi (1:00)
- Bảng so sánh: Chowdeck (Nigeria, 3.061 đơn, chính) và Zomato (Delhi NCR, 21.131 đơn, bổ sung).
- Quyết định phạm vi: loại Groceries và Medications; hai dataset phân tích riêng, không so số tuyệt đối ₦ và ₹.
- **Nói:** vì sao không gộp dữ liệu (khác tiền tệ, khác thị trường).

## Slide 4: Làm sạch và chất lượng dữ liệu (1:00)
- 870 đơn (≈ 28%) timestamp sai thứ tự, được đánh dấu chứ không xóa; `delay_min` ở nhóm này bằng 0 nên KPI độ trễ tính trên đơn hợp lệ.
- Rating Zomato thiếu 88,3%, không điền giá trị giả.
- **Nói:** đây là điểm thể hiện sự cẩn thận với dữ liệu.

## Slide 5: Doanh thu theo năm: Orders × AOV (1:00)
- Bảng 2023–2025: doanh thu −12,7% rồi +5,0%.
- Phân rã: số đơn và AOV cùng đóng góp.
- **Lưu ý nói rõ:** khác biệt giữa các năm chưa có ý nghĩa thống kê (p = 0,44).
- **Hình:** biểu đồ cột kết hợp đường (Orders, AOV, Revenue theo năm).

## Slide 6: Nhóm món: chênh lệch đến từ AOV (1:30)
- Số đơn gần bằng nhau (985–1.051), AOV chênh 2,1 lần (Food ₦11.040 so với Drinks ₦5.263).
- Food 43% doanh thu, Drinks 22%.
- **Nói:** Drinks bán nhiều đơn nhất nhưng ít doanh thu nhất; muốn tăng doanh thu phải tăng giá trị mỗi đơn.
- **Hình:** `chart_revenue_by_category.png`.

## Slide 7: Nhà hàng: khác biệt là do nhóm món (1:00)
- Thứ hạng shop theo đúng nhóm món. Trong cùng một nhóm, các shop không khác nhau (p = 0,67–0,70).
- Doanh thu cấp shop tương quan 0,98 với AOV, −0,26 với số đơn.
- **Nói:** đây là ví dụ cho việc kết luận ban đầu "nhà hàng quyết định doanh thu" **không đứng vững** khi kiểm soát nhóm món.
- **Hình:** `chart_top10_shops_revenue.png` (tô màu theo nhóm món nếu làm được).

## Slide 8: Điều dữ liệu không ủng hộ: Rating, khu vực, giờ, ngày (1:30)
- Bảng ngắn: Rating (r = 0,05–0,14), khu vực (p = 0,55), thứ (p = 0,50), giờ (p = 0,56); mỗi yếu tố giải thích dưới 1%.
- Doanh thu 10 khu vực chênh tối đa 1,2 lần.
- **Nói:** "không tìm thấy liên hệ" không có nghĩa là "không có tác động", nhưng không đủ cơ sở để đầu tư theo hướng này.
- **Hình:** `chart_rating_vs_orders.png` hoặc ảnh trang Key Drivers (sau khi sửa).

## Slide 9: Khuyến mãi (Zomato) (1:30)
- 61,1% đơn có khuyến mãi; khách trả ₹665 so với ₹710 (−6,3%), hóa đơn gốc ₹797 so với ₹676.
- **Điểm nhấn:** đi cùng nhau, nhưng chưa biết nhân quả (không có nhóm đối chứng; hóa đơn lớn có thể là điều kiện được giảm giá).
- **Hình:** `chart_orders_by_discount.png` và `chart_aov_by_discount.png`.

## Slide 10: Dashboard Power BI (1:00)
- Ảnh 2–3 trang chính: Key Drivers, Chowdeck tổng quan, Zomato khuyến mãi.
- **Nói:** dashboard cho phép lọc theo năm, nhóm món, khu vực.
- *(Dùng ảnh sau khi dashboard đã sửa xong.)*

## Slide 11: Machine Learning (1:00)
- Random Forest phân loại "đơn giá trị cao": Chowdeck 77,7% (CV 76,2%), Zomato 68,7% (CV 68,3%).
- Nhóm món dẫn đầu nhưng phần lớn là hiển nhiên; Rating chỉ 3%.
- **Nói:** model chỉ để xếp hạng tương đối, không để dự đoán từng đơn; mức quan trọng không phải nhân quả.
- **Hình:** `chart_ml_feature_importance_chowdeck.png`.

## Slide 12: Đề xuất, hạn chế và kết luận (1:30)
- **Đề xuất (3 ý):** (1) tăng giá trị mỗi đơn bằng combo hoặc bán kèm, (2) thử nghiệm khuyến mãi có đối chứng và đo lợi nhuận, (3) theo dõi Orders × AOV hằng tháng.
- **Hạn chế (3 ý):** không có chi phí nên không đo lợi nhuận; timestamp lỗi và Rating thưa; Zomato bị một nhà hàng chi phối (74% doanh thu).
- **Kết luận:** doanh thu mỗi đơn chủ yếu do giá món × số lượng; không tìm thấy liên hệ đáng kể ở Rating, khu vực, giờ.
- Cảm ơn và mở phần hỏi đáp.

---

## Chuẩn bị hỏi đáp

| Câu hỏi có thể gặp | Gợi ý trả lời |
|---|---|
| Vì sao không gộp hai dataset? | Khác thị trường, tiền tệ và cấu trúc; gộp thô sẽ so sánh khập khiễng. Chỉ so sánh tỷ lệ % ở mức tổng hợp. |
| Vì sao loại Groceries và Medications? | Đề tài về nhà hàng, hai nhóm này không phải đồ ăn. Groceries lại có doanh thu cao nhất, nên đây là quyết định có ảnh hưởng và đã ghi rõ trong báo cáo. |
| Vậy Rating không quan trọng à? | Dữ liệu này không cho thấy liên hệ với doanh thu. Điều đó không phủ nhận Rating có thể quan trọng cho uy tín dài hạn. Rating Chowdeck chỉ có 5 mức, Zomato chỉ 11,8% đơn có Rating. |
| Khuyến mãi có hiệu quả không? | Chưa kết luận được. Có thông tin về hóa đơn và AOV, nhưng thiếu nhóm đối chứng và chi phí. Đề xuất A/B test. |
| Vì sao kết quả "yếu" như vậy? | Dữ liệu có ít biến ngữ cảnh, và dữ liệu có dấu hiệu mô phỏng. Kết quả âm tính vẫn có giá trị vì tránh đầu tư theo giả định không có bằng chứng. |
| Sao không dùng model mạnh hơn? | Mục tiêu là xếp hạng yếu tố, không phải dự đoán; các yếu tố ngữ cảnh có tín hiệu yếu nên model mạnh hơn không giải quyết được. |
| Timestamp lỗi 28% xử lý thế nào? | Đánh dấu, không xóa; KPI độ trễ chỉ tính trên đơn hợp lệ (trễ 59,6%, trung bình 5,5 phút). |
| Kết quả có áp dụng cho nhà hàng khác không? | Không khái quát được: 15 shop (Chowdeck) và 6 nhà hàng, một nhà hàng chiếm 74% doanh thu (Zomato). |
| Doanh thu giảm 2024 có đáng lo không? | Chênh lệch giữa các năm chưa có ý nghĩa thống kê (p = 0,44), chưa thể gọi là xu hướng. |
| Đo lợi nhuận được không? | Không, hai dataset thiếu chi phí. Đó là hướng phát triển. |

## Checklist chuẩn bị
- [ ] Sửa xong dashboard và thay ảnh trong `powerbi/`
- [ ] Điền nguồn và giấy phép dataset Chowdeck vào báo cáo và README
- [ ] Làm slide theo outline (khoảng 12 slide, tối đa 3 dòng chữ chính mỗi slide)
- [ ] Mỗi người nắm số liệu chính: 3.061 đơn, ₦25,2 triệu, AOV ₦8.241, Food ₦11.040 so với Drinks ₦5.263
- [ ] Tập nói thử và đo thời gian (mục tiêu 12 phút)
- [ ] Chuẩn bị trả lời các câu hỏi trong bảng trên
