import pandas as pd
from dotenv import main
import os
import ast
import datetime
import argparse

# Carrega o arquivo .env
main.load_dotenv(dotenv_path=".env")

# Pega a variavel MORSE_CODE e transforma de volta em dicionário e inverte para ser usada na tradução
morse_code_str = os.getenv("MORSE_CODE")
morse_code = ast.literal_eval(morse_code_str)
reverse_morse_code_dict = {value: key for key, value in morse_code.items()}

# Função que traduz o código.
def morse_code_function(msg, dict):
    coded_words = msg.split("  ")
    decoded_msg = [] 
    for word in coded_words:
        decoded_word = []
        word_list = word.split(" ") 
        for letter in word_list:
            decoded_word.append(dict[letter])
            word_code = "".join(decoded_word)
        decoded_msg.append(word_code)    
    return " ".join(decoded_msg)

# Armazena as mensagens recebidas
def save_msg(msg_recebida, msg_traduzida, file_path):
    now = datetime.datetime.now()
    df = pd.DataFrame([[msg_recebida, msg_traduzida, now]], columns=['mensagem_recebida', 'mensagem_traduzida', 'datetime'])

    if os.path.exists(file_path):
        hdr = False
    else:
        hdr = True

    df.to_csv(file_path, mode='a', header=hdr, index=False)

def main():
    parser = argparse.ArgumentParser(description="Traduz codigo morse.")
    
    parser.add_argument('-msg', type=str, help='A mensagem para se decodificada. (Espaço duplo entre palavas e simples entre letras)')
    parser.add_argument('-file', type=str, help='Onde salvar a mensagem.')
    
    args = parser.parse_args()

    if args.msg and args.file:
        coded_msg = morse_code_function(args.msg, reverse_morse_code_dict)
        save_msg(args.msg, coded_msg, args.file)
        print("Mensagem salva com sucesso.")
        print(args.msg)
        print(coded_msg)
    else:
        print("Adicionar uma mensagem ou o caminho do arquivo.")

if __name__ == "__main__":
    main()
