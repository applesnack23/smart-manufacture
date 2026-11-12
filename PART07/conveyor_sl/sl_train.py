# sl_train.py — 지도학습: 정답표로 결정 트리 학습
import sys
import pandas as pd
sys.path.append(".")                          # AI_Training 폴더의 ai_table.py

# [1] 데이터 읽기: 특징 X 와 라벨 y
df = pd.read_csv("conveyor_sl/sl_dataset.csv")
print(df)
X = df[["Sensor01", "Sensor02", "LastSensor"]]
y = df["Label"]

# [2] 학습: fit
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X, y)
print("학습 정확도:", model.score(X, y))

# [3] 배운 규칙 보기
from sklearn.tree import export_text
print(export_text(model, feature_names=list(X.columns)))

# [4] 추론 해 보기: predict
for s in ([1, 0, 1], [0, 0, 2], [0, 0, 0]):
    q = pd.DataFrame([s], columns=X.columns)
    print("A,B,LAST =", s, "-> 행동", model.predict(q)[0])

# [5] 12 가지 상태 표로 저장
import ai_table

def predict(a, b, last):
    q = pd.DataFrame([[a, b, last]], columns=X.columns)
    return model.predict(q)[0]

ai_table.save(predict, "conveyor_sl/sl_table.json")
