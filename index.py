import os
import numpy as np
from skimage import io, color, transform
from skimage.io import imread, imsave
from sklearn.linear_model import OrthogonalMatchingPursuit
from scipy.fft import fft2, ifft2
from scipy.fftpack import dct, idct
import pywt
from skimage import img_as_ubyte
import matplotlib.pyplot as plt
import streamlit as st
from io import BytesIO
from skimage import io  # Add this line
from tensorflow.keras.models import load_model
from PIL import Image



# Set page configuration - This should be the first Streamlit command
st.set_page_config(
    page_title="CS-CNNVisionHub! 🚀: Lung Cancer Classification and Information",
    page_icon="🔬",
    layout="centered",
    initial_sidebar_state="collapsed"
    # initial_sidebar_state="expanded",
)

# Import necessary libraries
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Function to preprocess the input image
def preprocess_image(img):
    img = cv2.resize(img, (224, 224))
    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

# Load the saved model
# model_path = r"Code/final_modelDCTOMP90.h5"


# loaded_model = load_model(model_path)

# Function to get recommendations based on predicted lung cancer type
def get_recommendations(predicted_class):
    recommendations = {
        'out_lung_aca': "Adenocarcinoma is commonly associated with non-smokers. It's essential to consult with a healthcare professional for further evaluation.",
        'out_lung_n': "Squamous Cell Carcinoma (SCC) is often linked to smoking. If you are a smoker, consider discussing smoking cessation strategies with your doctor.",
        'out_lung_scc': "Large Cell Carcinoma is a less common but aggressive subtype. Early intervention and consultation with an oncologist are crucial for appropriate management."
    }
    return recommendations.get(predicted_class, "No specific recommendations for the predicted type.")


# Streamlit app content
st.title("CS-CNNVisionHub! 🚀") 
st.header("Lung Cancer Classification and Information")

st.caption("""CS-CNNVisionHub! 🚀 is Lung Cancer Classification and Information portal for detecting lung cancer using CNN (Convolutional Neural Network), which processes data that has undergone Compressive Sensing""")

# Add a divider after the main title
st.markdown("<hr/>", unsafe_allow_html=True)

st.sidebar.title("CS-CNNVisionHub! 🚀")
st.sidebar.caption("""Created in 2023, this is a portal for the Thesis ("CS-based Lung Classification Using CNN")💡 made by Andi Ainun Najib, a Master's student in Electrical Engineering at Telkom University.""")


# Add a divider after the main title
st.sidebar.markdown("<hr/>", unsafe_allow_html=True)

# st.sidebar.header("Contact Information")
# Sidebar image
# st.sidebar.image("Code/11.png", width=100, caption="")
# Sidebar links
st.sidebar.title("About Author")
st.sidebar.caption("""Andi Ainun Najib
                    (2101211017)""")

# st.sidebar.subheader("Anda dapat menghubungi saya")

# Adding links with Font Awesome icons
with st.sidebar.expander("See My Social Media Account🏆"):
    st.caption("Linkedin [Andi Ainun Najib](https://www.linkedin.com/in/andi-ainun-najib-220b58201/)")
    st.caption("Check out the accompanying Portfolio [here](andiainunnajib.github.io/MyPortofolio).")

with st.sidebar.expander("See My Other Streamlit Apps🏆"):
    st.caption("Sophisticated Palette: [App](https://sophisticated-palette.streamlit.app/) 🎈,  [Blog Post](https://blog.streamlit.io/create-a-color-palette-from-any-image/) 📝")
    # st.caption("Wordler: [App](https://wordler.streamlit.app/) 🎈,  [Blog Post](https://blog.streamlit.io/the-ultimate-wordle-cheat-sheet/) 📝")
    # st.caption("Koffee of the World: [App](https://koffee.streamlit.app/) 🎈")
   
with st.sidebar.expander("ℹ️ **Latest CNN Classification Release Notes**📅"):
    st.markdown("""Stay frosty and keep up with the coolest updates on the CNN portal [here](andiainunnajib.github.io/MyPortofolio).""")
cols = st.columns(2);

st.sidebar.info("""All for this portal CS-CNNVisionHub! 🚀 
                For further inquiries or additional information,
                please feel free to contact me. Your feedback and 
                suggestions are valuable in enhancing the platform's content and usability.""")

