import pandas as pd
import dataframe_image as dfi
import img2pdf
import matplotlib as plt

# Đọc dữ liệu từ nhiều file CSV
data01 = pd.read_csv('/Users/phamthanh/Downloads/Thongkecapnhatdiem.csv')
data02 = pd.read_csv('/Users/phamthanh/Downloads/SMAS Report (1) (1).csv')
data03 = pd.read_csv('/Users/phamthanh/Downloads/Thong Ke Cap Nhat Diem.csv')
data04 = pd.read_csv('/Users/phamthanh/Downloads/Thong Ke Cap Nhat Diem (2) (1).csv')
data05 = pd.read_csv('/Users/phamthanh/Downloads/Converted File 6a2.csv')
data06 = pd.read_csv('/Users/phamthanh/Downloads/Thongke Cap Nhat Diem (1).csv')
data07 = pd.read_csv('/Users/phamthanh/Downloads/coMinh.csv')
data08 = pd.read_csv('/Users/phamthanh/Downloads/coMinh2.csv')

# Gộp tất cả vào một DataFrame
df = pd.concat([data01, data02, data03, data04, data05, data06, data07, data08], ignore_index=True)

# Lọc theo điều kiện
mask_df = ((df['Tài khoản cập nhật'] == 'Nguyễn Thị Minh') & (df['Trước khi cập nhật'] != 'Trống'))
filtered = df[mask_df]

# Lấy các cột cần thiết
result = filtered[['Lớp', 'Học sinh', 'Môn học', 'Hành động', 'Trước khi cập nhật', 'Sau khi cập nhật', 'Thời gian cập nhật']]
# Đặt lại chỉ số
result = result.reset_index(drop=True)
result.index += 1
result.index.name = "STT"

# In ra kết quả
print(result)

# Xuất ra hình ảnh (nếu cần)
dfi.export(result, 'filtered_table.png')

# ✅ Xuất ra file Excel
result.to_excel("filtered_table.xlsx", index=True)
