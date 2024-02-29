import streamlit as st
import easyocr
import io  
from PIL import Image
import numpy as np
import time

st.title("Image to text")

# Create a file uploader
# uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# # Display the uploaded image
# if uploaded_file is not None:
#     st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)


# # Initialize EasyOCR reader
# reader = easyocr.Reader(['en'])

# # Read text from an image
#results = reader.readtext(uploaded_file)

# # Print the detected text
# for result in results:
#     print(result[1])


# Create a file uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Display the uploaded image
if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

    # Convert uploaded file to bytes
    image_bytes = uploaded_file.read()

    # Open image with PIL (Python Imaging Library)
    image = Image.open(io.BytesIO(image_bytes))

    image_np = np.array(image)

    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en'])

    def extract_text(image):
        # Read text from the image
        results = reader.readtext(image_np)

        # Display the detected text
        extr_text = " "
        for result in results:
            extr_text += result[1] + "\n"

        return extr_text
    with st.spinner("Loading..."):
        extr_text = extract_text(image_np)
        time.sleep(2)
    
 # Display extracted text in a text box
    st.text_area("Extracted Text", value=extr_text, height=200)