# Stage 1: Build Python dependencies
# Use the specified image as the base
FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye AS builder

# Set the working directory to /tmp
WORKDIR /tmp

# Copy only the 'requirements.txt' to the builder stage
COPY requirements.txt .

# Install Python dependencies from 'requirements.txt'
RUN pip3 install --user -r requirements.txt

# Install Streamlit
RUN pip3 install --user streamlit

# Copy the rest of the files to the builder stage
COPY *.py .
COPY *.jpg .

# Stage 2: Final image
FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

# Copy Python dependencies from the builder stage
COPY --from=builder /root/.local /root/.local

# Copy the rest of the files to the container
COPY *.py /app/
COPY *.jpg /app/
COPY .streamlit/ /app/.streamlit

# Set the working directory
WORKDIR /app

# Set the PATH environment variable to include the directory where Streamlit is installed
ENV PATH=/root/.local/bin:$PATH

# Inform Docker that the container listens on port 8501 at runtime
EXPOSE 8501

# Command to run when the container starts
CMD ["streamlit", "run", "streamlit_app.py", "--server.enableCORS", "false", "--server.enableXsrfProtection", "false"]

# The command to run when the container starts
#docker run -p 8501:8501 autogentestcases:latest tail -f /bin/bash
#bash
#cd /app
#streamlit run  streamlit_app.py --server.enableCORS false --server.enableXsrfProtection false
###AIzaSyBAYlb1kH9bSFrMjYZbfKNOvc5O0m-6wEo

###latest: docker run -p 8501:8501 autogentestcases:latest 