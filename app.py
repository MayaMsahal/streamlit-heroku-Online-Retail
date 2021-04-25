import streamlit as st

def main():

    # Defining header title
    st.sidebar.title("Streamlit Forecasting")
    st.sidebar.title("What to do")
    app_mode = st.sidebar.selectbox(
        "Choose the app mode", ["Show instructions", "Run Forecasting"]
    )

    # Defining control flow of the app
    if app_mode == "Show instructions":
        st.sidebar.success('To continue select "Run Forecasting"')
    elif app_mode == "Run Forecasting":
        st.text("Forecasting")


if __name__ == "__main__":
    main()
