FROM python:3.12.4

# Copy the requirements.txt file into tmp directory
COPY requirements.txt /tmp/requirements.txt

# Upgrade pip and install requirements.txt
RUN python -m pip install --no-cache-dir --upgrade pip &&\
    python -m pip install --no-cache-dir --timeout 3000000 -r /tmp/requirements.txt

# Copy the entire project
COPY . /app

# Set up the working directory
WORKDIR /app

# Expose the correct port (8501 for Streamlit)
EXPOSE 8501

# Run the Streamlit application on port 8501
CMD ["streamlit", "run", "main.py", "--server.port", "8501"]
