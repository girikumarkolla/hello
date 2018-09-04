# import the Playfair library
import playfair

# create a Playfair object for encrypting and decrypting
ph = playfair.Playfair()

ph.setPassword('Caput Draconis')


print (ph.encrypt('Emma Watson is the most talented actress.'))
