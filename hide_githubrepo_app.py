import streamlit as st

def hide_github_icon():
    hide_github_style = """
        <style>
        .stApp header .decoration {
            display: none;
        }
        </style>
    """
    st.markdown(hide_github_style, unsafe_allow_html=True)

def main():
    st.title("My Simple Streamlit App")
    st.write("This is a simple app with the GitHub icon hidden.")

    # Call the function to hide the GitHub icon
    hide_github_icon()

if __name__ == "__main__":
    main()
  
