from typing import List
from cluster import Cluster
from data import images, clusters


def get_clustered(image_list: List[list], cluster_list: List[Cluster]):
    clustered = cluster_list[:]

    for image_ in image_list:
        distances = [cluster.get_distance(image_) for cluster in cluster_list]
        minimum = min(distances)
        index = distances.index(minimum)
        clustered[index].add_image(image_)

    return clustered


classificated = get_clustered(images, clusters)

if __name__ == '__main__':

    for i, each in enumerate(classificated):
        print(f"Class {str(i + 1)}:")
        for image in each.images:
            print(list(image), end=', ')
        print()
