import os
import openai

openai.api_key = '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'

try:

    # retrieve all models
    models = openai.Model.list()

    # print the list of models
    for model in models['data']:
        print(model['id'])

except openai.error.AuthenticationError as e:
    print(f"Error: {e}.\nPlease ensure that you have set a valid OpenAI API key.")
except openai.error.OpenAIError as e:
    print(f"Error: {e}.\nPlease check your OpenAI API credentials and try again.")
except Exception as e:
    print(f"Unexpected error occurred: {e}.")
