import streamlit as st
import pandas as pd

# Initialize a DataFrame to store location data
locations = pd.DataFrame(columns=['Location', 'Count', 'Capacity'])

# Function to calculate crowdedness score
def crowdedness_score(count, capacity):
    score = (count / capacity)*100 if capacity > 0 else 0
    return score

# Streamlit app GUI
st.title("👥Crowd Compass🧭")

#Add location, button, capacity
if "restaurant_num" not in st.session_state:
    st.session_state["restaurant_num"] = 0

if st.button("Add Restaurant"):
    st.session_state["restaurant_num"] += 1

for num in range(1, st.session_state["restaurant_num"] + 1):
    new_location = st.text_input(f"Location #{num} Name")
    new_capacity = st.number_input(f"Capacity of {new_location}", value=0, min_value=0)
    new_count = st.number_input(f"Count of {new_location}", value=0, min_value=0)
    if new_count != 0:
        # color = (1 - crowdedness_score(new_count, new_capacity), crowdedness_score(new_count, new_capacity), 0)  # Green to Red gradient
        st.markdown(
    """
    <style>
        .stProgress > div > div > div > div {
            background-image: linear-gradient(to right, #ff0026, #27ab27);
        }
    </style>""",
    unsafe_allow_html=True,
)
        st.progress(int(crowdedness_score(new_count, new_capacity)))
