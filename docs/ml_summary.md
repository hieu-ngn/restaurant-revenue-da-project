# Machine Learning Summary

## Bài toán
Phân loại (Classification): dự đoán 1 đơn hàng có thuộc nhóm **"giá trị cao"** (trên median) hay không, dựa trên các yếu tố **ngữ cảnh** (nhà hàng, nhóm món, thời gian, khu vực, khoảng cách, rating, khuyến mãi, vận hành) — **không dùng** Unit Price/Quantity/Bill subtotal làm input vì đó là thành phần trực tiếp tạo ra giá trị đơn hàng (tránh data leakage).

**Mục đích:** xem xét đa biến (nhiều yếu tố cùng lúc) yếu tố nào có liên hệ với giá trị đơn hàng, để đối chiếu với phần tương quan đơn biến ở Bước 6. Model là công cụ **hỗ trợ**, không phải kết luận nhân quả; mục *Kiểm tra bổ sung* bên dưới cho thấy giá trị bổ sung của model so với baseline đơn giản.

Model dùng: **Random Forest Classifier** (200 cây, max_depth=8, class_weight='balanced'), chia Train/Test 80/20.

---

## Kết quả Chowdeck

| Metric | Giá trị |
|---|---|
| Accuracy | 77.5% |
| Precision | 82.5% |
| Recall | 63.4% |
| F1-score | 71.7% |

**Feature Importance (xếp hạng mức độ ảnh hưởng):**
1. Order Category — 35.4%
2. Shop Name — 20.8%
3. Distance (km) — 9.7%
4. Thời gian giao hàng — 8.8%
5. Khung giờ đặt hàng — 6.8%
6. Thời gian chuẩn bị món — 6.4%
7. Khu vực giao hàng — 4.7%
8. Thứ trong tuần — 4.4%
9. **Rating — 3.1% (thấp nhất)**

→ **Nhất quán với Bước 6**: Rating có ảnh hưởng yếu nhất, trong khi Nhóm món và Nhà hàng là 2 yếu tố nổi bật nhất (chiếm hơn 56% tổng mức độ quan trọng).

> ⚠️ **Lưu ý khi diễn giải:** Nhóm món và nhà hàng gần như quyết định mức giá của món (Food ≈ ₦11.040/đơn, Drinks ≈ ₦5.263/đơn), nên việc hai yếu tố này dự đoán tốt "đơn giá trị cao" phần lớn là điều hiển nhiên, chưa phải phát hiện mới. Mỗi shop thuộc đúng một nhóm món nên `Shop Name` một phần chỉ lặp lại thông tin của `Order Category`: khi kiểm soát nhóm món, các shop không khác nhau về giá trị đơn (ANOVA p = 0,67–0,70 trong từng nhóm), nên mức quan trọng 20,8% của `Shop Name` không nên đọc như "tên nhà hàng quyết định doanh thu". Thông tin đáng chú ý hơn là các yếu tố còn lại (Rating, khu vực, thứ trong tuần, khung giờ) đều có độ quan trọng thấp.

**Cross-Validation (5-fold):** Accuracy trung bình **76.2% (± 1.0%)** qua 5 lần chia dữ liệu khác nhau — rất ổn định, xác nhận kết quả 77.5% đo 1 lần không phải do may rủi của cách chia Train/Test. (Đã chạy lại và kiểm chứng trong `notebooks/03_chowdeck_ml.ipynb`; accuracy từng fold: 0.750, 0.773, 0.775, 0.753, 0.760.)

**SHAP Summary Plot** (`chart_ml_shap_summary_chowdeck.png`): cho biết thêm **chiều ảnh hưởng** của từng yếu tố số (Distance, prep_time, delivery_time, order_hour, Rating), ví dụ: thời gian chuẩn bị và khoảng cách thấp có xu hướng đi cùng xác suất "đơn giá trị cao" thấp hơn.

> ⚠️ **Không diễn giải màu đỏ/xanh cho `Order Category_enc`, `Shop Name_enc`, `Delivery Location_enc`, `order_dayofweek_enc`.** Các biến này được mã hóa bằng LabelEncoder (số thứ tự theo alphabet), nên "giá trị cao/thấp" của mã số không mang ý nghĩa thực tế. Với Order Category, hai cụm trên biểu đồ phản ánh các nhóm món khác nhau: Food (mã 1) đẩy xác suất lên, Drinks (mã 0) và Pastries (mã 2) kéo xuống, phù hợp với AOV từng nhóm.

