import streamlit as st

# Page config
st.set_page_config(
    page_title="Telco Customer Churn Predictor",
    page_icon="📱",
    layout="centered"
)

# Title
st.title("📱 Telco Customer Churn Predictor")

st.write("Predict whether a telecom customer may churn.")

st.markdown("---")

# Inputs
col1, col2 = st.columns(2)

with col1:
    tenure = st.slider("Tenure (Months)", 0, 72, 24)

    monthly = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        max_value=200.0,
        value=70.0
    )

    total = st.number_input(
        "Total Charges",
        min_value=0.0,
        max_value=10000.0,
        value=1500.0
    )

    contract = st.selectbox(
        "Contract Type",
        ["Month-to-month", "One year", "Two year"]
    )

with col2:
    internet = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    tech = st.selectbox(
        "Tech Support",
        ["Yes", "No"]
    )

    senior = st.selectbox(
        "Senior Citizen",
        ["Yes", "No"]
    )

# Prediction
if st.button("🔮 Predict Churn"):

    risk = 0

    if tenure < 12:
        risk += 35
    elif tenure < 24:
        risk += 20

    if monthly > 90:
        risk += 25
    elif monthly > 70:
        risk += 15

    if contract == "Month-to-month":
        risk += 30

    if internet == "Fiber optic":
        risk += 10

    if tech == "No":
        risk += 10

    if senior == "Yes":
        risk += 10

    if risk > 100:
        risk = 100

    st.markdown("---")

    if risk >= 60:
        st.error(f"⚠️ High Churn Risk ({risk}%)")

        st.write("### Suggested Actions")
        st.write("- Offer loyalty discounts")
        st.write("- Improve customer support")
        st.write("- Promote annual plans")

    else:
        st.success(f"✅ Low Churn Risk ({risk}%)")

        st.write("### Customer Status")
        st.write("- Customer appears stable")
        st.write("- Lower probability of churn")

st.markdown("---")
st.caption("Built using Python & Streamlit")