with st.sidebar.expander("Acknowlegde👍"):
    st.markdown(""" I would like to express my heartfelt gratitude to my parents, whose unwavering support and encouragement have been a constant source of inspiration throughout the development of the Lung Cancer Classification and Information portal. Your belief in my endeavors has been a driving force, and I am deeply thankful for your love and encouragement.

        A special thanks goes to my closest friends who provided valuable insights, constructive feedback, and moral support. Your friendship has been a pillar of strength, and I appreciate the camaraderie that fueled my motivation.

        This portal is a culmination of collective efforts, and I extend my appreciation to everyone who contributed, directly or indirectly, to its realization. Your support has been instrumental in bringing this project to fruition.

        Thank you, from the bottom of my heart.
        """)

st.image("Code/User guide.png", width=400, caption="Flow Using CS-CNNVisionHub! 🚀", use_column_width=True)

_, exp_col, _ = st.columns([1,3,1])
with exp_col:
    with st.expander("**📖 User Guide : How to Use This Cheat Sheet**"):
        st.markdown("""
                    However you like! 🤷🏻

                    But here's my recommendation:

                    1. This portal predicts the outcome of images that have undergone compressive sensing. 
                    
                    - Therefore, if you want to try compressive sensing, you can go to the compressive sensing tab and choose an image from the [histopathology image link](https://drive.google.com/drive/folders/1fOHSwspuFb1Wj_47PEAioyJYII26VepO?usp=sharing).
                    - If you do not want to perform compressive sensing but want the direct result from compressive sensing, I provide images that have [already undergone compressive sensing](https://drive.google.com/drive/folders/1yV-ckSX1jHRLWS8Nrjq8D7aYP9fSHgaq?usp=drive_link).
                    """)
        
        st.info("""
                Compressive sensing  images take a long time, so I recommend using the images that have already undergone compressive sensing available at the [link](https://drive.google.com/drive/folders/1yV-ckSX1jHRLWS8Nrjq8D7aYP9fSHgaq?usp=drive_link).
                """)
        
        st.markdown("""
                    2. Then, perform compressive sensing on the image you want to use for cancer classification in the Compressive sensing tab.

                    3. Choose the type of compressive sensing you want to perform in Classification tab. then process the data from the compressive sensing. 

                    4. Take the classification results/download data compressed, 

                    5. Go to tab Classification and choose method base on dataset that you already compressed. then process the data from the to detect the type of cancer disease in the given image using classification CNN.

                    6. Classification data result🚀
 
                    👈 Don't forget to check the sidebar for additional info and layout options!

                    Now, go build something awesome on CS-CNNVisionHub! 🚀

                    """)

# Add a divider after the main title
# st.markdown("<hr/>", unsafe_allow_html=True)
st.header("Choose tab you want access🔎")
# Tab layout with horizontal tabs
About_tab, cs_tab ,clas_tab, desc_tab, cv_tab = \
st.tabs(["About","Compressive Sensing","Classification", "Classification Explanations","Authors"])
# Add a divider after the main title
st.markdown("<hr/>", unsafe_allow_html=True)    

