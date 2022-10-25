FROM python:3.10.7

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8501

COPY . /app

ENTRYPOINT [ "streamlit", "run", "streamlit.py" ]

CMD streamlit run streamlit.py