import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Power Supply Fluctuation Prediction", layout="wide")

# Custom styled title and subtitle
st.markdown(
    """
    <div style='text-align: center; padding-top: 20px;'>
        <h1 style='color: #00DFFC; font-size: 42px; font-weight: bold;'>Power Supply Fluctuation Prediction in Rural Industry Clusters</h1>
        <p style='font-size: 20px; color: #cccccc;'>AI-Powered Alert System for Industrial Machine Safety in Rural Areas</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar: File upload and instructions
st.sidebar.title("📁 Upload Your Data")
uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])

st.sidebar.markdown("**Instructions:**")
st.sidebar.markdown("""
- Upload a `.csv` file containing power supply data.
- Required columns:
  - `Timestamp` (Date and time)
  - `Voltage` (in Volts)
""")

st.sidebar.markdown("**✅ Format Example:**")
st.sidebar.markdown("""
| Timestamp           | Voltage |

|---------------------|---------|

| 2025-06-01 12:00:00 | 229     |
""")

# Main: Bordered "About the Project" section
st.markdown("""
<div style='border: 1px solid #444; padding: 20px; border-radius: 10px; background-color: #111111;'>
    <h4 style='color: #58a6ff;'>About the Project</h4>
    <p style='color: #dddddd; font-size: 16px;'>
    In rural industrial clusters, inconsistent power supply can lead to unexpected machinery breakdowns,
    production losses, and safety hazards. This AI-powered tool predicts power supply fluctuations
    using voltage trend analysis. It helps users make informed decisions—like delaying operations
    or shutting down machines—before damage occurs.<br><br>
    The project combines predictive modeling, data visualization, and real-time smart advisory
    to support industries in low-resource environments.
    </p>
</div>
""", unsafe_allow_html=True)

# Developer credits
st.markdown("---")
st.markdown("""
**Developed by:** Madhav Raval  <br>
**Program:** Intel® AI Digital Readiness  <br>
**Department:** Electrical Engineering, L.D. College of Engineering
""", unsafe_allow_html=True)


# Process file if uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    st.subheader("📊 Voltage Trend Over Time")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df['Timestamp'], df['Voltage'], color='skyblue')
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("Voltage (V)")
    ax.set_title("Voltage Readings")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    st.subheader("⚠️ AI-Based Power Fluctuation Alert")
    avg_voltage = df['Voltage'].mean()
    critical_rows = df[(df['Voltage'] < 215) | (df['Voltage'] > 245)]

    if not critical_rows.empty:
        st.error("Fluctuation Detected: Abnormal voltage readings. Please delay critical machine operations.")
        st.markdown("**Times of concern:**")
        st.dataframe(critical_rows[['Timestamp', 'Voltage']])
    else:
        st.success("No significant fluctuation detected. Voltage appears stable.")

    # Smart Advisory
    st.subheader("🧠 Smart Shutdown Advisory System")
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
        """, unsafe_allow_html=True
    )
    st.progress(progress)
