import streamlit as st
import pandas as pd
import altair as alt

# Show Data Index Price
st.header("Show Data Index Price")
df = pd.read_csv("./data/shopping_trends.csv")
st.write(df.head(10))

# Show Chart
st.header("Show Chart")

# Age Distribution by Platform (Grouped Bar Chart)
age_range = st.slider("Select Purchase amount range", min_value=df["Purchase amount"].min(), max_value=df["Purchase amount"].max(), value=(df["Purchase amount"].min(), df["Purchase amount"].max()))
filtered_df = df[(df["Purchase amount"] >= age_range[0]) & (df["Purchase amount"] <= age_range[1])]
chart = alt.Chart(filtered_df).mark_bar().encode(
    x=alt.X('age:Q', title='Age'),
    y=alt.Y('count()', title='Count'),
    color='platform:N',
    tooltip=['platform', 'age']
).properties(
    width=600,
    height=400,
    title='Age Distribution by Platform'
)
st.altair_chart(chart, use_container_width=True)

# Time Spent Distribution by Platform (Grouped Bar Chart)
chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('platform:N', title='Platform'),
    y=alt.Y('time_spent:Q', title='Time Spent'),
    color='platform:N',
    tooltip=['platform', 'time_spent']
).properties(
    width=600,
    height=400,
    title='Time Spent Distribution by Platform'
)
st.altair_chart(chart, use_container_width=True)

# Max Age by Platform (Grouped Bar Chart)
max_age_by_platform = df.groupby('platform')['age'].max().reset_index()
bar_chart = alt.Chart(max_age_by_platform).mark_bar().encode(
    x=alt.X('platform:N', title='Platform'),
    y=alt.Y('Purchase amount:Q', title='Max Purchase amount'),
    color=alt.Color('platform:N', legend=None),
    tooltip=['platform', 'age']
).properties(
    width=600,
    height=400,
    title='Max Purchase amount by Platform'
)
st.altair_chart(bar_chart, use_container_width=True)

# Gender Distribution (Grouped Bar Chart)
gender_counts = df['Gender'].value_counts()
gender_chart = alt.Chart(gender_counts.reset_index()).mark_bar().encode(
    x=alt.X('index:N', title='Gender'),
    y=alt.Y('Gender:Q', title='Count'),
    tooltip=['index:N', 'Gender:Q']
).properties(
    width=600,
    height=400,
    title='Gender Distribution'
)
st.altair_chart(gender_chart, use_container_width=True)

# Platform Distribution (Pie Chart)
platform_counts = df['Platform'].value_counts()
platform_chart = alt.Chart(platform_counts.reset_index()).mark_bar().encode(
    x=alt.X('index:N', title='Platform'),
    y=alt.Y('Platform:Q', title='Count'),
    tooltip=['index:N', 'Platform:Q']
).properties(
    width=600,
    height=400,
    title='Platform Distribution'
)
st.altair_chart(platform_chart, use_container_width=True)


