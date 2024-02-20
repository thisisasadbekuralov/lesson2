

import classes
from admin import teacher_port
from user import user_port

def main():
    username = input("username: ")
    password = input("password: ")

    with open("data.txt", "r") as file:
        for line in file.readlines():
            data = list(line.split())
            if data[0] == username and data[1] == password and data[2] == 1:
                teacher_port()
            elif data[0] == username and data[1] == password and data[2] == 0:
                user_port()
            else:
                print("siz password yoki usenameni xato kiritdingiz")
                print("_______________________________________________\n")
                main()


if __name__ == "__main__":
    main()


