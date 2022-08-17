
#========  Method Simple Permutation  =======

class Simple_Permutation:

    def __init__(self):

        self.__cols = 3


    def encoding(self, message: str) -> str:

        message = self.__string_to_list(message)
        ciphertext = list()
        self.__matrix = list()


        remainder = len(message) % self.__cols
        height = int((len(message) - remainder) / self.__cols)
        k = 0

        for i in range(0, self.__cols + 1):
            self.__matrix.append(list())

            for j in range(0, height):

                if k < len(message):
                    self.__matrix[i].append(message[k])
                    k = k + 1

                else:
                    self.__matrix[i].append("*")

        for j in reversed(range(0, height)):

            for i in reversed(range(0, self.__cols + 1)):

                ciphertext.append(self.__matrix[i][j])

        return self.__list_to_string(ciphertext)




    def decoding(self, ciphertext: str) -> str:

        ciphertext = self.__string_to_list(ciphertext)
        message = list()
        height = int(len(ciphertext) / 4)

        for delay in range(0, 4):

            for j in range(len(ciphertext) - 1, 0, -4):
                message.append(ciphertext[j - delay])

        clean_message = list()

        for i in range(0, len(message)):

            if message[i] != "*":
                clean_message.append(message[i])

        return self.__list_to_string(clean_message)





    def __list_to_string(self, message: list) -> str:
        """Convert from list of characters to string"""
        return ''.join(message)



    def __string_to_list(self, message: str) -> list:
        """Convert from string to list of characters"""
        char_list = list()

        for char in message:
            char_list.append(char)

        return char_list