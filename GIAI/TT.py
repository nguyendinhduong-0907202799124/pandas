import pandas as pd
import math

X = pd.read_csv('D:/vscode/python/GIAI/Advertising.csv')
col1 = X['TV']
col2 = X['radio']

print("Cột 1 (TV):")
print(col1.head())

print("\nCột 2 (radio):")
print(col2.head())

# Tính hiệp phương sai giữa hai cột
covariance = col1.cov(col2)
print('Hiep phuong sai giua hai cot :',covariance)

# Tính phương sai của từng cột
variance_col1 = col1.var()
variance_col2 = col2.var()
print('Phuong sai cua cot 1:',variance_col1)
print('Phuong sai cua cot 2:',variance_col2)

# Tính hệ số tương quan Pearson giữa hai cột
pearson_correlation = col1.corr(col2)
print('He so tuong quan Pearson :',pearson_correlation)

# Tính góc θ (radian và độ) giữa hai cột
theta_radian = math.acos(pearson_correlation)
print('Góc θθ (radian):',theta_radian)
theta_degree = math.degrees(theta_radian)
print('Góc θθ (do):',theta_degree)