# Expander for About tab
with About_tab:
    st.info("About Lung Cancer Classification and Information App")

    # Explanation for Compressive Sensing
    with st.expander("Compressive Sensing (CS)"):
        st.subheader("Compressive Sensing (CS)")
        st.write("CS is a signal processing technique that allows for the reconstruction of a signal or image "
                 "from a small set of linear, non-adaptive measurements. It is useful in reducing data storage and transmission requirements.")
        st.markdown("### Objectives")
        st.write("The main goal of using CS in this application is to compress medical images for efficient storage and processing.")
        st.markdown("### Workflow")
        st.write("1. **Image Upload:** Users can upload medical images for compressive sensing.")
        st.write("2. **Compression Methods:** Users can choose between DCT, DWT, and FFT for image compression.")
        st.write("3. **Compression and Reconstruction:** The chosen compression method is applied, and the compressed image is reconstructed.")
        st.write("4. **Download:** Users can download the processed image.")

    
    # Explanation for CNN
    with st.expander("Convolutional Neural Network (CNN)"):
        st.subheader("Convolutional Neural Network (CNN)")
        st.write("CNN is a type of deep learning algorithm commonly used for image classification tasks. "
                 "It is particularly effective in capturing spatial hierarchies and patterns in images.")
        st.markdown("### Objectives")
        st.write("The main goal of using CNN in this application is to classify lung cancer types based on medical images.")
        st.markdown("### Workflow")
        st.write("1. **Image Preprocessing:** Input images are resized and normalized to prepare them for the model.")
        st.write("2. **Model Loading:** A pre-trained CNN model is loaded to make predictions.")
        st.write("3. **Prediction:** The uploaded medical image is processed by the model to predict the lung cancer type.")
        st.write("4. **Recommendations:** Based on the prediction, relevant recommendations for the predicted cancer type are provided.")

      # Mode Design & Implementation
    with st.expander("Model Design & Implementation"):
        st.subheader("Model Design & Implementation")
        st.write("The CNN model used in this application is designed for the classification of lung cancer types "
                 "from medical images. The model architecture is based on deep learning principles, utilizing convolutional layers, "
                 "pooling layers, and fully connected layers.")
        st.write("1. **Model Architecture:** The CNN model consists of multiple convolutional layers to capture hierarchical features "
                 "in the input images. Pooling layers are used for down-sampling and reducing dimensionality.")
        st.write("2. **Training:** The model is trained on a dataset of labeled medical images to learn the patterns associated with "
                 "different lung cancer types.")
        st.write("3. **Transfer Learning:** Transfer learning may be employed, using a pre-trained model on a large dataset to leverage "
                 "knowledge from a related task.")
        st.write("4. **Fine-Tuning:** The model may be fine-tuned on the specific dataset used in this application for improved performance.")
        
        # Display image related to Model Design & Implementation
        st.image("Code/about.png", use_column_width=True, caption="Model Design & Implementation", output_format="JPEG", width=500)

    # Application Objectives
    st.markdown("### Application Objectives🎯")
    # st.markdown("<hr/>", unsafe_allow_html=True)
    st.write("1. Provide a user-friendly interface for predicting lung cancer types from medical images.")
    st.write("2. Utilize CNN for accurate and efficient image classification.")
    st.write("3. Implement CS to compress medical images, reducing storage and processing requirements.")

    # Workflow Summary
    st.markdown("### Workflow Summary📣")
    # st.markdown("<hr/>", unsafe_allow_html=True)
    st.write("1. **Compressive Sensing:** Users can compress medical images using various methods.")
    st.write("2. **CNN Classification:** Users can predict lung cancer types from medical images.")
    st.write("3. **Recommendations:** Relevant recommendations are provided based on the predicted cancer type.")

    # Output Example
    st.markdown("### Output Example📉")
    # st.markdown("<hr/>", unsafe_allow_html=True)
    st.write("The application displays the predicted lung cancer type and provides recommendations for further actions.")

