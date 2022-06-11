import json
import os

import streamlit as st

from mypackage.utility import do_ocr


TEMP_IMG_PATH = "temp_img"
st.title(body="NODEFLUX INTERN TIM A")
picture = st.camera_input(label="Silahkan foto KTP anda.")
if picture:
    st.image(picture)
    if st.button(label="Submit!"):
        new_temp_img_path = os.path.join(TEMP_IMG_PATH, os.urandom(12).hex() + ".jpg")
        with open(new_temp_img_path, "wb") as f:
            f.write(picture.getvalue())
        # OCR HERE
        with st.spinner("Doing OCR ..."):
            ocr_res = do_ocr(new_temp_img_path)
        st.success(body="OCR done! Click button bellow to download.")
        text_contents = json.dumps(ocr_res)
        st.download_button(
            label="Download OCR result", data=text_contents, file_name="OCR result.json"
        )
        os.remove(new_temp_img_path)
