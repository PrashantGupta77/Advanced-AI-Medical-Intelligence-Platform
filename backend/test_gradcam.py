from app.services.gradcam_service import gradcam_service


image_path = "../data/sample_images/normal_example.jpeg"


result = gradcam_service.generate_gradcam(
    image_path
)


print("Grad-CAM saved at:")
print(result)