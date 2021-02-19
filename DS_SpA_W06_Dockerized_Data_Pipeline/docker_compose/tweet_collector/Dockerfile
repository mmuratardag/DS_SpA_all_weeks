# defines the baseline image

FROM python:3.8-slim

# WORKDIR <- name of working dir in container  # within the container the dir will b created
WORKDIR /app

# copy req. file from the tweet
COPY requirements.txt /app

# to install the req. libraries
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# execute the tweet_collector.py
CMD ["python", "tweet_collector.py"]