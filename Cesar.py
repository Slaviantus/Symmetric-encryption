
#========  Cesar method  =======

class Cesar:

    def __init__(self):

        self.__rus_alphabet = (
        'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж',
        'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О',
        'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц',
        'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю',
        'Я', ' ', ',', '.')

        self.__eng_alphabet = (
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z', '.', ',', ' ')

        self.__alphabet = self.__rus_alphabet



    def encoding(self, message: str, key: int) -> tuple:

        message = self.__string_to_list(message)
        ciphertext = list()

        for i in range(0, len(message)):

            for j in range(0, len(self.__alphabet)):

                if message[i] == self.__alphabet[j]:

                    if j + key + 1 <= len(self.__alphabet):
                        ciphertext.append(self.__alphabet[j + key])

                    else:
                        ciphertext.append(self.__alphabet[j + key  - len(self.__alphabet)])

        return self.__list_to_string(ciphertext), key



    def decoding(self, ciphertext: str, key: int) -> str:

        ciphertext = self.__string_to_list(ciphertext)
        message = list()

        for i in range(0, len(ciphertext)):

            for j in range(0, len(self.__alphabet)):

                if ciphertext[i] == self.__alphabet[j]:

                    if j - key >= 0:
                        message.append(self.__alphabet[j - key])

                    else:
                        message.append(self.__alphabet[len(self.__alphabet) - abs(j - key)])

        return self.__list_to_string(message)




    def __list_to_string(self, message: list) -> str:
        """Convert from list of characters to string"""
        return ''.join(message)


    def __string_to_list(self, message: str) -> list:
        """Convert from string to list of characters"""
        char_list = list()

        for char in message:
            char_list.append(char)

        return char_list