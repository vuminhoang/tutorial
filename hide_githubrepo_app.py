import streamlit as st

def hide_streamlit_elements():
    hide_elements_style = """
    <style>
    .viewerBadge_container__1QSob, .styles_viewerBadge__1yB5_, 
    .viewerBadge_link__1S137, .viewerBadge_text__1JaDK { 
        display: none !important; 
    } 
    #MainMenu { 
        visibility: hidden; 
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
    st.write("This is a simple app with custom UI elements hidden.")

    # Hide specific Streamlit elements
    hide_streamlit_elements()

if __name__ == "__main__":
    main()
