import pandas as pd
from dotenv import main
import os
import ast

# Load the .env file

main.load_dotenv(dotenv_path=".env")

# Get the MORSE_CODE variable and convert it back to a dictionary
morse_code_str = os.getenv("MORSE_CODE")
morse_code = ast.literal_eval(morse_code_str)

def morse_code_function(msg, dict):
    
    words = msg.split()
    code_msg = []
    for word in words:
        morse_word = []
        for letter in word:
            morse_word.append(dict[letter.upper()])
            word_code = " ".join(morse_word)
        code_msg.append(word_code)
    
    return "  ".join(code_msg)