# Expander for Compressive Sensing tab
with cs_tab:
    st.info("Tips 💡: Compressive sensing  images take a long time, so I recommend using the images that have already undergone compressive sensing available at the [link](https://drive.google.com/drive/folders/1yV-ckSX1jHRLWS8Nrjq8D7aYP9fSHgaq?usp=drive_link). but If you want to prosess compressive sensing you can get [original dataset](https://drive.google.com/drive/folders/1fOHSwspuFb1Wj_47PEAioyJYII26VepO?usp=drive_link) and you can process compressive sensing by yourself")

    # Choice between DCT, DWT, and FFT
    method_choice = st.radio("Select Compression Method:", ["DCT", "DWT", "FFT"])

    # Upload image through Streamlit for Compressive Sensing
    uploaded_cs_image = st.file_uploader("Upload image for Compressive Sensing...", type=["jpg", "jpeg", "png"])

    if uploaded_cs_image is not None:
        # Display the uploaded image
        st.image(uploaded_cs_image, caption="Uploaded Image for Compressive Sensing.", use_column_width=True)

        # Load and convert the uploaded image to grayscale
        A = imread(uploaded_cs_image)
        Abw = color.rgb2gray(A)

        # Resize the original image
        Anew = transform.resize(Abw, (int(Abw.shape[0] * 0.2), int(Abw.shape[1] * 0.2)))

        # Display the resized image
        # st.image(Abw, caption='Original Image', use_column_width=True)

        # Apply compression method based on user choice
        if method_choice == "DCT":
            # Apply DCT to the resized image
            coeffs = dct(dct(Anew, axis=0, norm='ortho'), axis=1, norm='ortho')

            # Flatten DCT coefficients
            A_flat = coeffs.flatten()

            # Apply Orthogonal Matching Pursuit (OMP)
            compression_ratio = 0.90
            n_nonzero_coefs = int(1 - compression_ratio * len(A_flat))
            omp = OrthogonalMatchingPursuit(n_nonzero_coefs=n_nonzero_coefs)
            omp.fit(np.identity(len(A_flat)), A_flat)

            # Reconstruct the image using the selected DCT coefficients
            selected_indices = omp.coef_ != 0
            A_reconstructed_flat = np.zeros_like(A_flat)
            A_reconstructed_flat[selected_indices] = omp.coef_[selected_indices]
            A_reconstructed = A_reconstructed_flat.reshape(coeffs.shape)

            # Apply inverse DCT to get the final image
            A_final = idct(idct(A_reconstructed, axis=0, norm='ortho'), axis=1, norm='ortho')

        elif method_choice == "DWT":

            # Apply DWT to the resized image
            n = 4
            w = 'db1'
            coeffs = pywt.wavedec2(Anew, wavelet=w, level=n)

            # Convert coefficients to a 1D array
            coeff_arr, coeff_slices = pywt.coeffs_to_array(coeffs)

            # Sort coefficients by magnitude
            Csort = np.sort(np.abs(coeff_arr.reshape(-1)))

            compression_ratio = 0.90
            # Thresholding
            thresh = Csort[int(np.floor((1 - compression_ratio) * len(Csort)))]
            ind = np.abs(coeff_arr) > thresh
            Cfilt = coeff_arr * ind

            # Convert modified coefficients back to original format
            coeffs_filt = pywt.array_to_coeffs(Cfilt, coeff_slices, output_format='wavedec2')

            # Reconstruct the image
            # A_dwt_reconstructed = pywt.waverec2(coeffs_filt, wavelet=w)

            # # Resize the reconstructed image to 153x153
            # A_dwt_reconstructed = transform.resize(A_dwt_reconstructed, (153, 153))

            # Apply OMP for sparse signal reconstruction
            X = Cfilt.reshape(-1, 1)
            omp = OrthogonalMatchingPursuit(n_nonzero_coefs=int(X.size * (1 - compression_ratio)))
            omp.fit(np.eye(X.size), X.flatten())
            coef_omp = omp.coef_
            X_omp = np.dot(np.eye(X.size), coef_omp)
            X_omp = X_omp.reshape(Cfilt.shape)

            # Convert OMP modified coefficients back to original format
            coeffs_omp = pywt.array_to_coeffs(X_omp, coeff_slices, output_format='wavedec2')

            # Reconstruct the image with OMP
            A_dwt_reconstructed_omp = pywt.waverec2(coeffs_omp, wavelet=w)

            # Resize the reconstructed image with OMP to 153x153
            A_final = transform.resize(A_dwt_reconstructed_omp, (153, 153))

        elif method_choice == "FFT":
            # Apply FFT to the resized image
            coeffs = fft2(Anew)

            # Flatten FFT coefficients
            A_fft_flat = coeffs.flatten()

            # Compute the magnitude of the FFT coefficients
            magnitude_A_fft_flat = np.abs(A_fft_flat)

            # Create an instance of the OMP model
            compression_ratio = 0.90
            n_nonzero_coefs = int(1 - compression_ratio * len(A_fft_flat))
            omp = OrthogonalMatchingPursuit(n_nonzero_coefs=n_nonzero_coefs)
            omp.fit(np.identity(len(A_fft_flat)), magnitude_A_fft_flat)

            # Reconstruct the image using the selected FFT coefficients
            selected_indices = omp.coef_ != 0
            A_fft_reconstructed_flat = np.zeros_like(A_fft_flat)
            A_fft_reconstructed_flat[selected_indices] = omp.coef_[selected_indices]
            A_fft_reconstructed = A_fft_reconstructed_flat.reshape(coeffs.shape)

            # Apply inverse FFT to get the final image
            A_final = np.real(ifft2(A_fft_reconstructed))

            # Normalize and clip the final image to [0.0, 1.0]
            A_final_normalized = (A_final - np.min(A_final)) / (np.max(A_final) - np.min(A_final))
            # Clip the final image to [0.0, 1.0]
            A_final_clamped = np.clip(A_final_normalized, 0.0, 1.0)

            # Display the clipped image using streamlit
            st.image(A_final_clamped, caption=f'Reconstructed Image ({method_choice})', use_column_width=True)

        # Download button for the processed image
        if st.button(f"Processed Image ({method_choice})"):
            # Convert the image to bytes
            img_bytes = BytesIO()
            io.imsave(img_bytes, (A_final * 255).astype(np.uint8), format="png")

            # Trigger the download
            st.download_button(
                label=f"Download Processed Image ({method_choice})",
                data=img_bytes.getvalue(),
                file_name=f"Reconstructed_{method_choice}_{uploaded_cs_image.name}",
                key="download_processed_image",
            )

            
