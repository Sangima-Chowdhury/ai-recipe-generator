# AI Recipe Generator

An AI-powered Flask web application that generates meal ideas based on ingredients entered by the user. The app uses the Anthropic Claude API to create practical recipes, cooking instructions, and ingredient suggestions.

## Features

- Enter ingredients you already have
- AI-generated recipe suggestions
- Step-by-step cooking instructions
- Estimated cooking time
- Suggests minimal extra ingredients if needed
- Clean and responsive user interface
- Dynamic rendering using Flask and Jinja templates

## Technologies Used

- Python
- Flask
- HTML & CSS
- Jinja2
- Anthropic Claude API
- dotenv
- Git & GitHub

## How It Works

1. User enters ingredients into the text box
2. Flask sends the ingredients to the Claude AI model
3. The AI generates:
   - Meal name
   - Extra ingredients needed
   - Step-by-step instructions
   - Cooking time
4. The recipe is displayed dynamically on the webpage

## What I Learned

This project helped me understand how AI APIs integrate into backend applications using Flask. I learned how to send prompts to an LLM, process AI responses, securely manage API keys using environment variables, and dynamically display generated content in a web application.

I also improved my understanding of:
- Flask routes
- POST requests
- Form handling
- Prompt engineering
- Template rendering
- Basic frontend styling

## Future Improvements

- User authentication
- Recipe history
- Save favourite recipes
- Image generation for meals
- Mobile responsive design improvements
- Deploy as a live web app


<img width="1352" height="878" alt="Screenshot 2026-05-10 at 22 52 20" src="https://github.com/user-attachments/assets/f68012d7-da6d-4018-a0c5-1e844e034ae4" />

<img width="1352" height="878" alt="Screenshot 2026-05-10 at 22 52 32" src="https://github.com/user-attachments/assets/89302d0b-e205-4381-ba81-43957e6ae937" />
