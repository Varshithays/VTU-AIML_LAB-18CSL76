import matplotlib.pyplot as plt 
from sklearn import datasets 
from sklearn.cluster import KMeans 
import numpy as np 
import pandas as pd 

iris=datasets.load_iris() 

x=pd.DataFrame(iris.data) 
x.columns=['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width'] 

y=pd.DataFrame(iris.target) 
y.columns=['Targets'] 

model=KMeans(n_clusters=3,n_init=2) 
model.fit(x) 

plt.figure(figsize=(14,14)) 
colormap=np.array(['red','lime','black']) 

plt.subplot(2,2,1) 
plt.scatter(x.Petal_Length,x.Petal_Width,c=colormap[y.Targets],s=40) 
plt.title("Red Clustering") 
plt.xlabel("Petal Length") 
plt.ylabel("Petal Width") 
plt.show() 

plt.subplot(2,2,2) 
plt.scatter(x.Petal_Length,x.Petal_Width,c=colormap[model.labels_],s=40) 
plt.title("K Means Clustering") 
plt.xlabel("Petal Length") 
plt.ylabel("Petal Width") 
plt.show()
