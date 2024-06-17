import hashlib

userhash_dictionary = {}
with open('password.txt','r') as f :
    #common_passwords.append(f.read().splitlines())
    common_passwords = f.read().splitlines()
#print(common_passwords)

with open('username.txt' , 'r') as f:
    text = f.read().splitlines()
    for user_hash in text:
        username = user_hash.split(":")[0]
        #print(username)
        hash = user_hash.split(":")[1]
        userhash_dictionary[username] = hash
#for user , hash in userhash_dictionary.items():
 #   print(user, hash)

for password in common_passwords:
    hashed_passwords = hashlib.sha256(password.encode('utf-8')).hexdigest()
    for username ,hash in userhash_dictionary.items():
         if hashed_passwords == hash:
             print(f"HASH FOUND ! \n  {username}: {password}" )