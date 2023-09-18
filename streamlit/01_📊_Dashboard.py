import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import folium

from streamlit_folium import st_folium

st.set_page_config(page_title="Morocco Disaster", layout="wide", page_icon="🇲🇦")

col1, col2, col3, col4, col5 = st.columns(5)
with col3:
    st.image("https://i.ibb.co/Df19cyK/khaimaAI.png")

st.markdown('<h4 style="text-align: center;">"Service to others is the rent you pay for your room here on Earth." - Muhammad Ali</h4>', unsafe_allow_html=True)

st.markdown("<p style='text-align: center;'>Crisis Management Made Simple: KhaimaAI is a powerful disaster relief tool designed to assist authorities in efficiently managing temporary camps after natural disasters. It provides real-time data, resource optimization, and vital information, streamlining disaster response efforts and bringing aid where it's needed most.</p>", unsafe_allow_html=True)

st.header("📝 How To Use")

st.markdown("#")

st.markdown("##### Step 1. \n Click on this link and make a copy on your own drive: https://docs.google.com/spreadsheets/d/1uz7ekgRI7AL5ohkiFkGly4RMNri2JPRjIxjEdDRUT1U/  ")
st.markdown("##### Step 2. \n Replace the existing data in the sheet with your own relevant informations.")
st.markdown("##### Step 3. \n When you're done, copy the link of your Google Sheet above in this format (https://docs.google.com/spreadsheets/d/xxxxxxx/edit#gid=0), and paste it below ⤵️")


st.markdown("")
st.info("Here's a Google Sheet for Moulay Ibrahim douar to test with: https://docs.google.com/spreadsheets/d/1uz7ekgRI7AL5ohkiFkGly4RMNri2JPRjIxjEdDRUT1U/edit#gid=0 *(Note: This is a fictif data and not a real one, just for the sake of prototyping)*")

st.markdown("---")

st.markdown("## 📊 Dashboard")

st.markdown("### 🔎 To explore the data for your shelter please import your Google Sheet:")

data = False
sheet = st.text_input("Please Enter the link of your Google Sheet:")

def load_data(sheets_url):
            csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
            return pd.read_csv(csv_url)

if sheet:
    try:
        df = load_data(sheet)
        data = True
    except:
        st.info("Please enter a valid Google Sheet url (https://docs.google.com/spreadsheets/d/xxxxxxx/edit#gid=0)")

