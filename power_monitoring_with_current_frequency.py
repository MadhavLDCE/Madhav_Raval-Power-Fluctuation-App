import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Power Supply Monitoring", layout="wide")

st.markdown(
    """
    <div style='text-align: center; padding-top: 20px;'>
        <h1 style='color: #00DFFC; font-size: 42px; font-weight: bold;'>Power Supply Fluctuation Prediction in Rural Industry Clusters</h1>
        <p style='font-size: 20px; color: #cccccc;'>AI-Powered Alert System with Voltage, Current, and Frequency Analysis</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.title("📁 Upload Your CSV")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])
st.sidebar.markdown("**Columns Required:**")
st.sidebar.markdown("""
- Timestamp  
- Voltage  
- Current  
- Frequency
""")


# About section
st.markdown("---")
st.markdown("**Developed by:** Madhav Raval  <br>"
            "**Program:** Intel® AI Digital Readiness  <br>"
            "**Department:** Electrical Engineering, L.D. College of Engineering",
            unsafe_allow_html=True)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    try:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])

        # ⚠️ Voltage Fluctuation Alert FIRST
        st.subheader("⚠️ Voltage Fluctuation Alert")
        critical_rows = df[(df['Voltage'] < 215) | (df['Voltage'] > 245)]

        if not critical_rows.empty:
            st.error(f"⚠️ Voltage fluctuation detected! {len(critical_rows)} unstable readings found.")
            st.markdown("**Unstable Timestamps:**")
            st.dataframe(critical_rows[['Timestamp', 'Voltage']])
        else:
            st.success("✅ All voltage values are within the stable range (215V–245V).")

        # 📈 Graphs Section
        st.subheader("📈 Power Metrics Over Time")

        # Voltage
        fig1, ax1 = plt.subplots(figsize=(10, 3))
        ax1.plot(df['Timestamp'], df['Voltage'], color='#00FF6A')  # neon green
        fig1.patch.set_facecolor('#0e1117')
        ax1.set_facecolor('#0e1117')
        ax1.tick_params(colors='white')
        ax1.xaxis.label.set_color('white')
        ax1.yaxis.label.set_color('white')
        ax1.title.set_color('white')
        ax1.set_title("Voltage Over Time")
        ax1.set_xlabel("Timestamp")
        ax1.set_ylabel("Voltage (V)")
        plt.xticks(rotation=45)
        st.pyplot(fig1)

        # Current
        fig2, ax2 = plt.subplots(figsize=(10, 3))
        ax2.plot(df['Timestamp'], df['Current'], color='#1E90FF')  # vivid blue
        fig2.patch.set_facecolor('#0e1117')
        ax2.set_facecolor('#0e1117')
        ax2.tick_params(colors='white')
        ax2.xaxis.label.set_color('white')
        ax2.yaxis.label.set_color('white')
        ax2.title.set_color('white')
        ax2.set_title("Current Over Time")
        ax2.set_xlabel("Timestamp")
        ax2.set_ylabel("Current (A)")
        plt.xticks(rotation=45)
        st.pyplot(fig2)

        # Frequency
        fig3, ax3 = plt.subplots(figsize=(10, 3))
        ax3.plot(df['Timestamp'], df['Frequency'], color='#BB00FF')  # electric purple
        fig3.patch.set_facecolor('#0e1117')
        ax3.set_facecolor('#0e1117')
        ax3.tick_params(colors='white')
        ax3.xaxis.label.set_color('white')
        ax3.yaxis.label.set_color('white')
        ax3.title.set_color('white')
        ax3.set_title("Frequency Over Time")
        ax3.set_xlabel("Timestamp")
        ax3.set_ylabel("Frequency (Hz)")
        plt.xticks(rotation=45)
        st.pyplot(fig3)

    except Exception as e:
        st.error(f"Error reading file: {e}")
else:
    st.info("Please upload a CSV file to visualize power metrics.")
