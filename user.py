from classes import Student

def user_port():
    options = int(input('''
         HUSH KELIBISIZ
    1.O'zim haqimdagi malumotlar.
    2.Mening kurslarim.
    3.Yangi kursga yozilish.
    4.To'lovlarim.
    5.Guruhlarim.
    6.Sozlamalar.  '''))

    if options == 1:
        get_fullinfo()
    elif options == 2:
        get_courses()
    elif options == 3:
        str(input('''
        Iltimos yozilmoqchi bolgan kursingiz nomini va tel raqamingizni qoldiring.
        Operatorimiz siz bilan bog'lanadi  
        '''))
    elif options == 4:
        if get_payment() is True:
            print("Sizning tolovingiz vaqtida amalga oshirilgan")
        else:
            print("Sizning tolovingiz bilan muamo bor. "
                  "Iltimos administratsiyaga murojat qiling")
    elif options == 5:
        get_group_info()
    elif options == 6:
        print('''
        Kechirasiz bazi texnik sabablarga kora ushbu sorovni amalga oshirishning iloji yoq.
        Noqulayliklar uchun uzur soraymiz
        SORRY
        ''')
    else:
        print("Siz tanlagan tanlov mavjud emas, iltimos qaytadan urunib koring.")

        print('................................................................')
        user_port()