""" 
[Hard] – Enigma Cipher (5 points)

The Enigma machine is a fairly complex cipher machine used by the Germans and others during World War II to encrypt their messages. The Enigma code was famously broken by Alan Turing during the war, using one of the world's first "computers". It is your job to implement the German Enigma machine.

For the full problem description, please see the following Gist: https://gist.github.com/vasilescur/31a79ad9ff3b4894c7aa0e57af041925

Test Cases:
encrypt([4, 1, 5], ['H', 'P', 'G'], "AAAAAAAAA") -> "RPWKMBZLN"
encrypt([1, 2, 3], ['A', 'A', 'A'], "PROGRAMMINGPUZZLES") -> "RTFKHDOVZSXTRMVPFC"
encrypt([1, 2, 3], ['A', 'A', 'A'], "RTFKHDOVZSXTRMVPFC") -> "PROGRAMMINGPUZZLES"
encrypt([2, 5, 3], ['U', 'L', 'I'], "GIBDZNJLGXZ") -> "UNCRACKABLE" 
"""
alpha =          'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
reflection =     'YRUHQSLDPXNGOKMIEBFZCWVJAT'
rotors = {  '1': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
            '2': 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
            '3': 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
            '4': 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
            '5': 'VZBRGITYUPSDNHLXAWMJQOFECK'}

notches = { 1: 'Q',
            2: 'E',
            3: 'V',
            4: 'J',
            5: 'Z'}

class Rotor():


    def __init__(self, rotor_num, notch):
        #find index of start position in base alphabet
        self.notch = notch
        self.rotor_num = rotor_num
        i = alpha.index(notch)
        #set encrypted alphabet for rotor
        encrypted_alpha = rotors.get(str(rotor_num))
        #shift based on starting position
        self.shifted_encrypted_alpha = encrypted_alpha[i:] + encrypted_alpha[:i]
        self.position = self.shifted_encrypted_alpha[0]
        

    def rotate(self):
        self.shifted_encrypted_alpha = self.shifted_encrypted_alpha[1:] + self.shifted_encrypted_alpha[0]
        self.position = self.shifted_encrypted_alpha[0]
    
    def sub_char(self, char):
        return self.shifted_encrypted_alpha[alpha.index(char)]

    def reverse_sub_char(self, char):
        return alpha[self.shifted_encrypted_alpha.index(char)]

def encrypt(rotor_nums, notches, msg):
    encrypted_msg = ''
    rotor1 = Rotor(rotor_nums[0], notches[0])
    rotor2 = Rotor(rotor_nums[1], notches[1])
    rotor3 = Rotor(rotor_nums[2], notches[2])

    for char in msg:
        c = rotor1.sub_char(char)
        c = rotor2.sub_char(c)
        c = rotor3.sub_char(c)
        c = reflect(c)
        c = rotor3.reverse_sub_char(c)
        c = rotor2.reverse_sub_char(c)
        c = rotor1.reverse_sub_char(c)
        encrypted_msg = encrypted_msg + str(c)

        if rotor2.position == rotor2.notch:
            rotor3.rotate()
            rotor2.rotate()
        if rotor1.position == rotor1.notch:
            rotor2.rotate()
        rotor1.rotate()


    print(encrypted_msg)

def reflect(char):
    return reflection[alpha.index(char)]

if __name__ == '__main__':
    encrypt([4, 1, 5], ['H', 'P', 'G'], "AAAAAAAAA") # -> "RPWKMBZLN"
    encrypt([1, 2, 3], ['A', 'A', 'A'], "PROGRAMMINGPUZZLES") # -> "RTFKHDOVZSXTRMVPFC"
    encrypt([1, 2, 3], ['A', 'A', 'A'], "RTFKHDOVZSXTRMVPFC") # -> "PROGRAMMINGPUZZLES"
    encrypt([2, 5, 3], ['U', 'L', 'I'], "GIBDZNJLGXZ") # -> "UNCRACKABLE" 
