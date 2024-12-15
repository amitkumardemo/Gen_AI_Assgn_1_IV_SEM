from pymongo import MongoClient
from datetime import datetime

# MongoDB Configuration
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "chatbot"
COLLECTION_NAME = "chat_history"

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# Function to store a message
def store_message(conversation_id, sender, message):
    """
    Store a single message in the chat history.
    Args:
        conversation_id (str): Unique identifier for the conversation.
        sender (str): 'user' or 'bot'.
        message (str): Message text.
    """
    try:
        timestamp = datetime.utcnow().isoformat()
        # Check if conversation exists
        conversation = collection.find_one({"conversation_id": conversation_id})
        
        if conversation:
            # Append to existing messages
            collection.update_one(
                {"conversation_id": conversation_id},
                {"$push": {"messages": {"sender": sender, "message": message, "timestamp": timestamp}}}
            )
        else:
            # Create a new conversation
            new_conversation = {
                "conversation_id": conversation_id,
                "messages": [{"sender": sender, "message": message, "timestamp": timestamp}]
            }
            collection.insert_one(new_conversation)
        
        print(f"Message stored for conversation ID: {conversation_id}")
    except Exception as e:
        print(f"Error storing message: {e}")

# Function to fetch chat history
def fetch_chat_history(conversation_id):
    """
    Fetch chat history for a given conversation.
    Args:
        conversation_id (str): Unique identifier for the conversation.
    Returns:
        list: List of messages in the conversation.
    """
    try:
        conversation = collection.find_one({"conversation_id": conversation_id})
        if conversation:
            return conversation["messages"]
        else:
            print("No conversation found with the given ID.")
            return []
    except Exception as e:
        print(f"Error fetching chat history: {e}")
        return []

# Close MongoDB connection
def close_connection():
    client.close()

# Example Usage
if __name__ == "__main__":
    # Example conversation ID
    convo_id = "abc123"
    
    # Storing messages
    store_message(convo_id, "user", "Hello!")
    store_message(convo_id, "bot", "Hi! How can I help you?")
    store_message(convo_id, "user", "Tell me about MongoDB.")
    store_message(convo_id, "bot", "MongoDB is a NoSQL database.")

    # Fetching chat history
    history = fetch_chat_history(convo_id)
    print("Chat History:")
    for msg in history:
        print(f"[{msg['timestamp']}] {msg['sender'].capitalize()}: {msg['message']}")
    
    # Close connection
    close_connection()
