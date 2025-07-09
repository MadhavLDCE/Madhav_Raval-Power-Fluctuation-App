
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# --- Page Config ---
st.set_page_config(page_title="Power Fluctuation Predictor", layout="wide")

# --- Custom Style ---
st.markdown("""
    <style>
    body {
        background-color: #1f1f1f;
        color: white;
    }
    .big-font {
        font-size:35px !important;
        font-weight: bold;
        color: #00e6f6;
    }
    .sub-font {
        font-size:18px !important;
        color: #aaaaaa;
    }
    .stAlert {
        background-color: #262626 !important;
        border-left: 5px solid #00e6f6 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title and Tagline ---
st.markdown('<div class="big-font">🔌 Power Supply Fluctuation Prediction in Rural Industry Clusters</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-font">AI-Powered Alert System for Industrial Machine Safety in Rural Areas</div>', unsafe_allow_html=True)
st.write("---")

# --- Upload Section ---
st.sidebar.header("📁 Upload Your Data")
uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])

@st.cache_data
def load_sample_data():
    time = pd.date_range(start='2025-01-01', periods=100, freq='H')
    voltage = np.random.normal(loc=410, scale=5, size=100)
    voltage[30:35] -= 50  # simulate a dip
    current = np.random.normal(loc=15, scale=2, size=100)
    frequency = np.random.normal(loc=50, scale=0.3, size=100)
    return pd.DataFrame({'Timestamp': time, 'Voltage': voltage, 'Current': current, 'Frequency': frequency})

if uploaded_file:
    data = pd.read_csv(uploaded_file, parse_dates=["Timestamp"])
    st.success("✅ File uploaded successfully!")
else:
    st.info("🔍 No file uploaded. Showing sample data...")
    data = load_sample_data()
st.markdown("""
**Developed by:** Madhav Raval  <br>
**Program:** Intel® AI Digital Readiness  <br>
**Department:** Electrical Engineering, L.D. College of Engineering
""", unsafe_allow_html=True)

# --- Show Dataset ---
st.subheader("📊 Data Preview")
st.dataframe(data.head(10), height=200)

# --- Line Charts ---
st.subheader("📈 Power Supply Trends")

fig, ax = plt.subplots(3, 1, figsize=(12, 8), sharex=True)
sns.lineplot(data=data, x='Timestamp', y='Voltage', ax=ax[0], color='#00FF7F')
ax[0].set_title("Voltage Over Time", color='white')
ax[0].tick_params(colors='white')

sns.lineplot(data=data, x='Timestamp', y='Current', ax=ax[1], color='#FFA07A')
ax[1].set_title("Current Over Time", color='white')
ax[1].tick_params(colors='white')

sns.lineplot(data=data, x='Timestamp', y='Frequency', ax=ax[2], color='#87CEFA')
ax[2].set_title("Frequency Over Time", color='white')
ax[2].tick_params(colors='white')

fig.patch.set_facecolor('#1f1f1f')
for axis in ax:
    axis.set_facecolor('#1f1f1f')
    for spine in axis.spines.values():
        spine.set_edgecolor('#444444')
st.pyplot(fig)

# --- Alert Section ---
st.subheader("⚠️ AI-Based Power Fluctuation Alert")

# Simple logic for fluctuation detection
unstable = data[(data['Voltage'] < 360) | (data['Voltage'] > 440)]

if not unstable.empty:
    st.error("🔴 Fluctuation Detected: Abnormal voltage readings. Please delay critical machine operations.")
    st.write("**Times of concern:**")
    st.dataframe(unstable[['Timestamp', 'Voltage']])
else:
    st.success("🟢 Power supply is stable. Machines can operate safely.")

# --- Footer (Optional) ---
st.markdown("---")
st.markdown("<div style='text-align:center; font-size:13px; color:gray;'>© 2025 | Built by Madhav Raval using Python, Streamlit | Intel AI Digital Readiness Project</div>", unsafe_allow_html=True)
