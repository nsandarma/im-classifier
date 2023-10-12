from tensorflow import keras
from keras.models import load_model
from keras.utils import load_img,img_to_array
import numpy as np


model = load_model('model-men-vs-women.h5')
def predict(path):

    img = load_img(path,target_size=(150,150))
    x = keras.utils.img_to_array(img)
    X = x
    x /= 255
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict(images)
    if classes[0] > 0.5:
        return "Perempuan"
    else:
        return "Laki-Laki"
