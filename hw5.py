import hashlib

try:
  input = raw_input
except NameError:
  pass

userid = input("Please provide your Andrew ID: ")
hash_object = hashlib.md5(userid.encode())
userf = open(userid + ".txt", "w+")
userf.write(hash_object.hexdigest())
userf.close()
