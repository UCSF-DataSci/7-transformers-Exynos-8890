# utils/conversation.py

import requests
import argparse
import os
API_URL = "https://router.huggingface.co/cohere/compatibility/v1/chat/completions"
def get_response(prompt: str,api_key:str, history=None, model_name="command-r-plus-04-2024", history_length=3):
    """
    Get a response from the model using conversation history

    Args:
        prompt: The current user prompt
        history: List of previous (prompt, response) tuples
        model_name: Name of the model to use
        api_key: API key for authentication
        history_length: Number of previous exchanges to include in context

    Returns:
        The model's response
    """
    # TODO: Implement the contextual response function
    # Initialize history if None
    if history is None:
        history = list()
    history.append(
        {"role": "user", "content": prompt}
    )
    payload = {
        'messages': history[(history_length * -1):],
        'model': model_name,
    }

    # TODO: Format a prompt that includes previous exchanges
    # Get a response from the API
    # Return the response
    headers = {"Authorization": f"Bearer {api_key}"}  # Optional for some models
    response= requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        response = response.json()
        # print(response)
        return response['choices'][0]['message']['content']
    else:
        print("Failed to get a valid response from the model.")
        return None

def run_chat(api_key: str):
    """Run an interactive chat session with context"""
    print("Welcome to the Contextual LLM Chat! Type 'exit' to quit.")

    # Initialize conversation history
    history = []

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # TODO: Get response using conversation history
        response = get_response(user_input, api_key, history=history)
        if response:
            print(f"Model: {response}")
            history.append(
                {"role": "assistant", "content": response}
            )
            print(history)
        else:
            print("Model: Sorry, I couldn't process that.")

def main():
    parser = argparse.ArgumentParser(description="Chat with an LLM using conversation history")
    # TODO: Add arguments to the parser
    parser.add_argument('--prompt', type=str,default= '', help='Initial prompt to send to the model')
    parser.add_argument('--key', type=str, required = True ,help='Hugging Face API key (required)')
    args = parser.parse_args()
    key = args.key
    prompt = args.prompt

    # TODO: Run the chat function with parsed arguments
    if prompt == '':
        run_chat(api_key=key)
    else:
        response = get_response(prompt, key)
        if response:
            print(f"Model: {response}")
        else:
            print("Model: Sorry, I couldn't process that.")

if __name__ == "__main__":
    main()
