# Build:

docker build --pull --rm -f "autoGenTestCases/Dockerfile" -t testgenie:latest "autoGenTestCases" 

# Run: 

docker run -p 8501:8501 testgenie:latest 

# Browser:

http://localhost:8501/


# Notes:
Internally it runs : streamlit run  streamlit_app.py --server.enableCORS false --server.enableXsrfProtection false


