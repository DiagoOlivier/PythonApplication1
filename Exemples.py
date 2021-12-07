string = "CC"
a =(ord("C")) # code ASCII du caractéres
b= (format(ord("c"),'b')) #binaire du code ascii du caratere
binary_converted = ''.join(format(ord(c), 'b') for c in string) # binaire de la chaine de caractères