# Expander for Classification tab
with clas_tab:
    st.info("Tips 💡: Predict lung cancer type and get recommendations. Pick Compresion Methode Based. For example you have Compression Image Using DCT, so the CNN has to be DCT to. I provide Image that already Compressed in [link](https://drive.google.com/drive/folders/1yV-ckSX1jHRLWS8Nrjq8D7aYP9fSHgaq?usp=drive_link)")
    # Get the selected compression method
    methodCNN_choice = st.radio("Select Compression Method Based On Image CS that you want predict:", ["DCT", "DWT", "FFT"], key="methodCNN")
    
    # Apply compression method based on user choice
    if methodCNN_choice == "DCT":
        model_path = r"Code/final_modelDCTOMP70.h5"
        # Load the saved model
        loaded_model = load_model(model_path)
        # Upload image through Streamlit
        uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

        if uploaded_image is not None:
            # Display the uploaded image
            st.image(uploaded_image, caption="Uploaded Image.", use_column_width=True)

            # Convert the uploaded image to a format that the model can use
            image = Image.open(uploaded_image)
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

            # Make predictions
            preprocessed_image = preprocess_image(image)
            predictions = loaded_model.predict(preprocessed_image)

            # Get the predicted class
            predicted_class = np.argmax(predictions, axis=1)[0]

            # Map the predicted class index to the actual class label
            class_folders = ['out_lung_aca', 'out_lung_n', 'out_lung_scc']
            predicted_label = class_folders[predicted_class]

            # Display the predicted class label
            st.markdown("#### Prediction Lung Cancer type📣")
            st.write("Predicted Class:", predicted_label)
            st.markdown("<hr/>", unsafe_allow_html=True)

            # Get recommendations based on predicted lung cancer type
            st.markdown("#### Recommendation Medical📣")
            recommendations = get_recommendations(predicted_label)
            st.write("Recommendations:", recommendations)

    # Apply compression method based on user choice
    if methodCNN_choice == "DWT":
        model_path = r"Code/final_modelDWTOMP70.h5"
        # Load the saved model
        loaded_model = load_model(model_path)
        # st.image("Code/graph.png", width=400, caption="Training & Validation Grafik", use_column_width=True)
        # Upload image through Streamlit
        uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

        if uploaded_image is not None:
            # Display the uploaded image
            st.image(uploaded_image, caption="Uploaded Image.", use_column_width=True)

            # Convert the uploaded image to a format that the model can use
            image = Image.open(uploaded_image)
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

            # Make predictions
            preprocessed_image = preprocess_image(image)
            predictions = loaded_model.predict(preprocessed_image)

            # Get the predicted class
            predicted_class = np.argmax(predictions, axis=1)[0]

            # Map the predicted class index to the actual class label
            class_folders = ['out_lung_aca', 'out_lung_n', 'out_lung_scc']
            predicted_label = class_folders[predicted_class]

            # Display the predicted class label
            st.markdown("#### Prediction Lung Cancer type📣")
            st.write("Predicted Class:", predicted_label)
            st.markdown("<hr/>", unsafe_allow_html=True)

            # Get recommendations based on predicted lung cancer type
            st.markdown("#### Recommendation Medical📣")
            recommendations = get_recommendations(predicted_label)
            st.write("Recommendations:", recommendations)

    # Apply compression method based on user choice
    if methodCNN_choice == "FFT":
        model_path = r"Code/final_modelFFTTOMP70.h5"
        # Load the saved model
        loaded_model = load_model(model_path)
        # Upload image through Streamlit
        uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

        if uploaded_image is not None:
            # Display the uploaded image
            st.image(uploaded_image, caption="Uploaded Image.", use_column_width=True)

            # Convert the uploaded image to a format that the model can use
            image = Image.open(uploaded_image)
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

            # Make predictions
            preprocessed_image = preprocess_image(image)
            predictions = loaded_model.predict(preprocessed_image)

            # Get the predicted class
            predicted_class = np.argmax(predictions, axis=1)[0]

            # Map the predicted class index to the actual class label
            class_folders = ['out_lung_aca', 'out_lung_n', 'out_lung_scc']
            predicted_label = class_folders[predicted_class]

            # Display the predicted class label
            st.markdown("#### Prediction Lung Cancer type📣")
            st.write("Predicted Class:", predicted_label)
            st.markdown("<hr/>", unsafe_allow_html=True)

            # Get recommendations based on predicted lung cancer type
            st.markdown("#### Recommendation Medical📣")
            recommendations = get_recommendations(predicted_label)
            st.write("Recommendations:", recommendations)

