'''Create a startup script for AWS Metabase'''

# Download the Metabase file
wget https://downloads.metabase.com/v0.35.4/metabase.jar

# Update apt-get
sudo apt-get update -y
sudo apt-get upgrade -y

# Install java
sudo apt-get install -y openjdk-11-jre-headless

# Start Metabase
sudo nohup java -jar -DMB_JETTY_PORT=80 metabase.jar &
