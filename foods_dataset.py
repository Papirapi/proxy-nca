import os
import pandas as pd
import numpy as np

path = "/content/proxy-nca/foods/images"
img_paths = []
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.jpg' in file:
            files.append(os.path.join(r, file))

for f in files:
    d = (f.split("/",5)[-1])
    img_paths.append(d)
data = pd.DataFrame(img_paths)

data[1]=(np.divmod(np.arange(len(data)),100)[0]+1)-1
data.to_csv('/content/proxy-nca/foods/food.csv',index=False)
