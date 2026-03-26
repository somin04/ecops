# 필요한 라이브러리 import
import numpy as np
from sklearn.linear_model import LinearRegression

# 예제 데이터 (집 크기 → 가격)
# 단위: 평수 / 가격(억)
X = np.array([[10], [20], [30], [40], [50]])
y = np.array([1, 2, 3, 4, 5])

# 모델 생성
model = LinearRegression()

# 학습
model.fit(X, y)

# 예측
new_size = np.array([[25]])
predicted_price = model.predict(new_size)

print(f"25평 집의 예상 가격: {predicted_price[0]:.2f}억")
