import random


upper =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    # upper = alle hoofdletters
lower = upper.lower()           # lowers = alle kleine letters
numbers = "0123456789"          # numbers = alle nummers
symbols = "&@#{[^!})$><*"       # symbols = alle symbolen dat je hebt opgegeven

string = upper + lower + numbers + symbols  # hier zegt gij string = al deze variabelen 
lenght = 12  # dit word de lengte van u password
password = "".join(random.sample(string, lenght))  #The string join() method returns a string by joining all the elements of an iterable (list, string, tuple), separated by the given separator.
                                                   # random.sample returns a particular length list of items chosen from the sequence dus hier gaat die random iets uitpikken van de variabel string met een de opgegeven lengte in lenght dus 12.
print("Your new Password IS: " + password)  # Hier gaat die dus je nieuwe password printen in u terminal