### Kiểm tra bổ sung (baseline, ablation, permutation) – Chowdeck

> Số liệu dưới đây lấy từ lần chạy `03_chowdeck_ml.ipynb` mục 5b (5-fold CV). Chạy lại trên máy khác có thể lệch ±1 điểm % tùy phiên bản thư viện.

| Bộ feature | Accuracy CV |
|---|---|
| Baseline: luôn đoán lớp đa số | 55,0% |
| Chỉ `Order Category` | 76,5% |
| `Order Category` + `Shop Name` | 76,5% |
| Bỏ `Order Category` và `Shop Name` | 51,5% |
| Bỏ `Shop Name` | 75,3% |
| Bỏ `prep_time` và `delivery_time` | 76,2% |
| **Đầy đủ feature (model hiện tại)** | **76,2%** |
| Đầy đủ feature, chỉ đơn timestamp hợp lệ (n = 2.191) | 75,9% |

**Kết luận:**
- Baseline đúng của Chowdeck là **55%** (lớp đa số), không phải 50%.
- Chỉ riêng `Order Category` đã đạt 76,5%, **bằng hoặc cao hơn** model đầy đủ (76,2%). Model **không học thêm được gì đáng kể** ngoài nhóm món.
- Bỏ cả nhóm món và shop thì accuracy giảm còn 51,5%, **thấp hơn baseline 55%**: các yếu tố còn lại (khoảng cách, giờ, thứ, khu vực, rating, thời gian) gần như không giúp phân biệt đơn giá trị cao/thấp.
- Permutation importance trên tập test: `Order Category` làm giảm accuracy ≈ 18,9 điểm %, `Shop Name` ≈ 4,2 điểm %, các feature còn lại ≈ 0 hoặc âm (nằm trong sai số). Điều này khác với `feature_importances_` (Distance 9,6%, delivery_time 8,8%): impurity importance thiên lệch về biến liên tục nên **không nên dùng thứ hạng đó để kết luận** Distance hay thời gian giao hàng quan trọng.
- Huấn luyện chỉ trên đơn có timestamp hợp lệ không làm thay đổi kết luận (75,9%).

**Cách nói khi báo cáo:** "Trong dataset này, giá trị đơn gần như được giải thích bởi nhóm món; các yếu tố vận hành và ngữ cảnh còn lại không cho thấy đóng góp rõ ràng. Model không cho thêm thông tin ngoài nhóm món."

---

## Kết quả Zomato

| Metric | Giá trị |
|---|---|
| Accuracy | 68.5% |
| Precision | 68.2% |
| Recall | 69.1% |
| F1-score | 68.6% |

**Feature Importance:**
1. Thời gian chuẩn bị món (KPT) — 50.5%
2. Tên nhà hàng — 11.0%
3. Có khuyến mãi hay không — 10.1%
4. Thời gian tài xế chờ — 8.4%
5. Khoảng cách giao hàng — 7.2%
6. Khung giờ đặt hàng — 5.9%
7. Thứ trong tuần — 3.5%
8. Khu vực (Subzone) — 3.4%

→ KPT duration nổi bật nhất — đơn phức tạp/nhiều món thường mất thời gian chuẩn bị lâu hơn và có giá trị cao hơn (quan hệ vận hành hợp lý, không phải lỗi rò rỉ dữ liệu vì KPT không được tính trực tiếp từ Bill subtotal). Khuyến mãi đứng thứ 3: đơn có khuyến mãi **đi cùng** hóa đơn gốc cao hơn (trung bình ₹797 so với ₹676 ở đơn không có khuyến mãi, đơn `Delivered`).

**Cross-Validation (5-fold):** Accuracy trung bình **68.5% (± 0.6%)** — ổn định, khớp với kết quả đo 1 lần (68.5%).

**SHAP Summary Plot** (`chart_ml_shap_summary_zomato.png`): `has_discount` là biến nhị phân nên đọc được màu: điểm đỏ (có khuyến mãi) tập trung về phía phải, tức đơn có khuyến mãi gắn với xác suất "giá trị hóa đơn gốc cao" lớn hơn.

> ⚠️ **Chiều nhân quả chưa xác định.** Đây là mối liên hệ, không chứng minh khuyến mãi làm hóa đơn tăng. Có thể ngược lại: hóa đơn lớn mới đủ điều kiện áp dụng khuyến mãi (ví dụ ngưỡng đơn tối thiểu). Ngoài ra, tiền giảm giá thường tính theo % hóa đơn nên tương quan giữa `total_discount` và `Bill subtotal` (0,50) một phần mang tính cơ học và không nên dùng làm bằng chứng khuyến mãi "kéo" giá trị đơn. Dữ liệu cũng không có nhóm đối chứng hay thay đổi theo thời gian để kết luận khuyến mãi tạo thêm đơn.

