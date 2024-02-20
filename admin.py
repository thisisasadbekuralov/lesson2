from classes import Teacher

def teacher_port():
    options = int(input('''
         HUSH KELIBSIZ 
    1.O'zim haqimdagi malumotlar.
    2.O'quvchilarning royhati.
    3.Log in porollarim.  '''))
    if options == 1:
        get_fullinfo()
    elif options == 2:
        with open("data.txt", "r") as file:
            for line in file.readlines():
                data = list(line.split())
                print(data["ism familiya joylashgan indexni qoyish kk"])
    elif options == 4:
        get_password()
    else:
        print("Siz tanlagan tanlov mavjud emas, iltimos qaytadan urunib koring.")

        print('................................................................')
        teacher_port()