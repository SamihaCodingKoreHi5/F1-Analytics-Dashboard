import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(
    page_title="F1 Analytics Dashboard",
    page_icon="🏎️",
    layout="wide"
)

# Title
st.title("🏎️ Formula 1 Analytics Dashboard")

# Load Dataset
df = pd.read_csv("data/f1_drivers.csv")

# Dataset
st.subheader("📋 F1 Drivers Dataset")
st.dataframe(df)

# Driver Selection
selected_driver = st.selectbox(
    "🏁 Select Driver",
    df["Driver"]
)

# Selected Driver Data
driver_data = df[df["Driver"] == selected_driver].iloc[0]

# Driver Statistics
st.subheader("📊 Driver Statistics")

col1, col2 = st.columns(2)

with col1:
    st.metric("🏆 Wins", driver_data["Wins"])
    st.metric("🥇 Podiums", driver_data["Podiums"])

with col2:
    st.metric("⭐ Points", driver_data["Points"])
    st.metric("⚡ Fastest Laps", driver_data["Fastest_Laps"])

# Driver Wins Chart
st.subheader("📈 Driver Wins Comparison")

fig, ax = plt.subplots(figsize=(10, 5))

bars = ax.bar(
    df["Driver"],
    df["Wins"],
    color="red"
)

ax.set_xlabel("Drivers")
ax.set_ylabel("Wins")
ax.set_title("Formula 1 Driver Wins")

plt.xticks(rotation=20)

for bar in bars:
    height = bar.get_height()

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        str(height),
        ha="center",
        va="bottom"
    )

st.pyplot(fig)

# Greatest Driver
best_driver = df.loc[df["Wins"].idxmax()]

st.subheader("🏆 Greatest Driver")

st.success(
    f"{best_driver['Driver']} leads the dataset with {best_driver['Wins']} career wins."
)

# Footer
st.markdown("---")
st.write("Built with Python, Pandas, Matplotlib and Streamlit 🚀")
