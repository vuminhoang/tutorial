import streamlit as st

def hide_elements():
    hide_elements_style = """
    <style>
    /* Hide the GitHub icon */
    .viewerBadge_container__1QSob {
        display: none !important;
    }
    /* Hide the header */
    header {
        visibility: hidden !important;
    }
    /* Hide the footer */
    footer {
        visibility: hidden !important;
    }
    </style>
    """
    st.markdown(hide_elements_style, unsafe_allow_html=True)

def main():
    st.title("My Simple Streamlit App")
    st.write("This app hides the GitHub icon, header, and footer while keeping the settings menu visible.")

    # Hide the specific elements
    hide_elements()

if __name__ == "__main__":
    main()
