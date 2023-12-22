import os 
import pyaes

file_name = 'teste.txt.ransomwaretroll'

file = open(file_name, 'rb')

file_data = file.read()

file.close()

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
descrypt_data = aes.descrypt(file_data)

os.remove(file_name)

new_file = 'teste.txt'
new_file = open(f'{new_file}','wb')
new_file.write(descrypt_data)
new_file.close()