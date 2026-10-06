# Machine Learning Summary

## Bài toán
Phân loại (Classification): dự đoán 1 đơn hàng có thuộc nhóm **"giá trị cao"** (trên median) hay không, dựa trên các yếu tố **ngữ cảnh** (nhà hàng, nhóm món, thời gian, khu vực, khoảng cách, rating, khuyến mãi, vận hành) — **không dùng** Unit Price/Quantity/Bill subtotal làm input vì đó là thành phần trực tiếp tạo ra giá trị đơn hàng (tránh data leakage).

**Mục đích:** xác định đa biến (xét nhiều yếu tố cùng lúc) yếu tố nào thực sự ảnh hưởng đến giá trị đơn hàng — bổ sung bằng chứng mạnh hơn cho phần tương quan đơn biến đã làm ở Bước 6.

Model dùng: **Random Forest Classifier** (200 cây, max_depth=8, class_weight='balanced'), chia Train/Test 80/20.

---

## Kết quả Chowdeck

| Metric | Giá trị |
|---|---|
| Accuracy | 77.7% |
| Precision | 83.3% |
| Recall | 63.0% |
| F1-score | 71.8% |

**Feature Importance (xếp hạng mức độ ảnh hưởng):**
1. Order Category — 33.9%
2. Shop Name — 22.5%
3. Distance (km) — 9.6%
4. Thời gian giao hàng — 8.9%
5. Khung giờ đặt hàng — 6.7%
6. Thời gian chuẩn bị món — 6.4%
7. Khu vực giao hàng — 4.6%
8. Thứ trong tuần — 4.4%
9. **Rating — 3.0% (thấp nhất)**

→ **Nhất quán với Bước 6**: Rating có ảnh hưởng yếu nhất, trong khi Nhóm món và Nhà hàng là 2 yếu tố nổi bật nhất (chiếm hơn 56% tổng mức độ quan trọng).

> ⚠️ **Lưu ý khi diễn giải:** Nhóm món và nhà hàng gần như quyết định mức giá của món (Food ≈ ₦11.040/đơn, Drinks ≈ ₦5.263/đơn), nên việc hai yếu tố này dự đoán tốt "đơn giá trị cao" phần lớn là điều hiển nhiên, chưa phải phát hiện mới. Thông tin đáng chú ý hơn là các yếu tố còn lại (Rating, khu vực, thứ trong tuần, khung giờ) đều có độ quan trọng thấp.

**Cross-Validation (5-fold):** Accuracy trung bình **76.2% (± 1.1%)** qua 5 lần chia dữ liệu khác nhau — rất ổn định, xác nhận kết quả 77.7% đo 1 lần không phải do may rủi của cách chia Train/Test. (Đã chạy lại và kiểm chứng trong `notebooks/03_chowdeck_ml.ipynb`; accuracy từng fold: 0.750, 0.771, 0.778, 0.750, 0.763.)

**SHAP Summary Plot** (`chart_ml_shap_summary_chowdeck.png`): cho biết thêm **chiều ảnh hưởng** của từng yếu tố số (Distance, prep_time, delivery_time, order_hour, Rating), ví dụ: thời gian chuẩn bị và khoảng cách thấp có xu hướng đi cùng xác suất "đơn giá trị cao" thấp hơn.

> ⚠️ **Không diễn giải màu đỏ/xanh cho `Order Category_enc`, `Shop Name_enc`, `Delivery Location_enc`, `order_dayofweek_enc`.** Các biến này được mã hóa bằng LabelEncoder (số thứ tự theo alphabet), nên "giá trị cao/thấp" của mã số không mang ý nghĩa thực tế. Với Order Category, hai cụm trên biểu đồ phản ánh các nhóm món khác nhau: Food (mã 1) đẩy xác suất lên, Drinks (mã 0) và Pastries (mã 2) kéo xuống, phù hợp với AOV từng nhóm.

## Kết quả Zomato

| Metric | Giá trị |
|---|---|
| Accuracy | 68.7% |
| Precision | 68.3% |
| Recall | 69.3% |
| F1-score | 68.8% |

