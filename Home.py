import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

# Show Data Index Price
st.header("Show Data Index Price")
df = pd.read_csv("./data/shopping_trends.csv")
st.write(df.head(10))

# Show Chart
st.header("Show Chart")

# Age Distribution by Platform (Grouped Bar Chart)
age_range = st.slider("Select age range", min_value=df["Age"].min(), max_value=df["Age"].max(), value=(df["Age"].min(), df["Age"].max()))
filtered_df = df[(df["Age"] >= age_range[0]) & (df["Age"] <= age_range[1])]
chart = alt.Chart(filtered_df).mark_bar().encode(
    x=alt.X('Age', title='Age'),
    y=alt.Y('count()', title='Count'),
    color='Platform:N',
    tooltip=['Platform', 'Age']
).properties(
    width=600,
    height=400,
    title='Age Distribution by Platform'
).configure_title(
    fontSize=20,
    fontWeight='bold',
    color='gray'
).configure_axis(
    labelFontSize=12,
    titleFontSize=16,
    titleFontWeight='normal'
)
st.altair_chart(chart, use_container_width=True)

# Time Spent Distribution by Platform (Grouped Bar Chart)
chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('Platform:N', title='Platform'),
    y=alt.Y('Time Spent', title='Time Spent'),
    color='Platform:N',
    tooltip=['Platform', 'Time Spent']
).properties(
    width=600,
    height=400,
    title='Time Spent Distribution by Platform'
)
st.altair_chart(chart, use_container_width=True)

# Max Age by Platform (Grouped Bar Chart)
max_age_by_platform = df.groupby('Platform')['Age'].max().reset_index()
bar_chart = alt.Chart(max_age_by_platform).mark_bar().encode(
    x=alt.X('Platform:N', title='Platform'),
    y=alt.Y('Age:Q', title='Max Age'),
    color=alt.Color('Platform:N', legend=None),
    tooltip=['Platform', 'Age']
).properties(
    width=600,
    height=400,
    title='Max Age by Platform'
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
fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(platform_counts, labels=platform_counts.index, autopct='%1.1f%%', startangle=140, colors=['#FF9999', '#66B2FF', '#99FF99'])
ax.set_title('Platform Distribution')
st.pyplot(fig)


# Platform Distribution (Pie Chart)
platform_counts = df.groupby('platform').size()
fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(platform_counts, labels=platform_counts.index, autopct='%1.1f%%', startangle=140, colors=['#FF9999', '#66B2FF', '#99FF99'])
ax.set_title('Platform Distribution')
st.pyplot(fig)

