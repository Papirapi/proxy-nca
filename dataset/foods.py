import pandas as pd
from .base import *
import scipy.io

class Foods(BaseDataset):
    def __init__(self, root, classes, transform = None):
        BaseDataset.__init__(self, root, classes, transform)
        df = pd.read_csv('/content/proxy-nca/foods/food.csv')
        ys = df[df.columns[1]].values.tolist()
        im_paths = df[df.columns[0]].values.tolist()
        index = 0
        for im_path, y in zip(im_paths, ys):
            if y in classes: # choose only specified classes
                self.im_paths.append(os.path.join(root, im_path))
                self.ys.append(y)
                self.I += [index]
                index += 1

