import openai
from flask import Flask, render_template

# set the OpenAI API key
openai.api_key = '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'

# create Flask app
app = Flask(__name__)

# build HTML table of models
def build_model_table():
    try:
        # retrieve all models
        models = openai.Model.list()

        model_table = "<table style='border-collapse: collapse; width: 100%; border: 1px solid black;'>" \
                      "<tr style='background-color: #ddd;'>" \
                      "<th style='border: 1px solid black; padding: 10px;'>ID</th>" \
                      "<th style='border: 1px solid black; padding: 10px;'>Name</th>" \
                      "</tr>"
        for model in models['data']:
            model_id = model.get('id')
            model_name = model.get('display_name', model_id)
        
            model_table += f"<tr style='background-color: #f2f2f2;'>" \
                           f"<td style='border: 1px solid black; padding: 10px;'>{model_id}</td>" \
                           f"<td style='border: 1px solid black; padding: 10px;'>{model_name}</td>" \
                           "</tr>"
        model_table += "</table>"
    except openai.error.AuthenticationError as e:
        model_table = f"<p>Error: {e}. Please ensure that you have set a valid OpenAI API key.</p>"
    except openai.error.OpenAIError as e:
        model_table = f"<p>Error: {e}. Please check your OpenAI API credentials and try again.</p>"
    except Exception as e:
        model_table = f"<p>Unexpected error occurred: {e}.</p>"

    return model_table

# define route for index page
@app.route("/")
def index():
    model_table = build_model_table()
    return render_template("index.html", model_table=model_table)

# start web server
if __name__ == "__main__":
    app.run()
