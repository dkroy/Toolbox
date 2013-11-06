import string


class rot13:


    @staticmethod
    def decrypt(message):
        return rot13.encrypt(message)
        
        
    @staticmethod
    def encrypt(message):
        rot13 = string.maketrans( 
            "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
            "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
        return string.translate(str(message), rot13)

        
