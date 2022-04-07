import plotly.express as px
import pandas as pd
import streamlit as st


def main():
    st.title("Jadual Sifir")

    choice = st.sidebar.selectbox('Menu', ['Home', 'Tentang'])
    if choice == 'Home':
        st.subheader('Home')

        # Layout 
        col1, col2 = st.columns([1,2])

        with col1:
            with st.form(key = 'myform'):
                number = st.text_input('Enter Number')
                end_number = st.number_input('End Number', min_value=12, max_value=200)
                submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                with col2:
                    with st.expander('Times Table'):
                        for i in range(1, (end_number + 1)):
                            answer = i * int(number)
                            st.write(f"{i} x {number} = {answer}")
                    
                    # Times Table as DataFrame
                    range_num = list(range(1, end_number))
                    multiplication = [f"{i} x {number} = " for i in range(1, end_number)]
                    answer = [i * int(number) for i in range(1, end_number)]
                    df = pd.DataFrame({'Numbers' : range_num, 'Multiplication' : multiplication, 'Answer' : answer})
                    st.dataframe(df)

                    # Plot
                    p1 = px.bar(df, x = 'Numbers' , y = 'Answer', color = 'Numbers')
                    st.plotly_chart(p1)


if __name__ == '__main__':
    main()