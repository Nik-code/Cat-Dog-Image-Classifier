from tensorflow import keras
import tensorflow as tf

# Don't forget to rename your model files as mentioned below
# If you want to run more or less models feel free to modify this code to add more or less model numbers, just add the 4
# lines, first assigning the model to an object
# then using model.predict function to get image prediction
# then score provided by the model as shown below
# and finally print out the score again as shown

model1 = keras.models.load_model('Model_1.keras')

model2 = keras.models.load_model("Model_2.keras")

model3 = keras.models.load_model("Model_3.keras")

image_size = (180, 180)

image_LOCATION = input('Enter path to image: ')

img = keras.preprocessing.image.load_img(
    F"{image_LOCATION}", target_size=image_size)
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)  # Create batch axis

predictions1 = model1.predict(img_array)
predictions2 = model2.predict(img_array)
predictions3 = model3.predict(img_array)

score1 = float(predictions1[0])
score2 = float(predictions2[0])
score3 = float(predictions3[0])

print(f"This image is {100 * (1 - score1):.2f}% cat and {100 * score1:.2f}% dog.")
print(f"This image is {100 * (1 - score2):.2f}% cat and {100 * score2:.2f}% dog.")
print(f"This image is {100 * (1 - score3):.2f}% cat and {100 * score3:.2f}% dog.")
