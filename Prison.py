
#========  Prison method  =======

class Prison:

    def __init__(self):

        self.__cipher_table = (('А', 'Б', 'В', 'Г'),
                               ('Д', 'Е', 'Ё', 'Ж'),
                               ('З', 'И', 'Й', 'К'),
                               ('Л', 'М', 'Н', 'О'),
                               ('П', 'Р', 'С', 'Т'),
                               ('У', 'Ф', 'Х', 'Ц'),
                               ('Ч', 'Ш', 'Щ', 'Ъ'),
                               ('Ы', 'Ь', 'Э', 'Ю'),
                               ('Я', ' ', ',', '.'))


    def encoding(self, message: str) -> tuple:

        message = self.__string_to_list(message)
        cipher = list()


        for i in range(0, len(message)):

            for j in range(0, len(self.__cipher_table)):

                for k in range(0, len(self.__cipher_table[j])):

                    if message[i] == self.__cipher_table[j][k]:

                        cipher.append(str(j + 1))
                        cipher.append(str(k + 1))

        return self.__list_to_string(cipher)


    def decoding(self, cipher: str) -> str:

        cipher = self.__string_to_list(cipher)
        message = list()

        for i in range(0, len(cipher), 2):

            message.append(self.__cipher_table[int(cipher[i]) - 1][int(cipher[i + 1]) - 1])

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