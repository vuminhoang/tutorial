import streamlit as st

def hide_github_and_footer():
    hide_elements_style = """
    <style>
    /* Hide the GitHub icon */
    .viewerBadge_container__1QSob { 
        display: none !important; 
    } 
    /* Hide the footer */
    footer { 
        visibility: hidden; 
    } 
    /* Hide the header */
    header { 
        visibility: hidden; 
    }
    </style>
    """
    st.markdown(hide_elements_style, unsafe_allow_html=True)

def main():
    st.title("My Simple Streamlit App")
    st.write("This app hides the GitHub icon, header, and footer but keeps the settings menu visible.")

    # Call the function to hide specific elements
    hide_github_and_footer()

if __name__ == "__main__":
    main()


def main():
    st.title("My Simple Streamlit App")
    st.write("This is a simple app with the GitHub icon, header, and footer hidden.")

    # Hide specific elements while keeping the settings menu
    hide_specific_elements()

if __name__ == "__main__":
    main()
