import requests
import json
import sys

SERVER_URL = "http://localhost:8080/completion"  # Adjust if your port is different

SYSTEM_PROMPT = """You are a helpful AI assistant engaged in a casual conversation. 
Respond naturally and concisely to the user's input. For greetings or simple queries, 
keep responses brief and friendly."""

def send_message(message, conversation_history):
    full_prompt = f"{SYSTEM_PROMPT}\n\nConversation:\n{conversation_history}\nHuman: {message}\nAssistant:"
    
    data = {
        "prompt": full_prompt,
        "temperature": 0.7,
        "max_tokens": 150,  # Adjust as needed
        "stop": ["\nHuman:", "\n\nHuman:"]  # Helps prevent the model from continuing the conversation on its own
    }
    response = requests.post(SERVER_URL, json=data)
    if response.status_code == 200:
        return response.json()['content'].strip()
    else:
        return f"Error: {response.status_code}"

def main():
    print("Welcome to the LlamaFile Chat Interface!")
    print("Type 'exit' to end the conversation.")
    
    conversation_history = ""
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            break
        
        response = send_message(user_input, conversation_history)
        print(f"\nAssistant: {response}")
        
        # Update conversation history
        conversation_history += f"Human: {user_input}\nAssistant: {response}\n"
        
        # Optionally, limit the conversation history to prevent it from growing too large
        conversation_history = conversation_history.split('\n')[-10:]  # Keep last 10 lines
        conversation_history = '\n'.join(conversation_history)

if __name__ == "__main__":
    main()