import streamlit as st
from utils.data_loader import load_data
from utils.analytics import compute_metrics, plot_trends

st.title("Vehicle Registration Dashboard")

# Load data
df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
category = st.sidebar.selectbox("Select Vehicle Type", ["All", "2W", "3W", "4W"])
manufacturer = st.sidebar.selectbox("Select Manufacturer", ["All"] + sorted(df["Manufacturer"].unique()))

# Filter the DataFrame
filtered_df = df.copy()
if category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == category]
if manufacturer != "All":
    filtered_df = filtered_df[filtered_df["Manufacturer"] == manufacturer]

# Check if there's data to show
if filtered_df.empty:
    st.warning("No data available for the selected filters.")
    st.stop()

# Show metrics and plots
st.subheader("YoY and QoQ Growth")
metrics = compute_metrics(filtered_df)
st.write(metrics)

st.subheader("Trends")
plot_trends(filtered_df)
