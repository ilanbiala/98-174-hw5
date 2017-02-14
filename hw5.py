import hashlib

userid = input("Please provide your Andrew ID: ")
hash_object = hashlib.md5(userid.encode())
userf = open(userid + ".txt", "w+")
userf.write(hash_object.hexdigest())
userf.close()
