import streamlit as st

def hide_streamlit_elements():
    hide_github_icon = """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob, 
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137, 
    .viewerBadge_text__1JaDK { 
        display: none; 
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
    st.markdown(hide_github_icon, unsafe_allow_html=True)

def main():
    st.title("My Simple Streamlit App")
    st.write("This is a simple app with custom UI elements hidden.")

    # Call the function to hide specific Streamlit elements
    hide_streamlit_elements()

if __name__ == "__main__":
    main()
