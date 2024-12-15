# Chatbot MongoDB Integration

# 📜 Overview:
# This project demonstrates the integration of MongoDB with a chatbot to store and retrieve chat messages. 
# The chatbot stores chat data in MongoDB, and users can retrieve and view chat history via the MongoDB shell. 
# Docker is used to run MongoDB in a container, and the Python script interacts with MongoDB using the `pymongo` library.

# 🛠️ Setup Instructions:
# 
# **Prerequisites**:
# 1. **Docker**: To run MongoDB in a container. Download Docker from [here](https://www.docker.com/products/docker-desktop).
# 2. **Python 3.x**: Install Python on your machine. The script requires the `pymongo` library to interact with MongoDB. Install it using:
#    ```bash
#    pip install pymongo
#    ```
# 3. **MongoDB**: The project uses MongoDB to store chatbot messages. Docker will be used to run MongoDB in a container.
# 
# 🏗️ Project Setup:
# 1️⃣ Setting Up MongoDB with Docker:
# Follow these steps to set up MongoDB in a Docker container:
# 
# Pull the MongoDB Docker image:
#    ```bash
#    docker pull mongo
#    ```
# 
# Run the MongoDB container:
#    ```bash
#    docker run --name my-mongo-container -d -p 27017:27017 mongo
#    ```
# 
# Verify MongoDB is running:
#    ```bash
#    docker ps
#    ```
# You should see `my-mongo-container` listed as running.
# 
# 2️⃣ Running the Python Script:
# Once MongoDB is running, you can execute the Python script `chatbot_mongo.py` to simulate the chatbot and store chat messages.
# 
# Clone or download the repository to your local machine.
# Navigate to the directory where `chatbot_mongo.py` is located.
# Run the Python script:
#    ```bash
#    python chatbot_mongo.py
#    ```
# This script will simulate a chatbot and store chat messages in MongoDB.

# 🗂️ File Structure:
# 
# Chatbot_Mongo_Assignment/
#   ├── chatbot_mongo.py             # Python script for chatbot MongoDB integration
#   ├── screenshots/                 # Folder containing MongoDB data screenshots
#   │    ├── cmd_chat_history        # MongoDB data screenshot 1
#   │    ├── vscode_output_history       # MongoDB data screenshot 2
#   └── README.md                    # This README file

# 🧑‍💻 Interacting with MongoDB in Docker:
# To interact with MongoDB and retrieve chat history, follow these steps:
# 
# Access MongoDB Shell: Open the terminal and run the following command to access the MongoDB shell inside the container:
#    ```bash
#    docker exec -it my-mongo-container mongo
#    ```
# 
# Use the Chatbot Database: Switch to the chatbot database:
#    ```bash
#    use chatbot
#    ```
# 
# Retrieve the Chat History: Use the following command to display the chat history:
#    ```bash
#    db.chat_history.find().pretty()
#    ```
# This will display all the chat messages stored in the `chat_history` collection in a formatted, human-readable way.
# 
# 📸 Screenshots:
# Here are some screenshots showing the chat history stored in MongoDB:
# - **Screenshot 1**: [cmd_chat_history](cmd_chat_history)
# - **Screenshot 2**: [vscode_output_history](vs_code_output_history)
# 🔧 Retrieving and Viewing Chat History Using CMD:
# To retrieve and view the chat history using the command line, follow these steps:
# 
# Access MongoDB:
#    ```bash
#    docker exec -it my-mongo-container mongo
#    ```
# Switch to the chatbot database:
#    ```bash
#    use chatbot
#    ```
# Find and display the chat history:
#    ```bash
#    db.chat_history.find().pretty()
#    ```
# This will display the stored chat history in a readable format.

# 💡 Conclusion:
# By following these steps, you will successfully integrate MongoDB into your chatbot to store and retrieve chat history. 
# The Python script utilizes the `pymongo` library to interact with MongoDB, while Docker makes setting up MongoDB easy and efficient.

# 📞 Contact:
# For any questions or issues, feel free to reach out to the project author:
# **Name**: Amit Kumar
# **Email**: amitk25783@example.com
# Mob - +91 7673825079

# --- Code Implementation Starts Below ---
import pymongo
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['chatbot']
chat_history = db['chat_history']

# Function to store a chat message in MongoDB
def store_message(user_message, bot_response):
    chat_message = {
        "user_message": user_message,
        "bot_response": bot_response
    }
    chat_history.insert_one(chat_message)
    print("Message stored in MongoDB!")

# Function to retrieve chat history from MongoDB
def get_chat_history():
    for chat in chat_history.find():
        print(f"User: {chat['user_message']}")
        print(f"Bot: {chat['bot_response']}")
        print("-" * 40)

# Simulating a chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    bot_reply = f"Bot response to: {user_input}"
    print(f"Bot: {bot_reply}")
    store_message(user_input, bot_reply)

# Retrieve and display chat history
print("\nChat History:")
get_chat_history()
