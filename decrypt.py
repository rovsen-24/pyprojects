import pyAesCrypt
import os
import sys

def decryption(file,password):
  buffer_size = 512 * 1024
  pyAesCrypt.decryptFile(
    str(file),
    str(os.path.splitext(file)[0]),
    password,
    buffer_size
  )
  print("[File" , str(os.path.splitext(file)[0]) ,"is decrypted]")
  os.remove(file)


def search_dir(dir,password):
  for name in os.listdir(dir):
    path = os.path.join(dir,name)

    if os.path.isfile(path):
      try:
        decryption(path,password)
      except Exception as ex:
        print(ex)
    else:
      search_dir(path,password)

#search for already encrypted files with '.crp' ext 
password = input("write a password to decrypt: ")
search_dir(input("directory for decrypt files: (for ex: /home/Desktop/folder/)"), password)