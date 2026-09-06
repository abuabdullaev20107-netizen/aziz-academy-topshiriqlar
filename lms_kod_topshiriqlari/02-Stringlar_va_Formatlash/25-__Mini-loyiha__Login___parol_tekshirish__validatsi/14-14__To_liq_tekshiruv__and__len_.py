# Kodingizni shu yerga yozing
login = input()
parol = input()
kirish = login == "admin" and len(parol) >= 4
print(kirish)