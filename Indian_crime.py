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
# 2. State-Wise Crime Distribution
st.subheader("State-Wise Crime Distribution")
fig, ax = plt.subplots(figsize=(12, 6))
df_state = df.groupby("State_UT").sum().reset_index()
sns.barplot(data=df_state.sort_values("Stolen_Cases", ascending=False)[:10], x="Stolen_Cases", y="State_UT", palette="Reds", ax=ax)
plt.title("Top 10 States with Highest Crime Rates")
st.pyplot(fig)

# 3. Recovery Success Rate
st.subheader("Recovery Success Rate")
df_recovery = df.groupby("State_UT")[["Recovered_Cases", "Stolen_Cases"]].sum().reset_index()
df_recovery["Recovery_Rate"] = df_recovery["Recovered_Cases"] / df_recovery["Stolen_Cases"] * 100
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=df_recovery.sort_values("Recovery_Rate", ascending=False)[:10], x="Recovery_Rate", y="State_UT", palette="Blues", ax=ax)
plt.title("Top 10 States with Highest Recovery Rates")
st.pyplot(fig)

# 4. Heatmap for Crime Rates by State
st.subheader("Heatmap of Crime Rates by State and Year")
fig, ax = plt.subplots(figsize=(12, 8))
df_pivot = df.pivot_table(values="Stolen_Cases", index="State_UT", columns="Year", aggfunc=np.sum)
sns.heatmap(df_pivot, cmap="Reds", annot=True, fmt=".0f", ax=ax)
plt.title("Heatmap of Stolen Cases by State and Year")
st.pyplot(fig)

# 5. Scatter Plot: Stolen vs Recovered Cases
st.subheader("Scatter Plot: Stolen vs Recovered Cases")
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(data=df, x="Stolen_Cases", y="Recovered_Cases", hue="Crime_Category", alpha=0.6, ax=ax)
plt.title("Stolen vs Recovered Cases by Crime Category")
st.pyplot(fig)

# 6. Boxplot: Stolen Value Distribution by Crime Type
st.subheader("Boxplot: Stolen Value Distribution by Crime Type")
fig, ax = plt.subplots(figsize=(12, 6))
sns.boxplot(data=df, x="Crime_Category", y="Stolen_Value", palette="coolwarm", ax=ax)
plt.xticks(rotation=45)
plt.title("Distribution of Stolen Value by Crime Type")
st.pyplot(fig)



st.write("### Data Table")
st.dataframe(df_filtered)

# Display Machine Learning Model Accuracy
st.write(f"### Machine Learning Model Accuracy: {accuracy:.2%}")


# In[ ]:




