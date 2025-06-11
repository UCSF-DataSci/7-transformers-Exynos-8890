# utils/test_chat.py

import os
import csv
from pathlib import Path
from keys import HF_API_KEY  # Import your Hugging Face API key

# Import our chat modules - since we're in the same directory
from one_off_chat import get_response as get_one_off_response
# Optionally import the conversation module if testing that too
# from conversation import get_response as get_contextual_response

def test_chat(questions, model_name= 'command-r-plus-04-2024', api_key= HF_API_KEY):
    """
    Test the chat function with a list of questions

    Args:
        questions: A list of questions to test
        model_name: Name of the model to use
        api_key: API key for authentication

    Returns:
        A dictionary mapping questions to responses
    """
    results = {}
    print(HF_API_KEY)

    for question in questions:
        print(f"Testing question: {question}")
        assert type(question) == str, "Question must be a string"
        # Get response using the one-off chat function
        response = get_one_off_response(question, api_key, model_name=model_name)
        results[question] = response

    return results

def save_results(results, output_file="results/part_2/example.txt"):
    """
    Save the test results to a file

    Args:
        results: Dictionary mapping questions to responses
        output_file: Path to the output file
    """
    with open(output_file, 'w') as f:
        # Write header
        f.write("# LLM Chat Tool Test Results\n\n")

        # Write usage examples
        f.write("## Usage Examples\n\n")
        f.write("```bash\n")
        f.write("# Run the one-off chat\n")
        f.write("python utils/one_off_chat.py\n\n")
        f.write("# Run the contextual chat\n")
        f.write("python utils/conversation.py\n")
        f.write("```\n\n")

        # Write test results
        f.write("## Test Results\n\n")
        f.write("```csv\n")
        f.write("question,response\n")

        for question, response in results.items():
            # Format the question and response for CSV
            q = question.replace(',', '').replace('\n', ' ')
            r = response.replace(',', '').replace('\n', ' ')
            f.write(f"{q},{r}\n")

        f.write("```\n")

if __name__ == "__main__":
    # List of healthcare questions to test
    test_questions = [
        "What are the symptoms of gout?",
        "How is gout diagnosed?",
        "What treatments are available for gout?",
        "What lifestyle changes can help manage gout?",
        "What foods should be avoided with gout?"
    ]

    results = test_chat(test_questions)
    save_results(results)
    print("Test results saved to results/part_2/example.txt")
