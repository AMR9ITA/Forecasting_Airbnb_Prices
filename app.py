import streamlit as st
import pickle

# Load your best trained GradientBoostingRegressor model
model_path = '/content/best_model_GB.pkl'
model_file = "best_model_GB.pkl"
with open(model_path, 'rb') as model_file:
    model = joblib.load(model_file)

# loaded_model = joblib.load(model_filename)

# Streamlit UI
st.title('Price Prediction App')
st.write('Enter the features for prediction:')

# Collect input features from user
neighbourhood_group_options = ['Osdorp', 'Negen Straatjes', 'Zuidas', 'Museum Quarter']
neighbourhood_options = ['Oostelijk Havengebied - Indische Buurt', 'Centrum-Oost', 'Centrum-West', 'De Pijp - Rivierenbuurt', 'Zuid', 'Oud-Oost', 'Westerpark', 'De Baarsjes - Oud-West', 'Slotervaart', 'IJburg - Zeeburgereiland', 'Watergraafsmeer', 'Noord-Oost', 'Bos en Lommer', 'Oud-Noord', 'Buitenveldert - Zuidas', 'Noord-West', 'De Aker - Nieuw Sloten', 'Osdorp', 'Bijlmer-Centrum', 'Geuzenveld - Slotermeer', 'Gaasperdam - Driemond', 'Bijlmer-Oost']
room_type_options = ['Private room', 'Entire home/apt', 'Hotel room', 'Shared room']

neighbourhood_group = st.selectbox('Neighbourhood Group', neighbourhood_group_options)
neighbourhood = st.selectbox('Neighbourhood', neighbourhood_options)
room_type = st.selectbox('Room Type', room_type_options)
minimum_nights = st.number_input('Minimum Nights', value=1)
availability_365 = st.number_input('Availability 365', value=0)

# Create a button to perform prediction
if st.button('Predict'):
    # Prepare input for prediction
    input_data = [[minimum_nights, availability_365]]  # Add more features as needed

    # Perform prediction
    prediction = model.predict(input_data)

    # Display prediction
    st.write(f'Predicted Price: {prediction[0]}')
