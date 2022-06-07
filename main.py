import streamlit as st
from src.text_reading import TextReplacement, TextReading

def main():
    st.title("This is the application to read the text file and replace the specific context of the file.")
    text_file= st.file_uploader("Upload the text file", type=["txt"])
    try:
        if text_file is not None:
            text_data_reading_object= TextReplacement()
            text_data=text_data_reading_object.read_text(text_file)
            st.write(text_data)
            original_string = st.text_input("Enter the original string to be replaced")
            new_string = st.text_input("Enter the new string to replace the original string")

            new_text_data = text_data_reading_object.replace_text(text_data, original_string, new_string)   
            st.write(new_text_data)
    except Exception as e:
        message= "Something went Wrong while uploading the text file. Kindly try once again."
        st.error(message+'\n'+str(e))

if __name__ == '__main__':

    main()