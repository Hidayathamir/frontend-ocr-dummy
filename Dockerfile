FROM python:3.10.5

WORKDIR /app

COPY ./main.py .

COPY ./mypackage ./mypackage

COPY ./temp_img ./temp_img

RUN pip3 install streamlit

CMD streamlit run main.py
