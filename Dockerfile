# Use a base image with Python
FROM python:3.12.7-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    g++ \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# RUN mkdir -p /app/models

# Script to download models
# RUN python download_models.py

EXPOSE 8501

# Command to run the Streamlit app

# CMD ["streamlit","run", "app.py"]
RUN pip install dvc[s3] streamlit


CMD ["sh", "-c", "dvc remote add myremote s3://dvc-models-rag &&
dvc pull && streamlit run app.py"]