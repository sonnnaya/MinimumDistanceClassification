import matplotlib.pyplot as plt
from main import classificated

image_clusters = [cluster.images for cluster in classificated]

x_es = [[image[0] for image in images] for images in image_clusters]
y_es = [[image[1] for image in images] for images in image_clusters]

for i in range(len(x_es)):
    plt.scatter(x_es[i], y_es[i])

plt.show()
