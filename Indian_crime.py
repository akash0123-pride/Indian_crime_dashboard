#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import streamlit as st
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load Data
url = "https://raw.githubusercontent.com/akash0123-pride/Indian_crime_dashboard/main/10_Property_stolen_and_recovered.csv"
df = pd.read_csv(url)


df.columns = [
    "State_UT", "Year", "Crime_Category", "Sub_Category", 
    "Recovered_Cases", "Stolen_Cases", "Recovered_Value", "Stolen_Value"
]

# Cleaning Data
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df["Recovered_Cases"] = df[["Recovered_Cases", "Stolen_Cases"]].min(axis=1)
df["Recovered_Value"] = df[["Recovered_Value", "Stolen_Value"]].min(axis=1)

# Machine Learning: Predict Recovery Success
df["Recovery_Rate"] = df["Recovered_Cases"] / df["Stolen_Cases"]
df["Recovery_Label"] = (df["Recovery_Rate"] > 0.5).astype(int)
X = df[["Stolen_Cases", "Stolen_Value"]]
y = df["Recovery_Label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Streamlit App
st.set_page_config(page_title="Indian Crime Data Dashboard", layout="wide", initial_sidebar_state="expanded")
st.markdown("""
    <style>
    body {
        background-color: #1e1e1e;
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: #333333;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Indian Crime Data Dashboard")
st.sidebar.header("Filters")

# Filters
year = st.sidebar.selectbox("Select Year", sorted(df["Year"].unique()), index=0)
state = st.sidebar.selectbox("Select State/UT", sorted(df["State_UT"].unique()))
category = st.sidebar.selectbox("Select Crime Category", sorted(df["Crime_Category"].unique()))

# Filtered Data
df_filtered = df[(df["Year"] == year) & (df["State_UT"] == state) & (df["Crime_Category"] == category)]

# Line Chart: Crime Trends
df_trend = df[df["Crime_Category"] == category].groupby("Year").sum().reset_index()
fig_trend = px.line(df_trend, x="Year", y=["Stolen_Cases", "Recovered_Cases"],
                     title="Crime Trends Over the Years", template="plotly_dark")
st.plotly_chart(fig_trend)

# Bar Chart: Stolen vs Recovered Cases
fig_bar = px.bar(df_filtered, x="Sub_Category", y=["Stolen_Cases", "Recovered_Cases"],
                 barmode='group', title=f"Stolen vs Recovered Cases in {state} ({year})", template="plotly_dark")
st.plotly_chart(fig_bar)

# Pie Chart: Recovery Success Rate
recovery_rate = df_filtered[["Recovered_Cases", "Stolen_Cases"]].sum()
fig_pie = px.pie(values=recovery_rate, names=["Recovered", "Not Recovered"],
                 title="Recovery Success Rate", template="plotly_dark")
st.plotly_chart(fig_pie)

#  State-Wise Crime Distribution
st.subheader("State-Wise Crime Distribution")
df_state = df.groupby("State_UT", as_index=False)[["Stolen_Cases"]].sum()
fig_state = px.bar(df_state.sort_values("Stolen_Cases", ascending=False)[:10], x="Stolen_Cases", y="State_UT", 
                    title="Top 10 States with Highest Crime Rates", template="plotly_dark")
st.plotly_chart(fig_state)

#  Recovery Success Rate
st.subheader("Recovery Success Rate")
df_recovery = df.groupby("State_UT")[["Recovered_Cases", "Stolen_Cases"]].sum().reset_index()
df_recovery["Recovery_Rate"] = df_recovery["Recovered_Cases"] / df_recovery["Stolen_Cases"] * 100
fig_recovery = px.bar(df_recovery.sort_values("Recovery_Rate", ascending=False)[:10], x="Recovery_Rate", y="State_UT", 
                        title="Top 10 States with Highest Recovery Rates", template="plotly_dark")
st.plotly_chart(fig_recovery)

# Heatmap for Crime Rates by State
st.subheader("Heatmap of Crime Rates by State and Year")
df_pivot = df.pivot_table(values="Stolen_Cases", index="State_UT", columns="Year", aggfunc="sum", fill_value=0)
fig_heatmap = px.imshow(df_pivot, labels=dict(x="Year", y="State_UT", color="Stolen Cases"), 
                         title="Heatmap of Stolen Cases by State and Year", template="plotly_dark")
st.plotly_chart(fig_heatmap)

#  Scatter Plot: Stolen vs Recovered Cases
st.subheader("Scatter Plot: Stolen vs Recovered Cases")
fig_scatter = px.scatter(df, x="Stolen_Cases", y="Recovered_Cases", color="Crime_Category", 
                         title="Stolen vs Recovered Cases by Crime Category", template="plotly_dark")
st.plotly_chart(fig_scatter)

#  Boxplot: Stolen Value Distribution by Crime Type
st.subheader("Boxplot: Stolen Value Distribution by Crime Type")
fig_boxplot = px.box(df, x="Crime_Category", y="Stolen_Value", color="Crime_Category", 
                      title="Distribution of Stolen Value by Crime Type", template="plotly_dark")
st.plotly_chart(fig_boxplot)


st.write("### Data Table")
st.dataframe(df_filtered)

# Display Machine Learning Model Accuracy
st.write(f"### Machine Learning Model Accuracy: {accuracy:.2%}")


# In[ ]:




