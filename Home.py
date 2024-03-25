import streamlit as st
import pandas as pd
import altair as alt

# Show Data Index Price
st.header("Show Data Index Price")
df = pd.read_csv("./data/shopping_trends.csv")
st.write(df.columns)

# Show Chart
st.header("Show Chart")

# Age Distribution by Gender (Grouped Bar Chart)
age_range = st.slider("Select Age range", min_value=df["Age"].min(), max_value=df["Age"].max(), value=(df["Age"].min(), df["Age"].max()))
filtered_df = df[(df["Age"] >= age_range[0]) & (df["Age"] <= age_range[1])]
chart = alt.Chart(filtered_df).mark_bar().encode(
    x=alt.X('Age:Q', title='Age'),
    y=alt.Y('count()', title='Count'),
    color='Gender:N',
    tooltip=['Gender', 'Age']
).properties(
    width=600,
    height=400,
    title='Age Distribution by Gender'
)
st.altair_chart(chart, use_container_width=True)

# Purchase Amount Distribution (Grouped Bar Chart)
purchase_range = st.slider("Select Purchase amount range", min_value=df["Purchase Amount (USD)"].min(), max_value=df["Purchase Amount (USD)"].max(), value=(df["Purchase Amount (USD)"].min(), df["Purchase Amount (USD)"].max()))
filtered_df = df[(df["Purchase Amount (USD)"] >= purchase_range[0]) & (df["Purchase Amount (USD)"] <= purchase_range[1])]
chart = alt.Chart(filtered_df).mark_bar().encode(
    x=alt.X('Purchase Amount (USD):Q', title='Purchase Amount (USD)'),
    y=alt.Y('count()', title='Count'),
    color='Gender:N',
    tooltip=['Gender', 'Purchase Amount (USD)']
).properties(
    width=600,
    height=400,
    title='Purchase Amount Distribution by Gender'
)
st.altair_chart(chart, use_container_width=True)

# Max Purchase Amount by Platform (Grouped Bar Chart)
max_purchase_by_platform = df.groupby('Preferred Payment Method')['Purchase Amount (USD)'].max().reset_index()
bar_chart = alt.Chart(max_purchase_by_platform).mark_bar().encode(
    x=alt.X('Preferred Payment Method:N', title='Preferred Payment Method'),
    y=alt.Y('Purchase Amount (USD):Q', title='Max Purchase Amount (USD)'),
    color=alt.Color('Preferred Payment Method:N', legend=None),
    tooltip=['Preferred Payment Method', 'Purchase Amount (USD)']
).properties(
    width=600,
    height=400,
    title='Max Purchase Amount by Preferred Payment Method'
)
st.altair_chart(bar_chart, use_container_width=True)


# Gender Distribution by Preferred Payment Method (Grouped Bar Chart)
gender_payment_counts = df.groupby(['Gender', 'Preferred Payment Method']).size().reset_index(name='count')
gender_payment_chart = alt.Chart(gender_payment_counts).mark_bar().encode(
    x=alt.X('Preferred Payment Method:N', title='Preferred Payment Method'),
    y=alt.Y('count:Q', title='Count'),
    color='Gender:N',
    tooltip=['Gender', 'Preferred Payment Method', 'count']
).properties(
    width=600,
    height=400,
    title='Gender Distribution by Preferred Payment Method'
)
st.altair_chart(gender_payment_chart, use_container_width=True)

# Preferred Payment Method Distribution (Grouped Bar Chart)
payment_counts = df['Preferred Payment Method'].value_counts()
payment_chart = alt.Chart(payment_counts.reset_index()).mark_bar().encode(
    x=alt.X('index:N', title='Preferred Payment Method'),
    y=alt.Y('Preferred Payment Method:Q', title='Count'),
    tooltip=['index:N', 'Preferred Payment Method:Q']
).properties(
    width=600,
    height=400,
    title='Preferred Payment Method Distribution'
)
st.altair_chart(payment_chart, use_container_width=True)

