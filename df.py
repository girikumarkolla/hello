# import the Playfair library
import playfair

# create a Playfair object for encrypting and decrypting
ph = playfair.Playfair()

# set the password for upcoming encryptions or decryptions
ph.setPassword('Caput Draconis')

# encrypt a plain text phrase and print it out
print (ph.encrypt('Emma Watson is the most talented actress.'))
