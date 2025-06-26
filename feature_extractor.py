import numpy as np
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.utils import image
from numpy.linalg import norm

class VGGNet:
    def __init__(self):
        self.model = VGG16(weights='imagenet', include_top=False, pooling='max')

    def extract_feat(self, img_path):
        img = image.load_img(img_path, target_size=(224, 224))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = preprocess_input(img)
        features = self.model.predict(img)[0]
        norm_feat = features / norm(features)
        return norm_feat