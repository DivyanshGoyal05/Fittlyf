import streamlit as st

#title -
st.title("ASSIGNMENT")

#Header
st.header("Section A/B Testing")

#Sub Header

st.subheader("Create a simple Streamlit app (you can follow this tutorial) using the function you created that performs the hypothesis test by taking in the above mentioned inputs from the user. Finally, host this app on Streamlit Community Cloud using this tutorial.")

#To give Information
import streamlit as st
import numpy as np

def ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level):
    # Calculate conversion rates
    control_rate = control_conversions / control_visitors
    treatment_rate = treatment_conversions / treatment_visitors
    
    # Calculate the standard error
    standard_error = np.sqrt(control_rate * (1 - control_rate) / control_visitors + 
                             treatment_rate * (1 - treatment_rate) / treatment_visitors)
    
    # Calculate the Z-score
    z_score = (treatment_rate - control_rate) / standard_error
    
    # Determine the confidence level for the Z-test
    confidence = {90: 1.645, 95: 1.96, 99: 2.576}[confidence_level]
    
    # Compare the Z-score with the critical Z-value
    if np.abs(z_score) > confidence:
        return "Experiment Group is Better" if z_score > 0 else "Control Group is Better"
    else:
        return "Indeterminate"

def main():
    st.title("A/B Test Hypothesis Testing")

    # User inputs
    control_visitors = st.number_input("Enter number of visitors in control group", min_value=1, step=1)
    control_conversions = st.number_input("Enter number of conversions in control group", min_value=0, step=1)
    treatment_visitors = st.number_input("Enter number of visitors in treatment group", min_value=1, step=1)
    treatment_conversions = st.number_input("Enter number of conversions in treatment group", min_value=0, step=1)
    confidence_level = st.slider("Select confidence level", min_value=90, max_value=99, step=5, value=95)

    # Run A/B test when button is clicked
    if st.button("Run A/B Test"):
        result = ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level)
        st.write("Result:", result)

if __name__ == "__main__":
    main()
