import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("model.h5")

# Image path
image_path = "/workspaces/Cat-Vs-Dog-Image-Classification-Project-/dataset/test/dogs/13.jpg"

# Open image
img = Image.open(image_path)

# Resize image
img = img.resize((150, 150))

# Convert to array
img_array = np.array(img)

# Normalize
img_array = img_array / 255.0

# Reshape for model
img_array = np.expand_dims(img_array, axis=0)

# Predict
prediction = model.predict(img_array)

# Output result
if prediction[0][0] > 0.5:
    print("Dog 🐶")
else:
    print("Cat 🐱")