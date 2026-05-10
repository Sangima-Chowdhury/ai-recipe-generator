from flask import Flask, render_template, request
from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    ingredients = request.form["ingredients"]

    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1500,
        messages=[
            {
                "role": "user",
                "content": f""" I have these ingredients: {ingredients}

Please suggest one meal I can make and give me:
1. The meal name
2. Any extra ingredients I might need (keep it minimal)
3. Step by step instructions
4. How long it takes

Keep it practical and simple, and make sure to use the ingredients I have as much as possible."""
            }
        ]
    )

    recipe = message.content[0].text
    return render_template("index.html", recipe=recipe, ingredients=ingredients)


if __name__ == "__main__":
    app.run(debug=True)
