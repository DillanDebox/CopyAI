import hmac
import random
import streamlit as st
from openai import OpenAI

MAX_TEMP = 1.5
MAX_VALUE = 100

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False

def generate(api_key, system_prompt, prompt, creativity=80):
    response = OpenAI(api_key=api_key).ChatCompletion.create(
        model="gpt-4-0125-preview",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        temperature=creativity/(1/MAX_TEMP*MAX_VALUE),
    )
    return response.choices[0].message.content.strip()


def main():
    st.set_page_config(layout="centered", page_title="Copy AI",page_icon="🤖")
    st.title("Copy AI 🤖📝")

    openai_api_key = st.secrets["OPENAI_API_KEY"]

    writing_style_options = ["Adventurous", "Article", "Blogging", "Boutique", "Business", "Creative", "Descriptive", "Editorial", "Elegant", "Exclusive", "Expository", "Journalistic", "Luxurious", "Narrative", "Persuasive", "Poetic", "Technical"]
    styles = st.multiselect("Select styles:", options=writing_style_options)
    creativity = st.slider("Creativity", min_value=0,max_value=MAX_VALUE,value=80,format="%d%%")
    word_count = st.slider("Word Count", min_value=100,max_value=2000,value=500,format="%d words")
    task = st.text_area("Provide a brief description of the the task at hand:", placeholder="Enter text here...")
    example = st.text_area("Provide an example of good writing for context:", placeholder="Enter text here...")


    system_prompt = """You are a highly skilled copywriter with a strong background in persuasive writing, conversion optimization, and marketing techniques. You craft compelling copy that appeals to the target audience’s emotions and needs, persuading them to take action or make a purchase. You understand the importance of AIDA (Attention, Interest, Desire, and Action) and other proven copywriting formulas, and seamlessly incorporate them into your writing. You have a knack for creating attention-grabbing headlines, captivating leads, and persuasive calls to action. You are well-versed in consumer psychology and use this knowledge to craft messages that resonate with the target audience. Your output should be tailored to the specific brand voice and marketing objectives of each client. Use markdown for headings and plain text for the body"""

    prompt = f"""
    # TASK:
    {task}

    # STYLE:
    Use the following suggested writing styles: {styles}

    # EXAMPLE:
    Example of good writing:
    "{example}"

    # WORD COUNT:
    The word count should be exactly {word_count} words.
    """

    messages = [
    "Marching through the vast scrolls of the Roman Empire to uncover your response...",
    "Ink is flowing, preparing the perfect prose...",
    "Summoning the literary muses for inspiration...",
    "Wielding the pen of creativity for your response...",
    "Typing at the speed of imagination for your answer...",
    "Weaving a tapestry of words to fetch your response...",
    "Crafting a symphony of syllables for your enlightenment...",
    "Brewing the alphabet soup of ideas for your request...",
    "Sculpting the clay of language to deliver your response..."]

    if openai_api_key:
        if st.button("Generate"):
            try:
                message = random.choice(messages)
                with st.spinner(message):
                    response = generate(openai_api_key, system_prompt.strip(), prompt.strip(), creativity)
                    st.write(response)
            except:
                st.warning("Incorrect API key")

if not check_password():
    st.stop()  # Prevent access to the app if password check fails

if __name__ == '__main__':
    main()