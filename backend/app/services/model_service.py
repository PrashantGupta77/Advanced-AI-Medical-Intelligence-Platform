import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import numpy as np

from PIL import Image

import tensorflow as tf

# Limit TensorFlow memory usage on Render
tf.config.threading.set_intra_op_parallelism_threads(1)
tf.config.threading.set_inter_op_parallelism_threads(1)


from tensorflow.keras.models import load_model

from tensorflow.keras.applications.efficientnet import preprocess_input

from app.config import settings



class ModelService:


    def __init__(self):

        self.model = load_model(
            settings.MODEL_PATH,
            compile=False
        )

        print("Medical AI Model Loaded")


    def preprocess_image(self, image_path):

        img = Image.open(
            image_path
        ).convert("RGB")


        img = img.resize(
            (224,224)
        )


        img_array = np.array(
            img
        )


        img_array = np.expand_dims(
            img_array,
            axis=0
        )


        img_array = preprocess_input(
            img_array
        )


        return img_array



    def predict(self, image_path):


        img_array = self.preprocess_image(
            image_path
        )


        prediction = self.model(
            img_array,
            training=False
        ).numpy()[0][0]


        if prediction >= 0.5:

            result = "PNEUMONIA"

            confidence = float(prediction)


        else:

            result = "NORMAL"

            confidence = float(1-prediction)



        return {
            "prediction": result,
            "confidence": round(confidence * 100, 2), 
            "model": "EfficientNetB0"
        }



model_service = ModelService()