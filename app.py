import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
import time

## Function to generate response

def getLLMResponse(input_text, no_of_words, article_type):
    ## LLama2 Model GGML
    llm = CTransformers(model="TheBloke/Llama-2-7B-Chat-GGUF",
                        config={'max_new_tokens': 4096, 'temperature': 0.07, 'context_length': 4096})
    
    ## Prompt Template
    
    prompt_template = """
    You are capable of writing the blog, research abstract and technical documents.
    Write a {article_type} on topic {input_text} with only max {no_of_words} number of words.
    In case of writing the blogs, keep homourand make sure that you are just not cross the line of wits.
    However in terms research abstract or technical documentation, keep it highly professional.
    """

    prompt = PromptTemplate(input_variables=["article_type", "input_text", "no_of_words"], template=prompt_template)

    ## Generating the response
    print(prompt.format(article_type=article_type, input_text=input_text, no_of_words=no_of_words))

    response = llm(prompt.format(article_type=article_type, input_text=input_text, no_of_words=no_of_words))
    print(response)
    return response

st.set_page_config(page_title="Harsh Generation App",
                   layout="centered",
                   initial_sidebar_state='collapsed')

st.header("	:pencil: :pencil: Blog/Research Paper/Technical Documentation Generation App :pencil: :pencil:", divider='rainbow')
input_text = st.text_input("Enter the topic :writing_hand:")
col1,col2=st.columns([5,5])
with col1:
    no_of_words=st.text_input('No of words')
with col2:
    article_type = st.selectbox('Article type', 
                              ('Blog','Research Paper abstract','Technical Documentation'),
                              index=0
                              )
generate_string = "Generate " + article_type + " :male-scientist:"

submit = st.button(generate_string)

def stream_data(response):
    for word in response.split(" "):
        yield word + " "
        time.sleep(0.02)

if submit:   
    st.write_stream(stream_data(getLLMResponse(input_text, no_of_words, article_type)))


st.write("Made with Love by **Harsh** :sunglasses:")