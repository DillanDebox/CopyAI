# Copy AI 🤖📝

Copy AI is a Streamlit-based web application designed to help users generate creative and compelling copywriting content. Leveraging the power of OpenAI's GPT models, Copy AI offers customizable writing styles and creativity levels to tailor the output to the user's specific needs.

## Features

- **Custom Writing Styles**: Choose from a variety of writing styles to match your content needs.
- **Adjustable Creativity Level**: Slide to adjust the creativity level for more conservative or adventurous content generation.
- **Word Count Control**: Specify the exact number of words for the generated content.
- **Password Protection**: Secure access to ensure only authorized users can generate content.

## Installation

To run Copy AI locally, you need Python installed on your system. Follow these steps to set up the app:

1. **Clone the repository**:
   
   ```bash
   git clone https://github.com/DillanDebox/CopyAI
   cd path-to-your-app
   ```

2. **Install requirements**:

   Create a virtual environment and install the required packages:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Set up your `secrets.toml` for local development**:

   In the `.streamlit` directory at the root of your project, create a `secrets.toml` file with the following content:

   ```toml
   # .streamlit/secrets.toml
   OPENAI_API_KEY = "your_openai_api_key_here"
   password = "your_password_here"
   ```

   Replace `your_openai_api_key_here` and `your_password_here` with your actual OpenAI API key and desired password.

## Running the App

With your environment set up and secrets in place, run the app using Streamlit:

```bash
streamlit run streamlit_app.py
```

## Deployment

To deploy Copy AI to Streamlit Cloud or another platform, ensure you add your `OPENAI_API_KEY` and `password` to the platform's secrets management feature. This process varies by platform but typically involves accessing the app settings or configuration panel.

