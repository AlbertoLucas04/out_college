import string

print('Olá, seja bem-vindo(a) ao Testador de Palíndromos!')

def isaPalindrome(str):
    exclude = set(string.punctuation)
    str = ' '.join(ch for ch in str if ch not in exclude)
    str = str.replace(" ", "").lower()
    if str == str[::-1]:
        return str + " é um Palíndormo!"
    else:
        return str + " não é um Palíndormo!"

def main():
    user_sentence = str(input('Insira uma Palavra e/ou Frase: '))
    print(isaPalindrome(user_sentence))

if __name__ == "__main__":
    main()


