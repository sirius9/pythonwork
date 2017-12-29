# -*- coding: utf-8 -*-
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.callbacks import EarlyStopping
import pandas as pd, numpy as np

# BMI 읽어들이고 정규화
csv = pd.read_csv("C:\\pythonwork\\python-machine-learning\\ch04\\ch04-5\\bmi.csv")

# 몸무게 키 데이터
csv['weight'] /=100
csv['height'] /= 200

X = csv[["weight", "height"]].as_matrix() # pandas dataframe을 numpy matrix로 변환

# 레이블
bclass = {"thin" : [1,0,0], "normal" : [0,1,0], "fat" : [0,0,1]}
y = np.empty((20000,3))
for i , v in enumerate(csv["label"]):
    y[i] = bclass[v]

# 훈련데이터와 테스트 데이터로 나누기
X_train, y_train = X[1:15001], y[1:15001]
X_test, y_test = X[15001:20001], y[15001:20001]

# 모델 구조 정의
model = Sequential()
model.add(Dense(512, input_shape=(2,)))
model.add(Activation('relu'))
model.add(Dropout(0.1))

model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.1))

model.add(Dense(3))
model.add(Activation('softmax'))

# 모델구축
model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

# 데이터 훈련
hist = model.fit(
    X_train, y_train,
    batch_size=100,  # 전체 데이터 대신 100개씩만
    nb_epoch=20, # 20번 반복
    validation_split=0.1,
    callbacks=[EarlyStopping(monitor='val_loss', patience=2)],
    verbose=1)

# 테스트 데이터로 평가
score= model.evaluate(X_test, y_test)
print('loss = ', score[0])
print('accuracy = ', score[1])