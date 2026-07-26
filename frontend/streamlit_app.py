import streamlit as st
import requests
from PIL import Image
import pandas as pd
import io


import os

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://localhost:8000"
)



# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(

    page_title="AI Medical Intelligence Platform",

    page_icon="🏥",

    layout="wide",

    initial_sidebar_state="expanded"

)



# -----------------------------
# Custom CSS
# -----------------------------

st.markdown(
"""
<style>

.main-title {

    font-size:40px;
    font-weight:700;
    color:#0F4C75;

}


.card {

    padding:20px;

    border-radius:15px;

    background:#f8f9fa;

    box-shadow:0px 4px 12px rgba(0,0,0,0.1);

}


.metric {

    font-size:28px;

    font-weight:bold;

}


.report {

    background:#ffffff;

    padding:20px;

    border-radius:10px;

    border-left:5px solid #0F4C75;

}


</style>
""",
unsafe_allow_html=True
)



# -----------------------------
# Sidebar
# -----------------------------


with st.sidebar:


    st.title(
        "🏥 AI Medical Platform"
    )


    st.divider()


    st.subheader(
        "System Information"
    )


    st.success(
        "Backend Connected"
    )


    st.write(
        """
🧠 Model

EfficientNetB0


🔍 Explainability

Grad-CAM


🤖 Language Model

Llama 3.3


⚡ Framework

FastAPI + Streamlit
"""
    )



    st.divider()


    st.caption(
        "Advanced AI Medical Intelligence Platform v1.0"
    )





# -----------------------------
# Header
# -----------------------------


st.markdown(

"""
<div class="main-title">

🏥 Advanced AI Medical Intelligence Platform

</div>

AI-powered Chest X-Ray diagnosis system

"""

,
unsafe_allow_html=True
)



st.divider()



# -----------------------------
# Upload Section
# -----------------------------


st.subheader(
    "📤 Upload Chest X-Ray"
)



uploaded_file = st.file_uploader(

    "Upload X-ray image",

    type=[
        "jpg",
        "jpeg",
        "png"
    ]

)



if uploaded_file:


    image = Image.open(
        uploaded_file
    )


    col1, col2 = st.columns(
        2
    )


    with col1:

        st.image(

            image,

            caption="Original X-Ray",

            width="stretch"

        )



    with col2:


        st.info(
            """
Supported Model:

EfficientNetB0

Input Size:

224 × 224

Task:

Pneumonia Detection
"""
        )



    st.divider()



    if st.button(

        "🚀 Analyze X-Ray",

        width="stretch"

    ):



        with st.spinner(
            "Running AI analysis..."
        ):


            files = {

                "file":
                (

                    uploaded_file.name,

                    uploaded_file.getvalue(),

                    uploaded_file.type

                )

            }



            prediction_response = requests.post(

                f"{BACKEND_URL}/predict/",

                files=files

            )



        if prediction_response.status_code == 200:


            prediction_data = (

                prediction_response
                .json()["data"]

            )


            prediction = prediction_data["prediction"]

            confidence = prediction_data["confidence"]



            # -----------------------------
            # Prediction Result
            # -----------------------------


            st.subheader(
                "🧠 AI Prediction"
            )


            c1,c2,c3 = st.columns(3)



            with c1:


                st.metric(

                    "Prediction",

                    prediction

                )



            with c2:


                st.metric(

                    "Confidence",

                    f"{confidence}%"

                )



            with c3:


                if prediction=="NORMAL":

                    st.success(
                        "Low Risk"
                    )

                else:

                    st.error(
                        "Abnormal Finding"
                    )



            st.progress(

                int(confidence)/100

            )



            st.divider()



            # -----------------------------
            # GradCAM
            # -----------------------------


            st.subheader(

                "🔍 Explainable AI - Grad-CAM"

            )


            gradcam_path = (

                f"{BACKEND_URL}/"

                +

                prediction_data["gradcam_image"]

            )


            try:

                response = requests.get(
                    gradcam_path
                )

                if response.status_code == 200:

                    gradcam_image = Image.open(
                        io.BytesIO(response.content)
                    )

                    st.image(
                        gradcam_image,
                        caption="AI Attention Heatmap",
                        width=500
                    )

                else:

                    st.error(
                        f"GradCAM image loading failed: {response.status_code}"
                    )

            except Exception as e:

                st.error(
                    f"GradCAM error: {e}"
                )



            st.divider()



            # -----------------------------
            # LLM Report
            # -----------------------------


            st.subheader(

                "🤖 AI Medical Report"

            )



            report_response = requests.post(

                f"{BACKEND_URL}/report/",

                json={

                    "prediction":
                    prediction,

                    "confidence":
                    confidence

                }

            )



            if report_response.status_code == 200:


                report = (

                    report_response
                    .json()["medical_report"]

                )


                st.markdown(

                    f"""

<div class="report">

{report}

</div>

""",

                    unsafe_allow_html=True

                )



                st.download_button(

                    "📄 Download Report",

                    report,

                    file_name="medical_report.txt"

                )



else:


    st.info(

        "Please upload a chest X-ray image."

    )




# -----------------------------
# History
# -----------------------------


st.divider()


st.subheader(

    "📊 Prediction History"

)



if st.button(

    "Refresh History",

    width="stretch"

):


    response = requests.get(

        f"{BACKEND_URL}/history/"

    )


    if response.status_code == 200:


        history = response.json()



        df = pd.DataFrame(

            history

        )


        st.dataframe(

            df,

            width="stretch"

        )