FROM python:3.10

RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p pdfs

EXPOSE 8501

CMD ["streamlit", "run", "streamlit.py"]
