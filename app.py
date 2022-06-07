import pandas as pd 
import streamlit as st
import os 

def main():
    st.title("This is the application to read the text file and replace the specific context of the file.")
    text_file= st.file_uploader("Upload the text file", type=["txt"])
    try:
        if text_file is not None:
            text_data= text_file.read().decode("utf-8")
            st.write(text_data)

        # Code to replace the specific context of the file
            original_string = st.text_input("Enter the original string to be replaced")
            new_string = st.text_input("Enter the new string to replace the original string")

            new_text_data = text_data.replace(original_string, new_string)
            st.write(new_text_data)



    except Exception as e:
        message= "Something went Wrong while uploading the text file. Kindly try once again."
        st.error(message)






if __name__== "__main__":
    main()