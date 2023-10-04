import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain

MAX_TEMP = 1.5
MAX_VALUE = 100

def main():
    st.set_page_config(layout="centered", page_title="Hotel AI",page_icon="🏠")
    st.title("Copy Write 📝")

    openai_api_key = st.sidebar.text_input("OpenAI API Key", type= "password")

    writing_style_options = ["Blogging", "Boutique", "Business", "Creative", "Descriptive", "Elegant", "Exclusive", "Expository", "Journalistic", "Luxurious", "Narrative", "Persuasive", "Poetic", "Technical"]
    writing_styles = st.multiselect("Select writing styles", options=writing_style_options)
    creativity = st.slider("Creativity", min_value=0,max_value=MAX_VALUE,value=80,format="%d%%")
    word_count = st.slider("Word Count", min_value=0,max_value=2000,value=500,format="%d words")
    description = st.text_area("Provide a brief description of the the task at hand:")

    prompt_template = """
    You are a highly skilled copywriter with a strong background in persuasive writing, conversion optimization, and marketing techniques.
    You craft compelling copy that appeals to the target audience's emotions and needs, persuading them to take action or make a purchase.
    You understand the importance of AIDA (Attention, Interest, Desire, and Action) and other proven copywriting formulas, and seamlessly incorporate them into your writing.
    You have a knack for creating attention-grabbing headlines, captivating leads, and persuasive calls to action. 
    You are well-versed in consumer psychology and use this knowledge to craft messages that resonate with the target audience.
    Your job is to write copy using the following writing styles: {writing_styles}
    Use the following format:
    ## Title

    Text

    Here is a brief description of the task:
    {description}

    The word count should be {word_count} words
    """

    if openai_api_key:
        if st.button("Generate"):
            custom_prompt = PromptTemplate(template=prompt_template, input_variables=["writing_styles", "description","word_count"])
            llm = ChatOpenAI(temperature=creativity/(1/MAX_TEMP*MAX_VALUE), model="gpt-3.5-turbo", openai_api_key=openai_api_key)

            llm_chain = LLMChain(
                llm = llm,
                prompt=custom_prompt,
            )
            with st.spinner("Fetching response..."):
                llm_response = llm_chain.run(writing_styles=writing_styles, description=description, word_count=word_count)
                st.write(llm_response)


if __name__ == '__main__':
    main()