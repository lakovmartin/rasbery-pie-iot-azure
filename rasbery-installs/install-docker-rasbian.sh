#!/bin/bash

# Update package lists
sudo apt-get update

# Install dependencies
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common

# Add Docker's official GPG key
curl -fsSL https://download.docker.com/linux/raspbian/gpg | sudo apt-key add -

# Add the Docker repository
echo "deb [arch=armhf] https://download.docker.com/linux/raspbian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list

# Update package lists again
sudo apt-get update

# Install Docker Engine
sudo apt-get install -y docker-ce docker-ce-cli containerd.io

# Create the Docker group
sudo groupadd docker

# Add user to docker group
sudo usermod -aG docker $USER

# Activate Changes to Group
newgrp docker

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Verify installation
echo "Docker version:"
docker --version
echo "Docker Compose version:"
docker compose --version
