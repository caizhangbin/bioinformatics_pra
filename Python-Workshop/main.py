import pandas as pd

df = pd.read_csv("../Python-Workshop/data.csv")

df['class'].unique()
classes = df['class'].unique()

for iris in classes:
  class_df = df.loc[ df['class']==iris, : ]
  print(iris)
  print(class_df.describe())


import matplotlib.pyplot as plt

data = [0,1,2,3,4,7,10,16,15,8,4,7,3,1,0]

plt.plot(data)
plt.show()


classes = df['class'].unique()

for iris in classes:
  iris_df = df.loc[df['class']==iris, :]
  x = iris_df['petal_length']
  y = iris_df['petal_width']
  plt.scatter(x, y)

plt.legend(classes)
plt.show()