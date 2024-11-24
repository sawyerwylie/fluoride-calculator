import streamlit as st

# Constants for calculations
CONSTANTS = {
    "Sodium Fluoride (NaF)": 128,
    "Sodium Monofluorophosphate (NaMFP)": 37,
    "Stannous Fluoride (SnF2)": 69,
    "Fluoride Ion": 218,
}

# Conversion factor
OUNCE_TO_GRAMS = 28.35
SPECIFIC_GRAVITY_TO_WEIGHT = 1.3

# Helper function to convert pounds to kilograms
def pounds_to_kg(pounds):
    return pounds / 2.20462

# Title
st.title("Fluoride Ingestion Calculator")

# User inputs
formulation = st.selectbox(
    "Formulation",
    ["Sodium Fluoride (NaF)", "Sodium Monofluorophosphate (NaMFP)", "Stannous Fluoride (SnF2)", "Fluoride Ion"],
)
concentration = st.number_input("Concentration in %", min_value=0.000, step=0.001, format="%.1f")
amount_ingested = st.number_input(
    "Amount Ingested of Product in Ounces", min_value=0.0, step=0.1, format="%.1f"
)
weight_input_type = st.selectbox("Patient Weight Input Type", ["Kilograms", "Pounds"])
weight = st.number_input(
    f"Patient Weight in {weight_input_type}",
    min_value=0.0,
    step=0.1,
    format="%.1f",
)

# Convert weight to kilograms if necessary
if weight_input_type == "Pounds":
    weight = pounds_to_kg(weight)

# Calculation
if st.button("Calculate"):
    if weight == 0 or concentration == 0 or amount_ingested == 0:
        st.error("Please ensure all inputs are greater than 0.")
    else:
        constant = CONSTANTS.get(formulation)
        fluoride_ingested = (concentration * amount_ingested * constant) / weight
        st.success(f"Amount Ingested: {fluoride_ingested:.2f} mg Fluoride/kg")
