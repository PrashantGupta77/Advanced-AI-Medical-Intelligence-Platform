import tensorflow as tf
import numpy as np
import cv2
import os

from PIL import Image

from app.services.model_service import model_service


OUTPUT_FOLDER = "outputs"

os.makedirs(
    OUTPUT_FOLDER,
    exist_ok=True
)



class GradCAMService:


    def __init__(self):

        self.model = model_service.model


    def generate_gradcam(
        self,
        image_path
    ):


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


        img_array = img_array / 255.0



        # EfficientNet last convolution layer

        last_conv_layer_name = "top_conv"



        grad_model = tf.keras.models.Model(

            inputs=self.model.inputs,

            outputs=[
                self.model.get_layer(
                    last_conv_layer_name
                ).output,

                self.model.output

            ]

        )



        with tf.GradientTape() as tape:


            conv_outputs, predictions = grad_model(
                [img_array]
            )


            loss = predictions[:,0]



        grads = tape.gradient(
            loss,
            conv_outputs
        )


        pooled_grads = tf.reduce_mean(
            grads,
            axis=(0,1,2)
        )


        conv_outputs = conv_outputs[0]


        heatmap = conv_outputs @ pooled_grads[..., tf.newaxis]


        heatmap = tf.squeeze(
            heatmap
        )


        heatmap = np.maximum(
            heatmap,
            0
        )


        heatmap /= np.max(
            heatmap
        )



        heatmap = cv2.resize(
            heatmap,
            (224,224)
        )


        img_original = cv2.imread(
            image_path
        )


        img_original = cv2.resize(
            img_original,
            (224,224)
        )


        heatmap = np.uint8(
            255 * heatmap
        )


        heatmap = cv2.applyColorMap(
            heatmap,
            cv2.COLORMAP_JET
        )


        superimposed_img = cv2.addWeighted(
            img_original,
            0.6,
            heatmap,
            0.4,
            0
        )


        output_path = os.path.join(
            OUTPUT_FOLDER,
            "gradcam_xray.jpeg"
        )


        cv2.imwrite(
            output_path,
            superimposed_img
        )


        return output_path.replace("\\", "/")



gradcam_service = GradCAMService()