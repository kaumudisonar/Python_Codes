import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show
import numpy as np
import pandas as pd
import copy

df=pd.DataFrame({'x':[12, 20, 28, 18, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61,64, 69, 72],
                'y':[39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19,7, 24]})
                
#Step 2 : Random centroids generation
np.random.seed(200)
k=3
#centroids[i]=[x,y]
centroids = {
 i+1: [np.random.randint(0, 80), np.random.randint(0, 80)]
 for i in range(k)
}
print(centroids)

fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color='k')
colmap = {1: 'r', 2: 'g', 3: 'b'}
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.title("Marvellous : Dataset with random centroid");
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show() 

#step 2: Assignment – K clusters are created by associating each observation with the nearest centroid 
def assignment(df,centroids):
    #sqrt=((x2-x1)**2-(y2-y1)**2)
    for i in centroids.keys():
        df['distance_from_{}'.format(i)] = (
                                        np.sqrt(
                                            (df['x'] - centroids[i][0]) ** 2
                                                + (df['y'] - centroids[i][1]) ** 2
                                                                   ) )
        centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()] 
    #create new column closest which indicates min distance value    
    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x : int(x.lstrip('distance_from_')))
    df['color'] = df['closest'].map(lambda x: colmap[x])
    return df
    
print("Before assignment dataset");
print(df)
df = assignment(df, centroids)
print("After assignment dataset");
print(df)

#plot the graph for assigned dataset
fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.title("Marvellous : Dataset with clustering & random centroid");
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show() 

#Step 3: Update – The centroid of the clusters becomes the new mean Assignment and Update are repeated iteratively until convergence

old_centriod=copy.deepcopy(centroids)

def update(k):
    print("Old values of k,",k)
    for i in centroids.keys():
        centroids[i][0]=np.mean(df[df['closest']==i]['x'])
        centroids[i][1]=np.mean(df[df['closest']==i]['y'])
    print("values of new centriods,",k)
    return k
    
    
centroids=update(centroids)
    
fig = plt.figure(figsize=(5, 5))
ax = plt.axes()
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
    plt.xlim(0, 80)
    plt.ylim(0, 80)

#to display distance between old centroid and new centriod
for i in old_centriod.keys():
    old_x = old_centriod[i][0]
    old_y = old_centriod[i][1]
    dx = (centroids[i][0] - old_centriod[i][0]) * 0.75
    dy = (centroids[i][1] - old_centriod[i][1]) * 0.75
    ax.arrow(old_x, old_y, dx, dy, head_width=2, head_length=3, fc=colmap[i],ec=colmap[i])
plt.title("Marvellous : Dataset with clustering and updated centroids");
plt.show()  

## Repeat Assigment Stage
print("Before assignment dataset");
print(df)
df = assignment(df, centroids)
print("After assignment dataset");
print(df) 

# Plot results
fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
 plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.title("Marvellous : Dataset with clustering and updated centroids");
plt.show() 

# Continue until all assigned categories don't change any more 
while True:
    closest_centriods=df['closest'].copy(deep=True)
    centroids=update(centroids)
    df = assignment(df, centroids)
    print("After assignment dataset");
    print(df) 
    if closest_centriods.equals(df['closest']):
        break
print("Final values of centroids")
print(centroids)