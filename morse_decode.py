import pandas as pd
from dotenv import main
import os
import ast
import datetime
import argparse

# Carrega o arquivo .env
main.load_dotenv(dotenv_path=".env")

# Pega a variavel MORSE_CODE e transforma de volta em dicionário
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

def save_msg(msg, code_msg, file_path):
    now = datetime.datetime.now()
    df = pd.DataFrame([[msg, code_msg, now]], columns=['mensagem', 'mensagem_codificada', 'datetime'])

    if os.path.exists(file_path):
        hdr = False
    else:
        hdr = True

    df.to_csv(file_path, mode='a', header=hdr, index=False)

def main():
    parser = argparse.ArgumentParser(description="Transforma a mensagem em codigo morse.")
    
    parser.add_argument('-msg', type=str, help='A mensagem para codificar. (Não usar acentos, nem caracteres especiais)')
    parser.add_argument('-file', type=str, help='Onde salvar a mensagem.')
    
    args = parser.parse_args()

    if args.msg and args.file:
        coded_msg = morse_code_function(args.msg, morse_code)
        save_msg(args.msg, coded_msg, args.file)
        print("Mensagem salva com sucesso.")
    else:
        print("Adicionar uma mensagem ou o caminho do arquivo.")

if __name__ == "__main__":
    main()

    
    