# ============================================================
# 02_zomato_cleaning_eda.py
# Data Cleaning + EDA cho dataset Zomato Delhi (Case study: Khuyến mãi)
# ============================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
pd.set_option('display.max_columns', 50)

# ------------------------------------------------------------
# 1. LOAD DATA
# ------------------------------------------------------------
df = pd.read_csv('order_history_kaggle_data.csv')
print("Shape ban đầu:", df.shape)

# ------------------------------------------------------------
# 2. LOẠI CỘT THIẾU QUÁ NHIỀU (>95%) VÀ CỘT KHÔNG CÓ BIẾN THIÊN
# ------------------------------------------------------------
cols_to_drop = [
    'Instructions', 'Review', 'Cancellation/Rejection reason',
    'Restaurant compensation (Cancellation)', 'Restaurant penalty (Rejection)',
    'Customer complaint tag', 'City', 'Delivery'
]
df = df.drop(columns=[c for c in cols_to_drop if c in df.columns])
print(f"Đã loại {len(cols_to_drop)} cột thiếu quá nhiều / không biến thiên")

# ------------------------------------------------------------
# 3. PARSE THỜI GIAN
# ------------------------------------------------------------
df['Order Placed At'] = pd.to_datetime(df['Order Placed At'], format='%I:%M %p, %B %d %Y', errors='coerce')
print(f"Số dòng không parse được thời gian: {df['Order Placed At'].isna().sum()}")
df['order_hour'] = df['Order Placed At'].dt.hour
df['order_dayofweek'] = df['Order Placed At'].dt.day_name()

# ------------------------------------------------------------
# 4. CHUẨN HÓA CỘT DISTANCE (text -> số km)
#    Quy ước theo xác nhận của user: "<1km" -> 1km
# ------------------------------------------------------------
def parse_distance(val):
    if pd.isna(val):
        return np.nan
    val = str(val).strip().lower().replace('km', '')
    if val.startswith('<'):
        return 1.0
    try:
        return float(val)
    except ValueError:
        return np.nan

df['distance_km'] = df['Distance'].apply(parse_distance)
print(f"Số dòng không parse được Distance: {df['distance_km'].isna().sum()}")

# ------------------------------------------------------------
# 5. XỬ LÝ CỘT DISCOUNT CONSTRUCT (missing = không áp dụng khuyến mãi)
# ------------------------------------------------------------
df['Discount construct'] = df['Discount construct'].fillna('No Discount')

# ------------------------------------------------------------
# 6. TẠO CỘT TỔNG KHUYẾN MÃI
# ------------------------------------------------------------
discount_cols = [
    'Restaurant discount (Promo)',
    'Restaurant discount (Flat offs, Freebies & others)',
    'Gold discount',
    'Brand pack discount'
]
df['total_discount'] = df[discount_cols].sum(axis=1)
df['has_discount'] = df['total_discount'] > 0

# ------------------------------------------------------------
# 7. XỬ LÝ RATING (thiếu 88.3%) - KHÔNG điền giá trị giả
# ------------------------------------------------------------
print(f"\nSố đơn có Rating: {df['Rating'].notna().sum()} / {len(df)} "
      f"({df['Rating'].notna().mean()*100:.1f}%)")
df_rating = df[df['Rating'].notna()].copy()  # dùng riêng khi phân tích Rating

# ------------------------------------------------------------
# 8. KIỂM TRA OUTLIER
# ------------------------------------------------------------
print("\nThống kê mô tả các cột số chính:")
print(df[['Bill subtotal', 'Total', 'distance_km', 'KPT duration (minutes)',
           'Rider wait time (minutes)']].describe())

# ------------------------------------------------------------
# 9. LƯU FILE ĐÃ LÀM SẠCH
# ------------------------------------------------------------
df.to_csv('zomato_clean.csv', index=False)
print(f"\nĐã lưu zomato_clean.csv | Shape cuối: {df.shape}")

