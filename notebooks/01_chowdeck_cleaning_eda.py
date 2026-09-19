# ============================================================
# 01_chowdeck_cleaning_eda.py
# Data Cleaning + EDA cho dataset Chowdeck (Nigeria)
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
df = pd.read_excel('Chowdeck_Order_Delivery_Details.xlsx', sheet_name='Sheet1')
print("Shape ban đầu:", df.shape)

# ------------------------------------------------------------
# 2. CHUẨN HÓA TÊN CỘT
# ------------------------------------------------------------
df.columns = [c.strip() for c in df.columns]  # bỏ khoảng trắng thừa (vd 'Total ' -> 'Total')

# ------------------------------------------------------------
# 3. KIỂM TRA TÍNH LOGIC THỜI GIAN
# ------------------------------------------------------------
time_cols = ['Order Received', 'Preparing Order', 'Rider Accepted', 'Order Ready',
             'Rider At Vendor', 'Rider Picked Up', 'Order Arrived', 'Order Delivered']

# Đánh dấu dòng có timestamp không tăng dần đúng thứ tự
is_monotonic = pd.Series(True, index=df.index)
for i in range(len(time_cols) - 1):
    is_monotonic &= (df[time_cols[i]] <= df[time_cols[i + 1]])
df['time_sequence_valid'] = is_monotonic
print(f"\nSố đơn có thứ tự thời gian KHÔNG hợp lệ: {(~is_monotonic).sum()} / {len(df)}")

# ------------------------------------------------------------
# 4. KIỂM TRA OUTLIER (chỉ xem, chưa loại bỏ)
# ------------------------------------------------------------
print("\nThống kê mô tả các cột số:")
print(df[['Unit Price', 'Distance (km)', 'Sub Total', 'Total']].describe())

# ------------------------------------------------------------
# 5. KIỂM TRA RATING HỢP LỆ
# ------------------------------------------------------------
invalid_rating = df[(df['Rating'] < 1) | (df['Rating'] > 5)]
print(f"\nSố Rating ngoài khoảng [1,5]: {len(invalid_rating)}")

# ------------------------------------------------------------
# 6. TẠO CỘT PHÁI SINH: THỜI GIAN XỬ LÝ
# ------------------------------------------------------------
df['prep_time_min'] = (df['Order Ready'] - df['Preparing Order']).dt.total_seconds() / 60
df['delivery_time_min'] = (df['Order Delivered'] - df['Order Received']).dt.total_seconds() / 60
df['delay_min'] = (df['Order Delivered'] - df['Expected Delivery Time']).dt.total_seconds() / 60
# delay_min > 0 : giao trễ so với dự kiến | < 0 : giao sớm hơn dự kiến

# ------------------------------------------------------------
# 7. TẠO CỘT PHÁI SINH: THỜI ĐIỂM ĐẶT HÀNG
# ------------------------------------------------------------
df['order_hour'] = df['Order Received'].dt.hour
df['order_dayofweek'] = df['Order Received'].dt.day_name()
df['order_month'] = df['Order Received'].dt.to_period('M').astype(str)
df['order_year'] = df['Order Received'].dt.year

# ------------------------------------------------------------
# 8. XÁC ĐỊNH CỘT REVENUE CHUẨN
# ------------------------------------------------------------
df['revenue'] = df['Sub Total']  # Revenue của nhà hàng, KHÔNG gồm Delivery Fee/Service Fee

# ------------------------------------------------------------
# 8b. LỌC PHẠM VI: CHỈ GIỮ NHÓM LIÊN QUAN ẨM THỰC (theo xác nhận của user)
# ------------------------------------------------------------
restaurant_categories = ['Food', 'Drinks & Beverages', 'Pastries']
n_before = len(df)
df = df[df['Order Category'].isin(restaurant_categories)].copy()
n_after = len(df)
print(f"\nLọc Order Category: giữ {n_after}/{n_before} dòng "
      f"(loại bỏ Groceries & Medications, mất {n_before - n_after} dòng)")

# ------------------------------------------------------------
# 9. LOẠI CỘT KHÔNG PHỤC VỤ PHÂN TÍCH
# ------------------------------------------------------------
df_clean = df.drop(columns=['Delivery PIN', 'Url', 'Wallet Balance'])

# ------------------------------------------------------------
# 10. LƯU FILE ĐÃ LÀM SẠCH
# ------------------------------------------------------------
df_clean.to_csv('chowdeck_clean.csv', index=False)
print(f"\nĐã lưu chowdeck_clean.csv | Shape cuối: {df_clean.shape}")

# ============================================================
# EDA - PHÂN TÍCH KHÁM PHÁ DỮ LIỆU
# ============================================================

