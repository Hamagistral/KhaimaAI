import streamlit as st
import openai
import pandas as pd

from streamlit_chat import message
from dotenv import load_dotenv

from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType


load_dotenv()

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

openai.api_key = OPENAI_API_KEY

st.set_page_config(page_title="Morocco Disaster", page_icon="🇲🇦")

col1, col2, col3, col4, col5 = st.columns(5)
with col3:
    st.image("https://i.ibb.co/Df19cyK/khaimaAI.png")

st.header("💬 Chatbot")

st.markdown("Our chatbot is your virtual assistant in times of need. It's here to help you find the essential resources you require after a natural disaster, such as food, water, and medical supplies. You can also ask about the nearest locations with extra resources, ensuring you get the support you need quickly. Whether it's crucial information or a friendly virtual hand, our chatbot is ready to assist you, anytime, anywhere.")

st.markdown("> Note: This is a fictif data and not a real one, just for the sake of prototyping")

st.markdown("---")

show_df = st.toggle("Show dataframe")

if show_df:
    df = pd.read_csv("streamlit/data/KhaimaAI - AllDouars.csv") # './data/KhaimaAI - AllDouars.csv' for local run
    
    # Define a custom function to format the contact_info values
    def format_contact_info(value):
        cleaned_value = value.replace('\u202F', '').replace(',', '')
        return f"+{int(cleaned_value)}"

    # Apply the custom function to the "contact_info" column
    df['contact_info'] = df['contact_info'].apply(format_contact_info)

    st.dataframe(df)

if 'generated' not in st.session_state:
    st.session_state['generated'] = ["👋🏻 Hi! I am KhaimaAI, how can I help you ?"]

if 'past' not in st.session_state:
    st.session_state['past'] = ['Hello !']

# Layout of input/response containers
input_container = st.container()
response_container = st.container()

def get_text():
    question = st.text_input("You : ", "", key="input")
    return question

with input_container:
    user_input = get_text()
    send = st.button("Send")

def generate_response(prompt):
    agent = create_csv_agent(
        ChatOpenAI(model="gpt-3.5-turbo"),
        "streamlit/data/KhaimaAI - AllDouars.csv",
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
    )

    response = agent.run(prompt)

    return response

## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if send and user_input:
        try:
            response = generate_response(user_input)
        except:
            response = "Sorry I don't have the answer for that 😞"
            
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            message(st.session_state["generated"][i], key=str(i), avatar_style="bottts-neutral", seed=90)
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user', avatar_style="avataaars-neutral", seed=10)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
