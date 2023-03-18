import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

MODEL =tf.keras.models.load_model("model/2")

CLASS_NAMES = ["Early Blight","Late Blight","Healthy"]



st.title('POTATO DISEASE CLASSIFICATION')


image = st.file_uploader("please upload image here!", type =["png","jpeg","jpg"])
if image is not None:
   image = image.read()
   img = Image.open(BytesIO(image))
   st.image(img, caption='Uploaded Image')
   
   img_batch = np.expand_dims(img, 0)
   prediction = MODEL.predict(img_batch)
   predicted_class = CLASS_NAMES[np.argmax(prediction[0])]
   confidence = np.max(prediction[0])

   st.text(predicted_class)
   st.text(confidence)

    
    