# ============================================================
# EDA - PHÂN TÍCH KHÁM PHÁ DỮ LIỆU
# ============================================================

# Chỉ tính Revenue/AOV trên đơn thành công (Delivered) - theo xác nhận của user
df_delivered = df[df['Order Status'] == 'Delivered'].copy()
print(f"\nSố đơn 'Delivered' dùng để tính Revenue/AOV: {len(df_delivered)} / {len(df)}")

# --- Q7: Khuyến mãi có làm tăng số lượng đơn hàng không? ---
orders_by_discount = df_delivered.groupby('has_discount').size()
print("\n=== Số lượng đơn theo có/không khuyến mãi (đơn Delivered) ===")
print(orders_by_discount)

# --- Q8: Khuyến mãi có làm giảm AOV không? ---
aov_by_discount = df_delivered.groupby('has_discount')['Total'].mean()
print("\n=== AOV theo có/không khuyến mãi (đơn Delivered) ===")
print(aov_by_discount)

corr_discount_bill = df_delivered['total_discount'].corr(df_delivered['Bill subtotal'])
print(f"\nTương quan Tổng khuyến mãi vs Bill subtotal: {corr_discount_bill:.3f}")

plt.figure(figsize=(7, 5))
sns.barplot(x=aov_by_discount.index.map({True: 'Có khuyến mãi', False: 'Không khuyến mãi'}),
            y=aov_by_discount.values)
plt.title('AOV: Có khuyến mãi vs Không khuyến mãi')
plt.ylabel('AOV (₹)')
plt.tight_layout()
plt.savefig('chart_aov_by_discount.png', dpi=120)
plt.close()

plt.figure(figsize=(7, 5))
sns.barplot(x=orders_by_discount.index.map({True: 'Có khuyến mãi', False: 'Không khuyến mãi'}),
            y=orders_by_discount.values)
plt.title('Số lượng đơn: Có khuyến mãi vs Không khuyến mãi')
plt.ylabel('Số đơn')
plt.tight_layout()
plt.savefig('chart_orders_by_discount.png', dpi=120)
plt.close()

# --- Q9: Đơn hủy/từ chối có liên quan đến KPT duration không? ---
status_kpt = df.groupby('Order Status')['KPT duration (minutes)'].mean().sort_values(ascending=False)
print("\n=== Thời gian chuẩn bị (KPT) trung bình theo Trạng thái đơn ===")
print(status_kpt)

plt.figure(figsize=(9, 5))
status_kpt.plot(kind='bar', color='indianred')
plt.title('Thời gian chuẩn bị món (KPT) trung bình theo Trạng thái đơn')
plt.ylabel('KPT (phút)')
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.savefig('chart_kpt_by_status.png', dpi=120)
plt.close()

order_status_dist = df['Order Status'].value_counts(normalize=True) * 100
print("\n=== Phân bố Order Status (%) ===")
print(order_status_dist)

# --- Tính KPI tổng hợp để so sánh liên thị trường ---
kpi_summary = {
    'dataset': 'Zomato',
    'market': 'India (Delhi NCR)',
    'total_orders_delivered': len(df_delivered),
    'total_revenue': df_delivered['Total'].sum(),
    'aov': df_delivered['Total'].mean(),
    'pct_orders_with_discount': df_delivered['has_discount'].mean() * 100,
    'aov_with_discount': aov_by_discount.get(True, np.nan),
    'aov_without_discount': aov_by_discount.get(False, np.nan),
    'corr_discount_vs_bill_subtotal': corr_discount_bill,
    'pct_rating_available': df['Rating'].notna().mean() * 100,
}
pd.DataFrame([kpi_summary]).to_csv('zomato_kpi_summary.csv', index=False)

print("\n=== HOÀN TẤT CLEANING + EDA ZOMATO ===")
print("Các file đã tạo: zomato_clean.csv, zomato_kpi_summary.csv, và 3 biểu đồ PNG")
