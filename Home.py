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
age_range = st.slider("Select age range", min_value=df["age"].min(), max_value=df["age"].max(), value=(df["age"].min(), df["age"].max()))
filtered_df = df[(df["age"] >= age_range[0]) & (df["age"] <= age_range[1])]
chart = alt.Chart(filtered_df).mark_bar().encode(
    x=alt.X('age', title='Age'),
    y=alt.Y('count()', title='Count'),
    color='platform:N',
    tooltip=['platform', 'age']
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
    x=alt.X('platform:N', title='Platform'),
    y=alt.Y('time_spent', title='Time Spent'),
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
    y=alt.Y('age:Q', title='Max Age'),
    color=alt.Color('platform:N', legend=None),
    tooltip=['platform', 'age']
).properties(
    width=600,
    height=400,
    title='Max Age by Platform'
)
st.altair_chart(bar_chart, use_container_width=True)

# Gender Distribution (Grouped Bar Chart)
NumM = df[df['gender'] == 'male'].count()
NumF = df[df['gender'] == 'female'].count()
dtSex = [NumM.iloc[0], NumF.iloc[0]]
dtSexb = pd.DataFrame(dtSex, index=["Male", "Female"], columns=["Count"])
st.bar_chart(dtSexb)

# Platform Distribution (Pie Chart)
platform_counts = df.groupby('platform').size()
fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(platform_counts, labels=platform_counts.index, autopct='%1.1f%%', startangle=140, colors=['#FF9999', '#66B2FF', '#99FF99'])
ax.set_title('Platform Distribution')
st.pyplot(fig)

