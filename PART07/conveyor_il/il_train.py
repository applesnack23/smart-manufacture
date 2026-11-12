# il_train.py — 모방학습: 운전 기록으로 결정 트리 학습
#   python conveyor_il/il_train.py conveyor_il/il_dataset.csv
import sys
import pandas as pd
sys.path.append(".")

# [1] 데이터 살펴보기
data = sys.argv[1]
df = pd.read_csv(data)
print(len(df), "줄")
print(df.head(6))
print(pd.crosstab([df.Sensor01, df.Sensor02, df.LastSensor], df.Action))
X = df[["Sensor01", "Sensor02", "LastSensor"]]
y = df["Action"]

# [2] 학습 80 % · 검증 20 % 로 나눠 학습
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
X_tr, X_val, y_tr, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_tr, y_tr)
print("학습 정확도:", round(model.score(X_tr, y_tr), 3))
print("검증 정확도:", round(model.score(X_val, y_val), 3))

# [3] 혼동 행렬 (행 = 사람, 열 = AI)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_val, model.predict(X_val)))

# [4] 12 가지 상태 표로 저장
import ai_table

def predict(a, b, last):
    q = pd.DataFrame([[a, b, last]], columns=X.columns)
    return model.predict(q)[0]

ai_table.save(predict, data.replace(".csv", "_table.json"))
