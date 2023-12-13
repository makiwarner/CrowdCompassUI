import streamlit as st
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

# Function to calculate crowdedness score
def crowdedness_score(count, capacity):
    score = (count / capacity) * 100 if capacity > 0 else 0
    return score

def admin():
    data = read_data()  # Read existing data

    # Display information that was previously stored
    # only "count" has edit functionality
    if "locations" in data:
        for num, location_data in data["locations"].items():
            st.subheader(f"Location #{num}")
            st.write(f"Capacity of {location_data['name']}: {location_data['capacity']}")

            # Allow editing only for count
            count_key = f"count_{num}"  # Unique key for count input
            new_count = st.number_input(f" Count of {location_data['name']}", value=location_data['count'], min_value=0, key=count_key)

            # Create an empty space for the progress bar
            progress_bar_container = st.empty()

            # Update the progress bar based on the updated count and existing capacity
            progress_bar_container.progress(int(crowdedness_score(new_count, location_data['capacity'])))

            # Save the updated count to be used by the user view
            data["locations"][num]["count"] = new_count
            data["locations"][num]["crowdedness"] = crowdedness_score(new_count, location_data['capacity'])

            st.markdown(
                """
                <style>
                    .stProgress > div > div > div > div {
                        background-image: linear-gradient(to right, #ff0026, #27ab27);
                    }
                </style>""",
                unsafe_allow_html=True,
            )

    # Streamlit app GUI to add location, button, capacity

    if "restaurant_num" not in st.session_state:
        st.session_state["restaurant_num"] = 0

    if st.button("Add Restaurant"):
        st.session_state["restaurant_num"] += 1

    for num in range(1, st.session_state["restaurant_num"] + 1):
        new_location = st.text_input(f"Location #{num} Name")
        new_capacity = st.number_input(f"Capacity of {new_location}", value=0, min_value=0)
        count_key = f"count_new_{num}"  # Unique key for count input
        new_count = st.number_input(f"Count of {new_location}", value=0, min_value=0, key=count_key)
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
            progress_bar_container = st.empty()
            progress_bar_container.progress(int(crowdedness_score(new_count, new_capacity)))

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
            st.subheader(f"Location #{num}")
            st.write(f"Capacity of {location_data['name']}: {location_data['capacity']}")
            st.write(f"Count of {location_data['name']}: {location_data['count']}")
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

