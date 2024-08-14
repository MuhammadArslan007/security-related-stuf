import hashlib

user_input = input("Please Enter Your Password: ")



def gen_h(input_str: str, salt:str = "44") -> str:
   
    hash_obj = hashlib.sha256()
    hash_obj.update(input_str.encode())
    passwd = hash_obj.hexdigest() 
    salt_pass:str  = passwd + str(salt)
    hash_obj.update(salt_pass.encode())
    passwd_db = hash_obj.hexdigest() 
    return passwd_db

enter_passwd = gen_h(user_input)


# verify user 
passwd_db = '123ja'

if enter_passwd == gen_h(passwd_db):
    print("You Are LogedIn Seccessfully! ")
else:
    print("Opps! Wrong password.")
