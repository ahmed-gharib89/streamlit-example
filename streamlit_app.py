from PIL import Image
import streamlit as st
import pandas as pd

st.title('Sales Report')

st.header('Q1 Results')

q1_sales = {
    'January': 100,
    'February': 110,
    'March': 115
}

st.write('January was the start of the year')
st.write(q1_sales)

st.header('Q2 Results')

q2_sales = {
    'April': 150,
    'May': 200,
    'June': 250
}

'Q2 had better results:smile:'
q2_df = pd.DataFrame(q2_sales.items(),
                     columns=['Month', 'Amount'])
q1_df = pd.DataFrame(q1_sales.items(),
                     columns=['Month', 'Amount'])

st.table(q2_df)
st.dataframe(q2_df)


st.line_chart(q2_df.set_index('Month'))
st.area_chart(q2_df.set_index('Month'))

st.bar_chart([q1_sales.values(), q2_sales.values()])

st.image(image=Image.open('visualization.png'),
         caption='Starting from origin')


if st.button('Show Q2 Data'):
    st.table(q2_df)
else:
    st.table(q1_df)

if st.checkbox('Show Q2 Data'):
    st.line_chart(q2_df.set_index('Month'))
else:
    st.line_chart(q1_df.set_index('Month'))

quarter = st.radio('Which quarter?', ('Q1', 'Q2'))
if quarter == 'Q1':
    st.line_chart(q1_df.set_index('Month'))
elif quarter == 'Q2':
    st.line_chart(q2_df.set_index('Month'))


selected_quarter = st.selectbox('Which quarter?', ('Q1', 'Q2'))
if selected_quarter == 'Q1':
    st.area_chart(q1_df.set_index('Month'))
elif selected_quarter == 'Q2':
    st.area_chart(q2_df.set_index('Month'))