# Expander for Classification Explanations tab
# Expander for Classification tab
with desc_tab:
    st.info("Learn about lung cancer types and their explanations.")
    col1, col2, col3 = st.columns(3)
    # Explanation for Adenocarcinoma
     # Explanation for Adenocarcinoma
    with st.expander("Adenocarcinoma"):
        st.subheader("Adenocarcinoma")
        col1.image("Code/lungaca1.png", use_column_width=True, caption="Adenocarcinoma", output_format="JPEG", width=200)
        with st.container():
            st.markdown("### Explanation")
            st.write("Adenocarcinoma is a type of lung cancer that originates in the mucus-secreting cells of the lungs. "
                     "It is commonly associated with non-smokers.")
            st.markdown("### Recommendations")
            st.write("Consult with a healthcare professional for further evaluation. Treatment may involve surgery, chemotherapy, or targeted therapies.")                
            st.markdown("### Medications")
            st.write("Specific medications may be prescribed based on the individual's condition. Consult a healthcare professional for personalized advice.")

    # Explanation for Squamous Cell Carcinoma (SCC)
    with st.expander("Squamous Cell Carcinoma"):
        st.subheader("Squamous Cell Carcinoma (SCC)")
        col2.image("Code/lungscc1.png", use_column_width=True, caption="Squamous Cell Carcinoma", output_format="JPEG", width=200)
        with st.container():
            st.markdown("### Explanation")
            st.write("Squamous Cell Carcinoma (SCC) is a type of lung cancer that often arises in the bronchial tubes. "                         
                     "It is commonly linked to smoking.")
            st.markdown("### Recommendations")
            st.write("If you are a smoker, consider discussing smoking cessation strategies with your doctor. "
                     "Treatment may involve surgery, radiation, or chemotherapy.")  
            st.markdown("### Medications")                
            st.write("Medications may be prescribed as part of the treatment plan. Consult a healthcare professional for personalized advice.")

    # Explanation for Large Cell Carcinoma
    with st.expander("Large Cell Carcinoma"):
        st.subheader("Large Cell Carcinoma")
        col3.image("Code/lungaca1.png", use_column_width=True, caption="Large Cell Carcinoma", output_format="JPEG", width=200)
        with st.container():
            st.markdown("### Explanation")
            st.write("Large Cell Carcinoma is a less common but aggressive subtype of lung cancer. "                         
                     "It tends to grow and spread quickly.")
            st.markdown("### Recommendations")
            st.write("Early intervention and consultation with an oncologist are crucial for appropriate management. "
                     "Treatment may involve surgery, chemotherapy, or targeted therapies.")            
            st.markdown("### Medications")
            st.write("Medications may be part of the treatment plan. Consult a healthcare professional for personalized advice.")

