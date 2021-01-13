def myemail_info (email):
    if "@" in email:
        x = email.split("@")    # x=tuple(email.split("@")
        return x[0], x[1]    # return x
    else :
        return None

print(myemail_info("email"))
print(myemail_info("xxxxx@gmail.com"))