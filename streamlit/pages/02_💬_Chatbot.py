import streamlit as st
import openai
import pandas as pd

from streamlit_chat import message
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType

from langchain.agents import create_csv_agent

load_dotenv()

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

openai.api_key = OPENAI_API_KEY

st.set_page_config(page_title="Morocco Disaster", page_icon="🇲🇦")

col1, col2, col3, col4, col5 = st.columns(5)
with col3:
    st.image("../assets/khaimaAI.png")

st.header("💬 Chatbot")

st.markdown("Our chatbot is your virtual assistant in times of need. It's here to help you find the essential resources you require after a natural disaster, such as food, water, and medical supplies. You can also ask about the nearest locations with extra resources, ensuring you get the support you need quickly. Whether it's crucial information or a friendly virtual hand, our chatbot is ready to assist you, anytime, anywhere.")

st.markdown("---")

show_df = st.toggle("Show dataframe")

if show_df:
    df = pd.read_csv("./data/KhaimaAI - AllDouars.csv")
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

def generate_response(prompt):
    agent = create_csv_agent(
        ChatOpenAI(model="gpt-4-0613"),
        "./data/KhaimaAI - AllDouars.csv",
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
    )

    response = agent.run(prompt)

    return response

## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            message(st.session_state["generated"][i], key=str(i), avatar_style="bottts-neutral", seed=90)
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user', avatar_style="avataaars-neutral", seed=10)