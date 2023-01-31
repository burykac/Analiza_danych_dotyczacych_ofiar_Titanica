# import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
train_file = pd.read_csv(r"D:\titanic\train.csv")
train_file["Age"].plot.hist(bins=30)
sns.set_style("darkgrid")
train_file.plot.hist(x="Age", y="Fare", figsize=(8, 6))
train_file.plot.scatter(x="Age", y="Fare", figsize=(8, 6))
plt.show()
