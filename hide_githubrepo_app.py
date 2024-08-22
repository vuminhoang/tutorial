import streamlit as st

def hide_specific_elements():
    hide_elements_style = """
    <style>
    .viewerBadge_container__1QSob, .styles_viewerBadge__1yB5_, 
    .viewerBadge_link__1S137, .viewerBadge_text__1JaDK { 
        display: none !important; 
    } 
    footer { 
        visibility: hidden; 
    } 
    header { 
        visibility: hidden; 
    }
    </style>
    """
    st.markdown(hide_elements_style, unsafe_allow_html=True)

def main():
    st.title("My Simple Streamlit App")
    st.write("This is a simple app with the GitHub icon, header, and footer hidden.")

    # Hide specific elements while keeping the settings menu
    hide_specific_elements()

if __name__ == "__main__":
    main()
