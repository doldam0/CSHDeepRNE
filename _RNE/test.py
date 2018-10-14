from keras.models import load_model
from main import formatting_data
import numpy as np
import matplotlib.pyplot as plt

# Import model
print(" ## IMPORT MODEL ## ")
model = load_model('park_sick.h5')

# Testing
_test = ['쌀밥', '북어국', '시금치나물', '시금치나물', '시금치나물', '배추김치', '방울토마토', '', '', '3']
test = formatting_data(_test)
x = np.array([test[:9]])
y = model.predict(x)
print(" ## TEST RESULT ## ")
print(y)

result = np.argmax(y)
if result == 0:
    print('매우 적음')
elif result == 1:
    print('적음')
elif result == 2:
    print('보통')
elif result == 3:
    print('많음')
else:
    print('매우 많음')