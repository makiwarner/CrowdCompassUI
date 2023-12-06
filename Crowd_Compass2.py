import streamlit as st
import pandas as pd
import json

def read_data():
    try:
        with open("crowd_compass_data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"restaurant_num": 0, "locations": {}}
    return data

def write_data(data):
    with open("crowd_compass_data.json", "w") as file:
        json.dump(data, file)
        
def login_page():
    st.title("Welcome to 👥Crowd Compass🧭")

    # Button to choose role
    role = st.radio("Choose your role:", ("User", "Admin"))

    if role == "Admin":
        password = st.text_input("Enter password:", type="password")
        return role, password

    elif role == "User":
        st.button("Log In")
        return role, None


def admin():
    data = read_data()  # Read existing data

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
                        
        # Save data to be used by the user view
        data["locations"][num] = {
            "name": new_location,
            "capacity": new_capacity,
            "count": new_count,
            "crowdedness": crowdedness_score(new_count, new_capacity)
        }

    # Save the updated data
    write_data(data)

def user():
    data = read_data()  # Read existing data

    # Display information without edit functionality
    if "locations" in data:
        for num, location_data in data["locations"].items():
            t.subheader(f"Location #{num}")
            st.write(f"Capacity of {new_location}: {location_data['capacity']}")
            st.write(f"Count of {new_location}: {location_data['count']}")
            st.progress(int(location_data['crowdedness']))
            st.markdown(
                """
                <style>
                    .stProgress > div > div > div > div {
                        background-image: linear-gradient(to right, #ff0026, #27ab27);
                    }
                </style>""",
                unsafe_allow_html=True,
            )


def app():
    role, password = login_page()

    if role == "Admin":
        if password == "CROWD":
            admin()
        elif password is not None:
            st.warning("Incorrect password. Please try again.")

    elif role == "User":
        user()

# Run the app if the script is executed
if __name__ == "__main__":
    app()
