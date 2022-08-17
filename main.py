
from Atbash import Atbash
from Cesar import Cesar
from Gronsfield import Gronsfield
from Prison import Prison
from Simple_Permutation import Simple_Permutation

import logging


def Encoding_Manager() -> bool:

    atbash = Atbash()
    cesar = Cesar()
    gronsfield = Gronsfield()
    prison = Prison()
    sim_permutation = Simple_Permutation()

    print("Choose the method which you want yo use.\n"
          "___________________________________________\n"
          "ATBASH method    *************   Type 1\n"
          "CESAR method     *************   Type 2\n"
          "GRONSFIELD method ************   Type 3\n"
          "PRISON method    *************   Type 4\n"
          "SIMPLE PERMUTATION method    *   Type 5\n")

    method = int(input())

    print("\nChoose the code way.\n"
          "___________________________________________\n"
          "ENCODING     *************   Type 1\n"
          "DECODING     *************   Type 2")

    way = int(input())

    print("Type original or encoded message\n"
          "___________________________________________\n")

    message = input()


    if method == 1 and way == 1:
        print(atbash.encoding(message))

    if method == 1 and way == 2:
        print(atbash.decoding(message))

    if method == 2 and way == 1:
        key = int(Cesar_key_request())
        print(cesar.encoding(message, key))

    if method == 2 and way == 2:
        key = int(Cesar_key_request())
        print(cesar.decoding(message, key))

    if method == 3 and way == 1:
        key = Gronsfield_key_request()
        print(gronsfield.encoding(message, key))

    if method == 3 and way == 2:
        key = Gronsfield_key_request()
        print(gronsfield.decoding(message, key))

    if method == 4 and way == 1:
        print(prison.encoding(message))

    if method == 4 and way == 2:
        print(prison.decoding(message))

    if method == 5 and way == 1:
        print(sim_permutation.encoding(message))

    if method == 5 and way == 2:
        print(sim_permutation.decoding(message))


    print("\n"
          "___________________________________________\n"
          "CONTINUE    *************   Type 1\n"
          "EXIT        *************   Type 2\n"
          "          and press ENTER\n")

    choosing = int(input())

    if choosing == 1:
        exit = False
    else:
        exit = True

    return exit



def Cesar_key_request():

    print("Enter the key\n"
          "___________________________________________\n")
    key = input()

    return key



def Gronsfield_key_request():
    
    print("Enter number of keys\n"
          "___________________________________________\n")
    sum_keys = int(input())
    key = list()

    for i in range(0, sum_keys):
        print("Enter the", i + 1, "key")

        key_elemet = int(input())
        key.append(key_elemet)

    return key





if __name__ == '__main__':

    logging.basicConfig(filename="bezpechnost.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')

    logger = logging.getLogger()

    logger.setLevel(logging.DEBUG)

    logger.warning("OOPS!!!Its a Warning")

    exit = False

    while exit == False:
        exit = Encoding_Manager()













