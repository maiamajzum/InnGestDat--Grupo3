from captcha import captcha
def main():
    
    status = captcha()

    if(status == 1):
        print("Ingresó al Sistema.")
    else:
        print("Acceso DENEGADO!")

if __name__ == "__main__":
    main()
