import streamlit as st

st.set_page_config(page_title="Morocco Disaster", layout="wide", page_icon="🇲🇦")

col1, col2, col3, col4, col5 = st.columns(5)
with col3:
    st.image("https://i.ibb.co/Df19cyK/khaimaAI.png")

st.markdown('<h4 style="text-align: center;">"Service to others is the rent you pay for your room here on Earth." - Muhammad Ali</h4>', unsafe_allow_html=True)

st.markdown("<p style='text-align: center;'>Crisis Management Made Simple: KhaimaAI is a powerful disaster relief tool designed to assist authorities in efficiently managing temporary camps after natural disasters. It provides real-time data, resource optimization, and vital information, streamlining disaster response efforts and bringing aid where it's needed most.</p>", unsafe_allow_html=True)

st.markdown("## ❔ About KhaimaAI")

st.markdown("""### 🌋 Project for the Morocco Solidarity Hackathon 🤝

KhaimaAI is a cutting-edge solution developed as part of the Morocco Solidarity Hackathon. 
This innovative project aims to address a critical challenge faced in the aftermath of natural disasters: 
efficiently managing temporary camps for displaced individuals. KhaimaAI leverages advanced technology, data analytics, 
and real-time communication to provide a comprehensive disaster relief management system.""")

st.markdown("""#### 🎯 Our Solution
In the wake of natural disasters, the immediate needs of affected populations are paramount. KhaimaAI was conceived and built with a singular goal: to assist official authorities in managing temporary camps with maximum efficiency and effectiveness. Here's what TentAI offers:

- **Data Visualization:** KhaimaAI provides a user-friendly dashboard that visualizes crucial data, empowering authorities to make informed decisions regarding population management, healthcare resources, and more.

- **Resource Management:** Our platform enables real-time monitoring and management of essential resources such as food, water, and medicine. Predictive analytics help anticipate resource needs.

- **Chatbot Connectivity:** KhaimaAI integrates a chatbot that connects to a comprehensive database of other cities and villages affected by the disaster. Users can inquire about resources, find neighboring villages with surplus supplies, and facilitate resource-sharing.

- **Geospatial Information:** Leveraging geospatial data, KhaimaAI pinpoints the locations of temporary camps, neighboring villages, and available resources. Maps aid in resource allocation and emergency response.

- **Historical Data and Trend Analysis:** KhaimaAI maintains a historical database for trend analysis and continuous improvement of disaster response strategies.""")

st.markdown("""#### 👩‍👩‍👦‍👦 The Impact
KhaimaAI has the potential to make a profound impact in the field of disaster response and recovery. By streamlining resource management, enhancing communication, and optimizing decision-making, TentAI can:

- Save lives by ensuring the efficient distribution of critical resources.
- Reduce the suffering and vulnerability of disaster-affected populations.
- Improve the effectiveness and coordination of official disaster response efforts.
- Foster resilience and preparedness in communities facing future disasters.
- Serve as a model for humanitarian assistance and disaster response worldwide.""")

st.markdown("#### 👨‍💻 Meet the Team ")

st.image("https://i.ibb.co/W3GDf2k/Whats-App-Image-2023-09-17-at-19-56-29.jpg")

st.markdown("- **[EL BELGHITI Hamza](https://www.linkedin.com/in/hamza-elbelghiti/)**") 
st.markdown("- **[AKHMIM Abdelilah](https://www.linkedin.com/in/akhmim-abdelilah/)**")  
st.markdown("- **[OUJJIR Achraf](https://www.linkedin.com/in/achraf-oujjir/)** ")
st.markdown("- **[JAKOUK Hamza](https://www.linkedin.com/in/hamza-jakouk-5b4304202/)** ") 
st.markdown("- **[CHEMLAL Salim](https://www.linkedin.com/in/salimchemlal/)**   (Our Awesome Mentor 🙌)")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 