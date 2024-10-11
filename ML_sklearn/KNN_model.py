from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data  = pd.read_excel(r'ML_sklearn\test_file.xlsx')
y = data['最終結果']
y = y.map({'成功':1,'失敗':0})
x = data[['成功次數','失敗次數']]
plt.scatter(x['成功次數'],x['失敗次數'],c=y)
plt.xlabel('success count')
plt.ylabel('fail count')

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x,y)
test = np.array([[112,5],[100,3],[2,50]])
plt.scatter(test[:,0],test[:,1],c=knn.predict(test),marker='x',s=100)
plt.show()
