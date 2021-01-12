from typing import List
import numpy as np


class Cluster:
    def __init__(self, standards: List[list]):
        self.standards: List[np.ndarray] = [np.array(each) for each in standards]
        self.images: List[np.ndarray] = []

    def get_distance(self, image: list):
        to_all_standards = [np.linalg.norm(np.array(image) - each) for each in self.standards]
        return min(to_all_standards)

    def add_image(self, image: list):
        self.images.append(np.array(image))
