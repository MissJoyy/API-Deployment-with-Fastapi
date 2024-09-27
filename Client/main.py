import streamlit as st
import requests

st.set_page_config(
    page_title="Sepsis Prediction Page",
    page_icon="🤖",
    layout="wide"
)

# set title of the application
st.title("Sepssis Classifier Application 🤖")

# # load the api endpoints from FastAPI
# gradient_boost_endpoint = "http://127.0.0.1:8000/forest_prediction"
# xgb_classifier_endpoint = "http://127.0.0.1:8000/knc_prediction"

# endpoints from Docker
random_forest_endpoint = "http://api:8000/forest_prediction"
knc_classifier_endpoint = "http://api:8000/knc_prediction"


# select between the two endpoints of the ml_model
col1,col2 = st.columns(2)
with col2:
    st.selectbox("Model Selection",options=["Knc Classifier","Forest Classifier"],key="model_select")

# initializa select model session state
if "model_select" not in st.session_state:
    st.session_state["model_select"] = "knc Classifier"

# Initialize session state for input features
input_keys = ["Plasma_Glucose", "Blood_Work_Result_1", "Blood_Pressure", "Blood_Work_Result_2",
              "Blood_Work_Result_3", "Body_Mass_Index", "Blood_Work_Result_4", "Age", "Insurance"]


for key in input_keys:
    if key not in st.session_state:
        st.session_state[key] = 0

# define function to accept inputs and display forms
def display_forms():
    with st.form("input-features"):
        col1,col2 = st.columns(2)
        with col1:
            st.number_input("Plasma Glucose",min_value=0,step=1,key = "Plasma_Glucose")
            st.number_input("Blood Work Result 1",min_value=0,step=1,key = "Blood_Work_Result_1")
            st.number_input("Blood Pressure",min_value=0,step=1,key = "Blood_Pressure")
            st.number_input("Blood Work Result 2",min_value=0,step=1,key = "Blood_Work_Result_2")
           
        with col2:
            st.number_input("Blood Work Result 3",min_value=0,step=1,key = "Blood_Work_Result_3")
            st.number_input("Body Mass Index",min_value=0.0,step=0.1,key = "Body_Mass_Index")
            st.number_input("Blood Work Result 4",min_value=0.0,step=0.1,key = "Blood_Work_Result_4")
            st.number_input("Age", min_value=0, step=1, key = "Age")
            st.number_input("Insurance",min_value=0, max_value =1,step=1,key = "Insurance")
        submit_button = st.form_submit_button("Predict")
    return submit_button


# define function to make predictions
def make_prediction():
    input_features = {key: st.session_state[key] for key in input_keys}
    if st.session_state["model_select"] == "knc Classifier":
        # send api resopnse to the gradient boost api
        knc_classifier_response =requests.post(knc_classifier_endpoint,json=input_features)
        if knc_classifier_response.status_code == 200:
            print(knc_classifier_response.status_code)
            prediction =knc_classifier_response.json()["prediction"]
            probability = knc_classifier_response.json()["prediction_probability"]
            st.divider()
            st.success(f"The Sepssis prediction is: {prediction}, with the following prediction probabilities {probability}")
        else:
            st.error(f"Error: {knc_classifier_response.json()}")
    else:
        random_forest_response =requests.post(random_forest_endpoint,json=input_features)
        print(random_forest_response.status_code)
        if random_forest_response.status_code == 200:
            print(random_forest_response.status_code)
            prediction = random_forest_response.json()["prediction"]
            probability = random_forest_response.json()["prediction_probability"]
            st.divider()
            st.success(f"The Sepssis prediction is: {prediction}, with the following prediction probabilities {probability}")
        else:
            st.error(f"Error: {random_forest_response.json()}")




if __name__ == "__main__":
    submit_button = display_forms()
    if submit_button:
        make_prediction()
