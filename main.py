import streamlit as st
import random
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain

MAX_TEMP = 1.5
MAX_VALUE = 100

def main():
    st.set_page_config(layout="centered", page_title="Copy Write",page_icon="📝")
    st.title("Copy Write 📝")

    openai_api_key = st.sidebar.text_input("OpenAI API Key", type= "password")

    writing_style_options = ["Blogging", "Boutique", "Business", "Creative", "Descriptive", "Elegant", "Exclusive", "Expository", "Journalistic", "Luxurious", "Narrative", "Persuasive", "Poetic", "Technical"]
    writing_styles = st.multiselect("Select writing styles", options=writing_style_options)
    creativity = st.slider("Creativity", min_value=0,max_value=MAX_VALUE,value=80,format="%d%%")
    word_count = st.slider("Word Count", min_value=100,max_value=2000,value=500,format="%d words")
    description = st.text_area("Provide a brief description of the the task at hand:")

    prompt_template = """
    You are a highly skilled copywriter with a strong background in persuasive writing, conversion optimization, and marketing techniques.
    You craft compelling copy that appeals to the target audience's emotions and needs, persuading them to take action or make a purchase.
    You understand the importance of AIDA (Attention, Interest, Desire, and Action) and other proven copywriting formulas, and seamlessly incorporate them into your writing.
    You have a knack for creating attention-grabbing headlines, captivating leads, and persuasive calls to action. 
    You are well-versed in consumer psychology and use this knowledge to craft messages that resonate with the target audience.
    Your job is to write copy using the following writing styles: {writing_styles}
    Use markdown for the heading and plain text for the body

    Here is a brief description of the task:
    {description}

    The word count should be {word_count} words
    """

    responses = [
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
                custom_prompt = PromptTemplate(template=prompt_template, input_variables=["writing_styles", "description","word_count"])
                llm = ChatOpenAI(temperature=creativity/(1/MAX_TEMP*MAX_VALUE), model="gpt-3.5-turbo", openai_api_key=openai_api_key)

                llm_chain = LLMChain(
                    llm = llm,
                    prompt=custom_prompt,
                )
                selected_response = random.choice(responses)
                with st.spinner(selected_response):
                    llm_response = llm_chain.run(writing_styles=writing_styles, description=description, word_count=word_count)
                    st.write(llm_response)
            except:
                st.warning("Incorrect API key")

if __name__ == '__main__':
    main()