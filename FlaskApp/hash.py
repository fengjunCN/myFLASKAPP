from passlib.hash import sha256_crypt


user_entered_password = 'pa$$w0rd'
salt = "5gz"
db_password = user_entered_password+salt
h = hashlib.md5(db_password.encode())
h2 = hashlib.md5(db_password.encode())
print(h.hexdigest())
print(h2.hexdigest())
#print(password)
#print(password2)