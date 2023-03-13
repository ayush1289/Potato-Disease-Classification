from fastapi import FastAPI, File, UploadFile
from enum import Enum
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL =tf.keras.models.load_model("/home/ayush/Documents/Disease_Classifcation/model/2")



CLASS_NAMES = ["Early Blight","Late Blight","Healthy"]

@app.get("/")
async def root():
    return "this is home"

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.post("/predict")
async def predict(files: UploadFile = File(...)):
    data = read_file_as_image(await files.read())
    img_batch = np.expand_dims(data, 0)
    prediction = MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(prediction[0])]
    confidence = np.max(prediction[0])

    return {
        'class': predicted_class,
        'confidence':float(confidence)
    }



if __name__ == "__main__":
    uvicorn.run(app, host = 'localhost', port = 8000)