---

### Kiểm tra bổ sung (baseline, ablation, permutation) – Zomato

> Số liệu lấy từ lần chạy `04_zomato_ml.ipynb` mục 5b (5-fold CV). Chạy lại có thể lệch ±1 điểm %.

| Bộ feature | Accuracy CV |
|---|---|
| Baseline: luôn đoán lớp đa số | 50,2% |
| Chỉ `Restaurant name` | 56,4% |
| Chỉ `KPT duration` | 63,2% |
| Bỏ `KPT duration` | 61,6% |
| Bỏ `KPT` và `Rider wait time` | 61,1% |
| Bỏ `Restaurant name` | 66,9% |
| Bỏ `has_discount` | 66,7% |
| **Đầy đủ feature (model hiện tại)** | **68,5%** |

**Kết luận:**
- Baseline của Zomato ≈ 50,2%, model hơn khoảng 18 điểm %.
- `KPT duration` đóng góp rõ nhất: bỏ KPT thì accuracy giảm khoảng 7 điểm % (68,5% → 61,6%); permutation importance giảm ≈ 13 điểm %. Con số 50,4% của impurity importance **phóng đại** mức đóng góp này.
- `Restaurant name` và `has_discount` mỗi biến đóng góp khoảng 2 điểm % (bỏ từng biến thì accuracy giảm còn 66,9% và 66,7%).
- `Rider wait time` gần như không đóng góp (bỏ thêm không làm accuracy giảm; permutation ≈ 0,001).
- Quan hệ KPT – giá trị đơn là quan hệ vận hành hợp lý (đơn nhiều món thường lâu hơn), không phải nhân quả đã được chứng minh; `has_discount` vẫn chỉ là mối liên hệ như đã nêu ở trên.

---

## Giới hạn cần nêu trong báo cáo

- Model hơn baseline lớp đa số (Chowdeck 55%, Zomato ≈ 50%) nhưng độ chính xác không rất cao (68–78%). Ở Chowdeck, phần hơn baseline gần như hoàn toàn đến từ `Order Category` (xem mục Kiểm tra bổ sung). Model phù hợp để **đối chiếu mức độ liên hệ tương đối** giữa các yếu tố, KHÔNG nên dùng để dự đoán chính xác giá trị từng đơn hàng trong thực tế vận hành.
- Random Forest cho ra "Feature Importance" dựa trên mức độ giảm độ hỗn loạn (Gini impurity) khi chia theo từng yếu tố. Thước đo này thiên lệch về biến liên tục và biến nhiều giá trị, nên cần đối chiếu với permutation importance và ablation (đã làm ở mục 5b). Cả hai vẫn chỉ là đóng góp thống kê, **không chứng minh quan hệ nhân quả**.
- Các biến phân loại (nhóm món, nhà hàng, khu vực, thứ trong tuần) được mã hóa bằng LabelEncoder; Random Forest xử lý được nhưng thứ tự mã số không có ý nghĩa, nên chỉ đọc độ quan trọng, không đọc chiều SHAP của các biến này.
- Target được định nghĩa bằng ngưỡng median tự chọn (nhị phân hóa) — cách định nghĩa "giá trị cao" khác có thể cho kết quả hơi khác.
- Model chưa được tinh chỉnh tham số (hyperparameter tuning) kỹ lưỡng — đây là model "nhỏ" phục vụ mục đích tìm insight, không phải model triển khai thực tế.

## File liên quan
- `notebooks/03_chowdeck_ml.ipynb`
- `notebooks/04_zomato_ml.ipynb`
- `outputs/charts/chart_ml_feature_importance_chowdeck.png`, `chart_ml_feature_importance_zomato.png`
- `outputs/charts/chart_ml_confusion_matrix_chowdeck.png`, `chart_ml_confusion_matrix_zomato.png`
- `outputs/charts/chart_ml_shap_summary_chowdeck.png`, `chart_ml_shap_summary_zomato.png`
- `outputs/charts/chart_ml_ablation_chowdeck.png`, `chart_ml_ablation_zomato.png`
- `outputs/charts/chart_ml_permutation_importance_chowdeck.png`, `chart_ml_permutation_importance_zomato.png`
