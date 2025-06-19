import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt
from call_function import available_functions
from call_function import call_function

def main():

    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):   
    model_name = "gemini-2.0-flash-001"
    config_type = types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
    

    try:
        response = client.models.generate_content(model=model_name, contents=messages, config=config_type)
        if not response.function_calls:
            return response.text
        for function_call_part in response.function_calls:
            function_call_response = call_function(function_call_part, verbose)
            if not function_call_response.parts[0].function_response.response:
                raise Exception("Missing response")
            if verbose:
                 print(function_call_response.parts[0].function_response.response)
        if verbose:

            print("Prompt tokens:", response.usage_metadata.prompt_token_count)
            print("Response tokens:", response.usage_metadata.candidates_token_count)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