**Feature Importance:**
1. Thời gian chuẩn bị món (KPT) — 50.4%
2. Tên nhà hàng — 11.2%
3. Có khuyến mãi hay không — 10.3%
4. Thời gian tài xế chờ — 8.3%
5. Khoảng cách giao hàng — 7.2%
6. Khung giờ đặt hàng — 5.9%
7. Thứ trong tuần — 3.4%
8. Khu vực (Subzone) — 3.3%

→ KPT duration nổi bật nhất — đơn phức tạp/nhiều món thường mất thời gian chuẩn bị lâu hơn và có giá trị cao hơn (quan hệ vận hành hợp lý, không phải lỗi rò rỉ dữ liệu vì KPT không được tính trực tiếp từ Bill subtotal). Khuyến mãi đứng thứ 3: đơn có khuyến mãi **đi cùng** hóa đơn gốc cao hơn (trung bình ₹797 so với ₹676 ở đơn không có khuyến mãi, đơn `Delivered`).

**Cross-Validation (5-fold):** Accuracy trung bình **68.3% (± 0.7%)** — ổn định, khớp với kết quả đo 1 lần (68.7%).

**SHAP Summary Plot** (`chart_ml_shap_summary_zomato.png`): `has_discount` là biến nhị phân nên đọc được màu: điểm đỏ (có khuyến mãi) tập trung về phía phải, tức đơn có khuyến mãi gắn với xác suất "giá trị hóa đơn gốc cao" lớn hơn.

> ⚠️ **Chiều nhân quả chưa xác định.** Đây là mối liên hệ, không chứng minh khuyến mãi làm hóa đơn tăng. Có thể ngược lại: hóa đơn lớn mới đủ điều kiện áp dụng khuyến mãi (ví dụ ngưỡng đơn tối thiểu). Ngoài ra, tiền giảm giá thường tính theo % hóa đơn nên tương quan giữa `total_discount` và `Bill subtotal` (0,50) một phần mang tính cơ học và không nên dùng làm bằng chứng khuyến mãi "kéo" giá trị đơn. Dữ liệu cũng không có nhóm đối chứng hay thay đổi theo thời gian để kết luận khuyến mãi tạo thêm đơn.

---

## Giới hạn cần nêu trong báo cáo

- Model đạt độ chính xác tốt hơn đoán ngẫu nhiên (50%) nhưng không phải rất cao (68–78%) — phù hợp để **xếp hạng mức độ quan trọng tương đối** giữa các yếu tố, KHÔNG nên dùng để dự đoán chính xác giá trị từng đơn hàng cụ thể trong thực tế vận hành.
- Random Forest cho ra "Feature Importance" dựa trên mức độ giảm độ hỗn loạn (Gini impurity) khi chia theo từng yếu tố — đây vẫn là thước đo tương quan/đóng góp thống kê, **không chứng minh quan hệ nhân quả**.
- Các biến phân loại (nhóm món, nhà hàng, khu vực, thứ trong tuần) được mã hóa bằng LabelEncoder; Random Forest xử lý được nhưng thứ tự mã số không có ý nghĩa, nên chỉ đọc độ quan trọng, không đọc chiều SHAP của các biến này.
- Target được định nghĩa bằng ngưỡng median tự chọn (nhị phân hóa) — cách định nghĩa "giá trị cao" khác có thể cho kết quả hơi khác.
- Model chưa được tinh chỉnh tham số (hyperparameter tuning) kỹ lưỡng — đây là model "nhỏ" phục vụ mục đích tìm insight, không phải model triển khai thực tế.

## File liên quan
- `notebooks/03_chowdeck_ml.ipynb`
- `notebooks/04_zomato_ml.ipynb`
- `outputs/charts/chart_ml_feature_importance_chowdeck.png`, `chart_ml_feature_importance_zomato.png`
- `outputs/charts/chart_ml_confusion_matrix_chowdeck.png`, `chart_ml_confusion_matrix_zomato.png`
- `outputs/charts/chart_ml_shap_summary_chowdeck.png`, `chart_ml_shap_summary_zomato.png`
