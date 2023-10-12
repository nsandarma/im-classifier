from tensorflow import keras
from keras.models import load_model

model = load_model('model-men-vs-women.h5')
print(model.__getstate__())