if data:
        previous_row = df.iloc[-2]
        
        # Select the last row
        last_row = df.iloc[-1]

        douar_name = last_row.douar_name
        st.markdown(f"## 📍 {douar_name}")

        population = int(last_row.population)
        injuries = int(last_row.injuries)
        deaths = int(last_row.deaths)
        healthcare_personel = int(last_row.healthcare_personel)

        # Calculate the difference in tents from the previous value
        population_difference = population - int(previous_row.population)
        injuries_difference = injuries - int(previous_row.injuries)
        deaths_difference = deaths - int(previous_row.deaths)
        healthcare_difference = healthcare_personel - int(previous_row.healthcare_personel)

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("👨‍👩‍👧‍👧 Population", population, population_difference)
        col2.metric("🤕 Injuries", injuries, injuries_difference)
        col3.metric("💀 Deaths", deaths, deaths_difference)
        col4.metric("👨‍⚕️ Healthcare Personel", healthcare_personel, healthcare_difference)

        tents = int(last_row.tents)
        medecine = int(last_row.medecine_in_percentage)
        food = int(last_row.food_in_percentage)
        water = int(last_row.water)

        # Calculate the difference in tents from the previous value
        tents_difference = tents - int(previous_row.tents)
        medecine_difference = medecine - int(previous_row.medecine_in_percentage)
        food_difference = food - int(previous_row.food_in_percentage)
        water_difference = water - int(previous_row.water)

        st.markdown("#")

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("🏕️ Tents (Unit)", tents, tents_difference)
        col2.metric("⚕️ Medecine (%)", medecine, medecine_difference)
        col3.metric("🍽️ Food (%)", food, food_difference)
        col4.metric("💧 Water (Liter)", water, water_difference)

        douars_data = pd.read_csv("streamlit/data/KhaimaAI - AllDouars.csv") # '../data/KhaimaAI - AllDouars.csv' for local run

        coordinates = last_row.lat_long.strip('()')
        lat_str, lon_str = coordinates.split(', ')
        lat = float(lat_str)
        lon = float(lon_str)
        
        st.markdown("#")

        # Create a Folium map
        m = folium.Map(location=[lat, lon], zoom_start=10)

        # Iterate through each row in the DataFrame
        for index, row in douars_data.iterrows():
            # Get the values for the current row
            douar_name = row['douar_name']
            lat_long = row['lat_long']
            population = row['population']
            injuries = row['injuries']
            deaths = row['deaths']
            healthcare_personel = row['healthcare_personel']
            tents = row['tents']
            medecine = row['medecine_in_percentage']
            food = row['food_in_percentage']
            water = row['water']
                
            # Extract latitude and longitude
            coordinates = lat_long.strip('()')

            lat_str, lon_str = coordinates.split(', ')
            lat = float(lat_str)
            lon = float(lon_str)

            # Determine the marker color and icon based on food and medicine values
            if food > 100 and medecine > 100:
                # Green marker with a "thumbs-up" icon for values over 100%
                icon = folium.Icon(color="green", icon="thumbs-up")
            elif food > 80 and medecine > 80:
                # Blue marker with a "check" icon for values over 80%
                icon = folium.Icon(color="blue", icon="check")
            elif food > 50 and medecine > 50:
                # Yellow marker with an "exclamation" icon for values over 50%
                icon = folium.Icon(color="orange")
            else:
                # Red marker with a "warning" icon for values under 50%
                icon = folium.Icon(color="red", icon="cutlery")

            # Create a tooltip with HTML line breaks
            tooltip_html = f"""<b>📍 Douar name:</b> {douar_name}<br>
                            <b>👨‍👩‍👧‍👧 Population:</b> {population}<br>
                            <b>🤕 Injuries:</b> {injuries}<br>
                            <b>💀 Deaths:</b> {deaths}<br>
                            <b>👨‍⚕️ Healthcare Personel:</b> {healthcare_personel}<br>
                            <b>🏕️ Tents (Unit):</b> {tents}<br>
                            <b>⚕️ Medecine (%):</b> {medecine}<br>
                            <b>🍽️ Food (%):</b> {food}<br>
                            <b>💧 Water (Liter):</b> {water}<br>
                            <b>🗺️ Coordinates:</b> {coordinates}"""
                
            # Create a marker and add it to the map
            folium.Marker(
                [lat, lon], 
                popup=douar_name, 
                tooltip=tooltip_html,
                icon=icon
            ).add_to(m)
                
        # Display the map in Streamlit
        st_folium(m, width=1500)   


        #### Visualizations ####
        data = df

        # Convert the 'date' column to datetime
        data['date'] = pd.to_datetime(data['date'], format='%d/%m/%Y')

        col1, col2 = st.columns(2)

        #Multi-line chart
        st.area_chart(
                data,
                x='date',
                y=['population', 'injuries', 'deaths']
        )

        st.bar_chart(
                data,
                x='date',
                y='tents'
        )

        with col1:
            # Line Chart for Population Over Time
            st.subheader("Population In The Camp")
            st.line_chart(data.set_index('date')['population'], height=200)

            st.markdown("#")

            # Line Chart for Food and Medicine Percentage Over Time
            st.subheader("Food and Medicine Percentage Over Time")
            st.line_chart(data.set_index('date')[['food_in_percentage', 'medecine_in_percentage']])

        with col2:
            # Bar Chart for Tents Over Time
            st.subheader("Tents In The Camp")
            st.line_chart(data.set_index('date')['tents'], height=200, color="#d6281c")

            st.markdown("#")

            # Bar Chart for Water Availability Over Time
            st.subheader("Water Availability Over Time")
            st.bar_chart(data.set_index('date')['water'])

else:
        pass
    