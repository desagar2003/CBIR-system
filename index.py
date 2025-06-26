import os
import h5py
import numpy as np
from feature_extractor import VGGNet

img_dir = 'dataset/'
img_paths = [os.path.join(img_dir, img) for img in os.listdir(img_dir) if img.endswith(('.jpg', '.png'))]

feats = []
names = []
model = VGGNet()

for path in img_paths:
    print(f"Indexing: {path}")
    feat = model.extract_feat(path)
    feats.append(feat)
    names.append(os.path.basename(path))

feats = np.array(feats)
with h5py.File('features.h5', 'w') as f:
    f.create_dataset('features', data=feats)
    f.create_dataset('names', data=np.string_(names))