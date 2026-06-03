import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def compute_metrics(df):
    if df.empty or "Date" not in df.columns or "Registrations" not in df.columns:
        return {"QoQ Change": "N/A"}

    df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
    df = df.dropna(subset=["Date", "Registrations"])
    df = df.sort_values("Date")

    if df.empty:
        return {"QoQ Change": "N/A"}

    summary = df.groupby("Date")["Registrations"].sum().pct_change().fillna(0)

    if summary.empty:
        return {"QoQ Change": "N/A"}

    return {"QoQ Change": f"{summary.iloc[-1] * 100:.2f}%"}

def plot_trends(df):
    if df.empty or "Date" not in df.columns or "Registrations" not in df.columns:
        st.warning("No data to plot trends.")
        return

    df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
    df = df.dropna(subset=["Date", "Registrations"])
    df = df.sort_values("Date")

    if df.empty:
        st.warning("No valid data after cleaning.")
        return

    trend = df.groupby("Date")["Registrations"].sum()

    if trend.empty:
        st.warning("No trend data available.")
        return

    st.line_chart(trend)
