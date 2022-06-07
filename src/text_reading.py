import os 
import shutil
from abc import ABC, abstractmethod
import streamlit as st


class ReadingText(ABC):

    @abstractmethod
    def read_text(self, text_file):
        pass

class TextReading(ReadingText):

    def read_text(self, text_file):
        try:
            if text_file is not None:
                text_data= text_file.read().decode("utf-8")
                return text_data
        except Exception as e:
            st.error("Something went Wrong while uploading the text file. Kindly try once again."+'\n'+str(e))  
            return None

class TextReplacement(ReadingText):
    
        def replace_text(self, text_data, original_string, new_string):
            try:
                if text_data is not None:
                    new_text_data = text_data.replace(original_string, new_string)
                    return new_text_data
            except Exception as e:
                st.error("Something went Wrong while uploading the text file. Kindly try once again."+'\n'+str(e))  
                return None