# --- Q1: Nhà hàng nào tạo doanh thu & AOV cao nhất? ---
shop_stats = df_clean.groupby('Shop Name').agg(
    total_orders=('revenue', 'count'),
    total_revenue=('revenue', 'sum'),
    avg_order_value=('Total', 'mean'),
    avg_rating=('Rating', 'mean')
).sort_values('total_revenue', ascending=False)
print("\n=== Top 10 nhà hàng theo doanh thu ===")
print(shop_stats.head(10))

plt.figure(figsize=(10, 6))
shop_stats['total_revenue'].head(10).plot(kind='barh')
plt.title('Top 10 Nhà hàng theo Tổng Doanh thu (Sub Total)')
plt.xlabel('Doanh thu (₦)')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('chart_top10_shops_revenue.png', dpi=120)
plt.close()

# --- Q2: Nhóm món ăn nào đóng góp doanh thu nhiều nhất? ---
category_revenue = df_clean.groupby('Order Category')['revenue'].sum().sort_values(ascending=False)
print("\n=== Doanh thu theo Order Category ===")
print(category_revenue)

plt.figure(figsize=(8, 5))
category_revenue.plot(kind='bar', color='teal')
plt.title('Doanh thu theo Nhóm sản phẩm (Order Category)')
plt.ylabel('Doanh thu (₦)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('chart_revenue_by_category.png', dpi=120)
plt.close()

# --- Q3: Rating có liên hệ với số đơn / AOV không? (ở cấp nhà hàng) ---
corr_rating_orders = shop_stats['avg_rating'].corr(shop_stats['total_orders'])
corr_rating_aov = shop_stats['avg_rating'].corr(shop_stats['avg_order_value'])
print(f"\nTương quan Rating trung bình vs Số đơn hàng (theo nhà hàng): {corr_rating_orders:.3f}")
print(f"Tương quan Rating trung bình vs AOV (theo nhà hàng): {corr_rating_aov:.3f}")

plt.figure(figsize=(7, 5))
sns.scatterplot(data=shop_stats, x='avg_rating', y='total_orders')
plt.title('Rating trung bình vs Số lượng đơn hàng (theo Nhà hàng)')
plt.tight_layout()
plt.savefig('chart_rating_vs_orders.png', dpi=120)
plt.close()

# --- Q4: Thời gian giao hàng/chuẩn bị món có liên hệ với Rating/số đơn? ---
corr_delivery_rating = df_clean['delivery_time_min'].corr(df_clean['Rating'])
corr_prep_rating = df_clean['prep_time_min'].corr(df_clean['Rating'])
print(f"\nTương quan Thời gian giao hàng vs Rating (cấp đơn hàng): {corr_delivery_rating:.3f}")
print(f"Tương quan Thời gian chuẩn bị món vs Rating (cấp đơn hàng): {corr_prep_rating:.3f}")

# --- Q5: Khu vực nào có doanh thu & mật độ đơn cao nhất? ---
location_stats = df_clean.groupby('Delivery Location').agg(
    total_orders=('revenue', 'count'),
    total_revenue=('revenue', 'sum')
).sort_values('total_revenue', ascending=False)
print("\n=== Doanh thu theo Khu vực giao hàng ===")
print(location_stats)

# --- Q6: Khung giờ/ngày nào tạo doanh thu cao nhất? ---
hourly_revenue = df_clean.groupby('order_hour')['revenue'].sum()
dow_revenue = df_clean.groupby('order_dayofweek')['revenue'].sum().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

plt.figure(figsize=(10, 5))
hourly_revenue.plot(kind='line', marker='o')
plt.title('Doanh thu theo Khung giờ trong ngày')
plt.xlabel('Giờ')
plt.ylabel('Doanh thu (₦)')
plt.tight_layout()
plt.savefig('chart_revenue_by_hour.png', dpi=120)
plt.close()

plt.figure(figsize=(8, 5))
dow_revenue.plot(kind='bar', color='coral')
plt.title('Doanh thu theo Thứ trong tuần')
plt.ylabel('Doanh thu (₦)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('chart_revenue_by_dayofweek.png', dpi=120)
plt.close()

# --- Tính KPI tổng hợp để lưu vào summary_metrics ---
kpi_summary = {
    'dataset': 'Chowdeck',
    'market': 'Nigeria',
    'total_orders': len(df_clean),
    'total_revenue': df_clean['revenue'].sum(),
    'aov': df_clean['Total'].mean(),
    'avg_rating': df_clean['Rating'].mean(),
    'corr_rating_vs_orders(shop_level)': corr_rating_orders,
    'corr_rating_vs_aov(shop_level)': corr_rating_aov,
    'corr_delivery_time_vs_rating': corr_delivery_rating,
    'corr_prep_time_vs_rating': corr_prep_rating,
}
pd.DataFrame([kpi_summary]).to_csv('chowdeck_kpi_summary.csv', index=False)

print("\n=== HOÀN TẤT CLEANING + EDA CHOWDECK ===")
print("Các file đã tạo: chowdeck_clean.csv, chowdeck_kpi_summary.csv, và 5 biểu đồ PNG")