# Expander for CV Authors tab
with cv_tab:
  
    
    with st.expander("Intorduction"):
        st.markdown("#### Authors Contibution")
        st.info("The research represents a collaborative contribution involving three individual, including Prof. Dr. Indrarini Dyah Irawati., S.T., M.T., Dr. Gelar Budiman, S.T., M.T., and Andi Ainun Najib, S.T.")
        st.write("1. **Prof. Dr. Indrarini Dyah Irawati., S.T., M.T.** designed the experiments, analyzed the data, reviewed drafts of the article, and approved the final draft.")
        st.write("2. **Dr. Gelar Budiman, S.T., M.T.** performed the computation work, authored, or reviewed drafts of the article, and approved the final draft.")
        st.write("3. **Andi Ainun Najib, S.T.** performed the experiments, get analyze dataset process, make model CNN, and created portal prepared figures and/or tables, and approved the final draft.")


    # Information about the CV author
    st.image("Code/1.png", width=400, caption="Andi Ainun Najib", use_column_width=True)
    st.markdown("<hr/>", unsafe_allow_html=True)
    # st.subheader("Andi Ainun Najib")
    
    # Description
    st.markdown("### About Me")
    st.info("Hello 👋, I am a Telecommunication Engineer and Electrical Engineer, programmer and data enthusiast, started my career as an Telecommunication Engineer and graduated from Telkom University in Bandung," 
            "Indonesia. I am an active person, sociable, happy with calculations and logic, and like to improve myself to develop further."
            "I am a passionate data scientist with a strong background in machine learning and deep learning. "
            "My expertise lies in developing and deploying AI solutions for various domains. Now I Work in BNI as IT Asset Management")

    st.markdown("<hr/>", unsafe_allow_html=True)
    # Experience
    st.markdown("### Experience")
    st.text("PT. Telkom Indonesia Divre 7💡")
    st.markdown("- Student Intern")
    st.caption("June 2019 - July 2019")
    st.caption("Working on data Enterprise Goverment and Business (EGBIS) at Telkom service purchase data, confirm payments and arrears for each Witel Regional Account Manager Divre 7, Create work orders, and record partner work letters.")
    st.text("Telkom DDS (Divisi Digital Service)📊")
    st.markdown("- Student Intern🧑‍💻")
    st.caption("Juni 2020 - July 2020")
    st.caption("Intern at Unit Energy & Device. Conducting research and searching for data related to lithium-ion, regulations in the deployment of electronic lithium battery manufacturing tools (ITU.T). Make presentation from data research.")
    st.text("Basic Transmission Laboratory")
    st.markdown("- Coordinator Laboratory🌐")
    st.caption("March 2020 - March 2021")
    st.caption("Coordinating divisions in the Basic Transmission laboratory. Making modules, creating admin content, and testing lab tools and applications. Controlling laboratory.")
    st.text("PT. Telkom Indonesia")
    st.markdown("- Data Visualization & Data Analyst📊")
    st.caption("September 2021 - December 2021")
    st.caption("Intern in HCBP I unit. Used python and data company (employe), clean, filtering, visualization, and analyze large datasets. Cleaning and filtering data with python (pandas, NumPy) and Matplotlib. Make Machine learning supervised (XGBoost, Decision Tree) for predict promotable employee, and unsupervised (K-means) to clustering critical division")
    st.text("Bank Negara Indonesia (BNI)")  
    st.markdown("- Officer Development Program📚")
    st.caption("Mei 2022 - Mei 2023")
    st.caption("Officer Development Program BNI, for future leader BNI")
    st.markdown("- IT Enterprise Architecture📑")
    st.caption("Mei 2022 - Juli 2023")
    st.caption("""Work as IT Enterprise Architecture,
        - Architectural Design and Planning: Proficient in designing robust and scalable IT architecture solutions based on business requirements and existing architectural conditions.
        - Standard Adherence: Ensure project delivery adheres to established IT architecture standards and reference models, guaranteeing consistency and compatibility.
        - Collaboration and Coordination: Work closely with the Unit Strategic Partner to provide advisory and solutions to LoB for delivery projects, ensuring alignment with IT architecture principles.
        - Technical Expertise: Possess in-depth knowledge of application and infrastructure architecture, systems integration, and project management.
        - Stakeholder Engagement: Skilled in effectively engaging with stakeholders to understand their needs and provide tailored architecture solutions.
        -Being part of IT Culture IT Strategy & Architecture""")
    st.markdown("- IT Asset Management🤖")
    st.caption("Juli 2023 - Now")
    st.caption("Tracking, managing, and optimizing an organization's information technology (IT) assets throughout their lifecycle. IT assets can include hardware devices (such as computers, servers, printers, and networking equipment), software licenses, applications, digital documents, and even virtual assets like cloud resources. The primary goal of ITAM is to ensure that an organization's IT assets are utilized efficiently, economically, and in compliance with relevant regulations and licensing agreements.")
    # ... add more experiences

    st.markdown("<hr/>", unsafe_allow_html=True)
    # Education
    st.markdown("### Education")
    st.text("Master of Science in Electrical Engineering, Telkom University, Indonesia (2022)")
    st.text("Bachelor of Telecommucation Engineering, Telkom University, Indonesia (2021)")

    # # Certifications
    # st.markdown("### Certifications")
    # st.text("- Certified Machine Learning Engineer (Certification Body, Year)")
    # st.text("- Deep Learning Specialization (Coursera, Year)")
    # # ... add more certifications
