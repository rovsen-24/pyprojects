import pyAesCrypt
import os
import sys

def encryption(file,password):
  #default buffersize
  buffer_size = 512 * 1024
  pyAesCrypt.encryptFile(
    str(file),
    str(file) + ".crp",
    password,
    buffer_size
  )
  print("[File" , str(os.path.splitext(file)[0]) ,"is encrypted]")
  os.remove(file)


def search_dir(dir,password):
  for name in os.listdir(dir):
    path = os.path.join(dir,name)
    if os.path.isfile(path):
      try:
        encryption(path,password)
      except Exception as ex:
        print(ex)
    else:
      search_dir(path,password)

#password is not saving, for safety just remember it
password = input("write a password to encrypt: ")
search_dir(input("directory for encrypt files: (for ex: /home/Desktop/folder/)"), password)