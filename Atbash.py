
#========  Method Atbash  =======

class Atbash:

    def __init__(self):

        self.__rus_alphabet = (
        'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж',
        'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О',
        'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц',
        'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю',
        'Я', ' ', ',', '.')

        self.__rus_atbash_alphabet = (
        '.', ',', ' ', 'Я', 'Ю', 'Э', 'Ь', 'Ы',
        'Ъ', 'Щ', 'Ш', 'Ч', 'Ц', 'Х', 'Ф', 'У',
        'Т', 'С', 'Р', 'П', 'О', 'Н', 'М', 'Л',
        'К', 'Й', 'И', 'З', 'Ж', 'Ё', 'Е', 'Д',
        'Г', 'В', 'Б', 'А')

        self.__eng_alphabet = (
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z', '.', ',', ' ')

        self.__eng_atbash_alphabet = (
        ' ', ',', '.', 'Z', 'Y', 'X', 'W', 'V',
        'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N',
        'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F',
        'E', 'D', 'C', 'B', 'A')

        self.__alphabet = self.__rus_alphabet
        self.__atbash_alphabet = self.__rus_atbash_alphabet




    def encoding(self, message: str) -> str:    # message has to be in capital cyrilic letters

        message = self.__string_to_list(message)
        ciphertext = list()

        for i in range(0, len(message)):

            for j in range(0, len(self.__alphabet)):

                if message[i] == self.__alphabet[j]:

                    ciphertext.append(self.__atbash_alphabet[j])


        return self.__list_to_string(ciphertext)




    def decoding(self, ciphertext: str) -> str:

        ciphertext = self.__string_to_list(ciphertext)
        message = list()

        for i in range(0, len(ciphertext)):

            for j in range(0, len(self.__atbash_alphabet)):

                if ciphertext[i] == self.__atbash_alphabet[j]:

                    message.append(self.__alphabet[j])


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

