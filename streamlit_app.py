import time
from PIL import Image
import streamlit as st
import pandas as pd

my_logo_path = "./light.png"
my_logo = Image.open(my_logo_path)
st.set_page_config(
    page_title="Ribo",
    page_icon=my_logo,
    layout="wide",
    initial_sidebar_state="auto",
)

print('Started script...', end='')


@st.cache(max_entries=2, ttl=600)
def download_data(quarter):
    sales = [100, 200, 300, 400]
    time.sleep(3)
    return sales[quarter - 1]


def main():
    st.title('Sales Report')
    # st.header('Q1 Results')
    q1_sales = {
        'January': 100,
        'February': 110,
        'March': 115
    }
    q2_sales = {
        'April': 150,
        'May': 200,
        'June': 250
    }
    q2_df = pd.DataFrame(q2_sales.items(),
                         columns=['Month', 'Amount'])
    q1_df = pd.DataFrame(q1_sales.items(),
                         columns=['Month', 'Amount'])
    section = st.sidebar.radio('Which section?',
                               ('Home', 'Text', 'Charts',
                                'Widgets', 'More widgets',
                                'Caching'))
    if section == 'Home':
        st.image(image=Image.open('joudy_joumana.jpg'),
                 caption='Ribo',
                 use_column_width=True)
        st.markdown('**Ribo** is a **streamlit** app that is used to '
                    'demonstrate how to use **streamlit** to create '
                    'interactive web apps.')
    if section == 'Text':
        show_text(q1_sales, q2_df)
    elif section == 'Charts':
        show_charts(q1_sales, q2_df, q2_sales)
    elif section == 'Widgets':
        show_widgets(q1_df, q2_df)
    elif section == 'More widgets':
        show_more_widgets()
    elif section == 'Caching':
        quarter = st.number_input('Which quarter?', 1, 4)
        sales_amount = download_data(quarter)
        st.write('Sales amount: ', sales_amount)


def show_more_widgets():
    st.write(st.slider('Which quarters?', 1, 4, (1, 2)))
    st.write(st.multiselect('Choose quarters',
                            ['Q1', 'Q2', 'Q3', 'Q4']))
    st.write(st.number_input('Which quarter?', 1, 4))


def show_widgets(q1_df, q2_df):
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


def show_charts(q1_sales, q2_df, q2_sales):
    st.line_chart(q2_df.set_index('Month'))
    st.area_chart(q2_df.set_index('Month'))
    st.bar_chart([q1_sales.values(), q2_sales.values()])
    from PIL import Image
    st.image(image=Image.open('visualization.png'),
             caption='Starting from origin')


def show_text(q1_sales, q2_df):
    st.write('January was the start of the year')
    st.write(q1_sales)
    st.header('Q2 Results')
    'Q2 had better results:smile:'
    st.table(q2_df)
    st.dataframe(q2_df)


main()
print('finished script')
