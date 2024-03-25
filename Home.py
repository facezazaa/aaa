import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend which doesn't require a display
import matplotlib.pyplot as plt

import streamlit as st
import seaborn as sns
import pandas as pd

gender_data = pd.read_csv('./data/onlinefoods.csv')

html_example_table = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>ตัวอย่างตารางข้อมูล</h3></center>
</div>
"""
st.markdown(html_example_table, unsafe_allow_html=True)
st.write(gender_data.head(10))

html_count_by_age = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>จำนวนเพศตามช่วงอายุ</h3></center>
</div>
"""
st.markdown(html_count_by_age, unsafe_allow_html=True)

plt.figure(figsize=(15, 5))
sns.countplot(x='Gender', data=gender_data)  # แก้เป็น gender_data แทน shopping_trends.csv
plt.title('จำนวนเพศตามช่วงอายุ')
plt.xlabel('เพศ')
plt.ylabel('จำนวน')
plt.xticks(rotation=45)
st.pyplot()

html_sales_by_gender = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>ยอดขายอาหาร</h3></center>
</div>
"""
st.markdown(html_sales_by_gender, unsafe_allow_html=True)

plt.figure(figsize=(15, 5))
sns.countplot(x='Gender', data=gender_data)  # แก้เป็น gender_data แทน shopping_trends.csv
plt.title('ยอดขายอาหาร')
plt.xlabel('ภูมิภาค')
plt.ylabel('จำนวน')
plt.xticks(rotation=45)
st.pyplot()



