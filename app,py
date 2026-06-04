import streamlit as st
import pandas as pd
import plotly.express as px

from analytics import generate_insights

st.set_page_config(
    page_title="Investment Analytics Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Investment Analytics Dashboard")

uploaded_file = st.file_uploader(
    "Upload Investment Dataset",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.success("Dataset Loaded Successfully")

    # -----------------
    # KPIs
    # -----------------

    col1,col2,col3,col4 = st.columns(4)

    col1.metric(
        "Total Investors",
        len(df)
    )

    col2.metric(
        "Average Age",
        round(df["age"].mean(),1)
    )

    col3.metric(
        "Male",
        len(df[df["gender"]=="Male"])
    )

    col4.metric(
        "Female",
        len(df[df["gender"]=="Female"])
    )

    st.divider()

    # -----------------
    # DATA PREVIEW
    # -----------------

    with st.expander("View Dataset"):
        st.dataframe(df)

    # -----------------
    # GENDER ANALYSIS
    # -----------------

    st.subheader("Gender Distribution")

    fig = px.pie(
        df,
        names="gender",
        title="Investor Gender Split"
    )

    st.plotly_chart(fig, use_container_width=True)

    # -----------------
    # AGE ANALYSIS
    # -----------------

    st.subheader("Age Distribution")

    fig = px.histogram(
        df,
        x="age",
        nbins=10,
        title="Age Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

    # -----------------
    # INVESTMENT PREFERENCE
    # -----------------

    st.subheader("Investment Preference Ranking")

    investment_cols = [
        "Mutual_Funds",
        "Equity_Market",
        "Debentures",
        "Government_Bonds",
        "Fixed_Deposits",
        "PPF",
        "Gold"
    ]

    ranking = df[investment_cols].mean().sort_values()

    fig = px.bar(
        x=ranking.index,
        y=ranking.values,
        title="Average Preference Ranking"
    )

    st.plotly_chart(fig, use_container_width=True)

    # -----------------
    # OBJECTIVE ANALYSIS
    # -----------------

    st.subheader("Investment Objectives")

    objective_counts = (
        df["Objective"]
        .value_counts()
        .reset_index()
    )

    objective_counts.columns = [
        "Objective",
        "Count"
    ]

    fig = px.bar(
        objective_counts,
        x="Objective",
        y="Count"
    )

    st.plotly_chart(fig, use_container_width=True)

    # -----------------
    # RETURN EXPECTATION
    # -----------------

    st.subheader("Expected Returns")

    fig = px.pie(
        df,
        names="Expect"
    )

    st.plotly_chart(fig, use_container_width=True)

    # -----------------
    # SOURCE ANALYSIS
    # -----------------

    st.subheader("Source of Financial Knowledge")

    source = (
        df["Source"]
        .value_counts()
        .reset_index()
    )

    source.columns = [
        "Source",
        "Count"
    ]

    fig = px.bar(
        source,
        x="Source",
        y="Count"
    )

    st.plotly_chart(fig, use_container_width=True)

    # -----------------
    # AUTO INSIGHTS
    # -----------------

    st.subheader("AI Generated Insights")

    insights = generate_insights(df)

    for item in insights:
        st.info(item)
