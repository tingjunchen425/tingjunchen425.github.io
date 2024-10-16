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
plt.show()