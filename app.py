import streamlit as st
import pandas as pd
import pickle

st.title("Customer Satisfication Prediction")

st.write("----")


sidebar_title = st.sidebar.title("Input Features")

Gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female"]
)

Customer_Type = st.sidebar.selectbox(
    "Customer Type",
    ["Loyal Customer", "disloyal Customer"]
)

Age = st.sidebar.number_input("Enter Age", min_value=7, max_value=85)

Type_of_Travel = st.sidebar.selectbox(
    "Type of Travel",
    ["Business travel", "Personal Travel"]
)

Class = st.sidebar.selectbox(
    "Class",
    ["Business", "Eco", "Eco Plus"]
)

Flight_Distance = st.sidebar.number_input("Flight distance", min_value= 31, max_value= 4983)

Inflight_wifi_service = st.sidebar.number_input("Inflight wifi service", min_value=0, max_value=5)

Departure_time_convenient = st.sidebar.number_input("Departure time convenient:", min_value=0, max_value=5)

Ease_of_Online_booking = st.sidebar.number_input("Ease of Online booking", max_value=5)

Gate_location = st.sidebar.number_input("Gate location:", min_value=1, max_value=5)

Food_and_drink = st.sidebar.number_input("Food and drink", max_value=5)

Online_boarding = st.sidebar.number_input("Online boarding", max_value=5)

Seat_comfort = st.sidebar.number_input("Seat comfort", max_value=5)

Inflight_entertainment = st.sidebar.number_input("Inflight entertainment:", max_value=5)

On_board_service = st.sidebar.number_input("On-board service:", max_value=5)

Leg_room_service = st.sidebar.number_input("Leg room service", max_value=5)

Baggage_handling = st.sidebar.number_input("Baggage handling:", min_value=1, max_value=5)

Checkin_service = st.sidebar.number_input("Checkin service", max_value=5)

Inflight_service = st.sidebar.number_input("Inflight service", max_value=5)

Cleanliness = st.sidebar.number_input("Cleanliness", max_value=5)

Departure_Delay_in_Minutes = st.sidebar.number_input("Departure Delay in Minutes", max_value=1592)

Arrival_Delay_in_Minutes = st.sidebar.number_input("Arrival Delay in Minutes", max_value=1584.0)

# Create dataframeW

df = pd.DataFrame({
    "Gender": [Gender],
    "Customer Type": [Customer_Type],
    "Age": [Age],
    "Type of Travel": [Type_of_Travel],
    "Class": [Class],
    "Flight Distance": [Flight_Distance],
    "Inflight wifi service": [Inflight_wifi_service],
    "Departure/Arrival time convenient": [Departure_time_convenient],
    "Ease of Online booking": [Ease_of_Online_booking],
    "Gate location": [Gate_location],
    "Food and drink": [Food_and_drink],
    "Online boarding": [Online_boarding],
    "Seat comfort": [Seat_comfort],
    "Inflight entertainment": [Inflight_entertainment],
    "On-board service": [On_board_service],
    "Leg room service": [Leg_room_service],
    "Baggage handling": [Baggage_handling],
    "Checkin service": [Checkin_service],
    "Inflight service": [Inflight_service],
    "Cleanliness": [Cleanliness],
    "Departure Delay in Minutes": [Departure_Delay_in_Minutes],
    "Arrival Delay in Minutes": [Arrival_Delay_in_Minutes]

})


st.markdown("#### Input Data")
st.write(df.head())

# Encode categorical columns
encode_map = {
    "Gender": {"Male": 1, "Female": 0},
    "Customer Type": {"Loyal Customer":1, "disloyal Customer":0},
    "Type of Travel": {"Business travel":1 , "Personal Travel": 0},
    "Class": {"Business":1, "Eco":2, "Eco Plus":3}

}

for col, mapping in encode_map.items():
    df[col] = df[col].map(mapping)


st.write("_____")
button = st.button("Predict")

# Load model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Prediction
prediction = model.predict(df)


if button:
    if prediction == 1:
        st.markdown("### 😆 Customer is SATISFIED")

    else:
        st.markdown("### 😒 Customer is NEUTRAL OR DISSATISFIED")

st.markdown("### About the Model")

model_info = {
    "Model Name": "Random Forest Classifier",
    "Accuracy": 96,
    "Precision": 95,
    "Recall": 98
}

dat = pd.DataFrame(model_info, index=[1])
st.write(dat.head())


st.info("Build by **Zakir Ali** | Machine Learning Engineer")