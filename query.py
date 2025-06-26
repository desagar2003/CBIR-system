import numpy as np
import h5py
from feature_extractor import VGGNet
from scipy.spatial.distance import cosine


def search(query_img_path, top_k=5):
    model = VGGNet()
    query_feat = model.extract_feat(query_img_path)

    with h5py.File('features.h5', 'r') as f:
        feats = f['features'][:]
        names = f['names'][:]

    scores = [1 - cosine(query_feat, feat) for feat in feats]
    top_indices = np.argsort(scores)[::-1][:top_k]

    results = []
    for idx in top_indices:
        name = names[idx]
        name = name.decode() if isinstance(name, bytes) else name
        results.append(name)

    return results