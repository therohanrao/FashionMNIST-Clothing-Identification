import tensorflow as tf
from tensorflow import keras
import numpy as np
from matplotlib import pyplot as plt

mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# "normalizing" to make all values between 0 and 1 instead of 0 and 255
train_images = train_images / 255.0
test_images = test_images / 255.0

# To display images :
plt.imshow(train_images[0]) # a shoe
plt.show(block=True)
plt.imshow(train_images[42]) # another shoe
plt.show(block=True)
# End of display code

model = keras.models.Sequential([keras.layers.Flatten(),

                                keras.layers.Dense(128, activation=tf.nn.relu),
                                keras.layers.Dense(10, activation=tf.nn.softmax)])
model.compile(optimizer = keras.optimizers.Adam(),
              loss = 'sparse_categorical_crossentropy',
              metrics = ['accuracy'])
model.fit(train_images, train_labels, epochs=5)

model.evaluate(test_images, test_labels)
