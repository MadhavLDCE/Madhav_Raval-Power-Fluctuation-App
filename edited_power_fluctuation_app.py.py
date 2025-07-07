
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Power Supply Fluctuation Prediction", layout="centered")

# Title and Author Info
st.title("Power Supply Fluctuation Prediction in Rural Industry Clusters")

st.markdown(
    """
    **Developed by:** Madhav Raval  
    **Program:** Intel® AI Digital Readiness  
    **Department:** Electrical Engineering, L.D. College of Engineering  
    """
)

# About the Project (collapsible)
with st.expander("📘 About the Project"):
    st.markdown(
        """
        In rural industrial clusters, inconsistent power supply can lead to unexpected machinery breakdowns,  
        production losses, and safety hazards. This AI-powered tool predicts power supply fluctuations  
        using voltage trend analysis. It helps users make informed decisions—like delaying operations  
        or shutting down machines—before damage occurs.  
        The project combines predictive modeling, data visualization, and real-time smart advisory  
        to support industries in low-resource environments.
        """
    )

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# Mini Instructions & Checklist
st.markdown("""
### 📂 Instructions:
Please upload a `.csv` file containing power supply data.

**Required Columns:**
- `Timestamp` – Date and time of recording
- `Voltage` – Voltage reading (in Volts)

**Example:**
| Timestamp           | Voltage |
|---------------------|---------|
| 2025-06-01 12:00:00 | 229     |
| 2025-06-01 12:01:00 | 231     |
""")

st.markdown("""
### ✅ Data Checklist:
- [x] File must be in `.csv` format  
- [x] Should contain `Timestamp` and `Voltage` columns  
- [x] No missing or non-numeric values
""")

# Once the user uploads a file, process it
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Preview of Uploaded Data")
    st.write(df.head())

    # Fluctuation Alert
    st.markdown("""
    ### 🔔 Fluctuation Alert Notification
    This section provides a quick analysis of whether your data shows any critical voltage fluctuations.
    """)

    avg_voltage = df['Voltage'].mean()
    if avg_voltage < 215 or avg_voltage > 245:
        st.error("⚠️ Warning: Significant voltage fluctuation detected! Please take precautions.")
    else:
        st.success("✅ Voltage levels are within a stable range.")

    # Smart Shutdown Advisory System
    st.subheader("Smart Shutdown Advisory System")

    fluctuation = abs(230 - avg_voltage)
    percent_drop = (fluctuation / 230) * 100

    if percent_drop < 5:
        severity = "Low"
        recommendation = "No immediate action required."
        color = "#d4edda"
        progress = 0.2
    elif 5 <= percent_drop <= 15:
        severity = "Moderate"
        recommendation = "Delay machine operations. Monitor closely."
        color = "#fff3cd"
        progress = 0.5
    else:
        severity = "High"
        recommendation = "⚠️ Shutdown advised to prevent machine damage."
        color = "#f8d7da"
        progress = 0.85

    st.markdown(
        f"""
        <div style='background-color:{color};padding:12px;border-radius:5px;'>
            <b>Fluctuation Severity:</b> {severity} ({percent_drop:.2f}% deviation from nominal voltage)<br>
            <b>Action:</b> {recommendation}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(progress)

    # Power Supply Trend Graph
    st.subheader("Power Supply Trend")
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    plt.figure(figsize=(10,4))
    plt.plot(df['Timestamp'], df['Voltage'], color='green' if percent_drop < 5 else 'red')
    plt.xlabel("Timestamp")
    plt.ylabel("Voltage (V)")
    plt.title("Voltage Trend Over Time")
    plt.xticks(rotation=45)
    st.pyplot(plt)

    # Optional: Add Confusion Matrix Section (if ML model is integrated)
    st.markdown("""
    ### 📊 Model Evaluation (Simulated)
    Confusion matrix helps visualize the accuracy of prediction models. It shows how many times the model correctly predicted 'stable' vs. 'unstable' power.
    """)
