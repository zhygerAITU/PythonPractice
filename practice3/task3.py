def check_pass(pswd):
    
    allowed_special_chars = "*-#"

    
    err = {}

    
    if len(pswd) < 8:
        err['length'] = 'Password length should be at least 8 characters.'

    
    if not any(char.isupper() for char in pswd):
        err['uppercase'] = 'Password should contain at least one uppercase letter.'

    if not any(char.islower() for char in pswd):
        err['lowercase'] = 'Password should contain at least one lowercase letter.'

    if not any(char.isdigit() for char in pswd):
        err['number'] = 'Password should contain at least one number.'

    if not any(char in allowed_special_chars for char in pswd):
        err['special_chars'] = f'Password should contain at least one of {allowed_special_chars}.'

    
    if err:
        for key, value in err.items():
            print(value)
    else:
        print("The password is perfect")

check_pass("Abc12345#")  
check_pass("abc12345")   
