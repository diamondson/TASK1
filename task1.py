text = input("Введите имя и фамилию через пробел: ")
full_name = text.split()
name = str(full_name[0])
surname = str(full_name[1])

name = input("Введите ваше имя: ")
surname = input("Введите фамилию: ")

print("Добрый день " + name[0].capitalize() + "."+ surname.capitalize())

