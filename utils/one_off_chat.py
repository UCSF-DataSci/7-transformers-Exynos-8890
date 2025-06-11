# utils/one_off_chat.py
import argparse
import requests
from keys import HF_API_KEY
API_URL = "https://router.huggingface.co/cohere/compatibility/v1/chat/completions"
# from keys import HF_API_KEY  # Import your Hugging Face API key

def get_response(prompt:str,api_key, model_name="command-r-plus-04-2024"):
    """
    Get a response from the model

    Args:
        prompt: The prompt to send to the model
        model_name: Name of the model to use
        api_key: API key for authentication (optional for some models)

    Returns:
        The model's response
    """
    # TODO: Implement the get_response function
    # Set up the API URL and headers
    # Create a payload with the prompt
    # Send the payload to the API
    # Extract and return the generated text from the response
    # Handle any errors that might occur
    headers = {"Authorization": f"Bearer {api_key}"}  # Optional for some models
    payload = {
        'messages': [
            {'role': 'user', 'content': prompt}
        ],
        'model': model_name
    }
    response= requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        response = response.json()
        return response['choices'][0]['message']['content']
    else:
        print("error", response.status_code, response.text)
        return None
    pass

def run_chat(api_key):
    """Run an interactive chat session"""
    print("Welcome to the Simple LLM Chat! Type 'exit' to quit.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # TODO: Get response from the model
        response = get_response(user_input, api_key)
        if response:
            print(f"Model: {response}")
        else:
            print("Model: Sorry, I couldn't process that.")

def main():
    parser = argparse.ArgumentParser(description="Chat with an LLM")
    # TODO: Add arguments to the parser
    parser.add_argument('--prompt', type=str,default= '', help='Initial prompt to send to the model')
    parser.add_argument('--key', type=str, default= HF_API_KEY ,help='Hugging Face API key (required)')
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
   

