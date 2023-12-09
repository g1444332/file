name = input("Введіть ім'я файлу: ")
isName = False
while not isName:
    try:
        with open(name, 'r', encoding='utf-8') as f:
            data = f.read()
            isName = True
    except:
        print("Такого файлу не існує! Повторіть ведення.")
        name = input("Введіть ім'я файлу: ")


    
print(data)

a = input("\nХто написав ці рядкі?")

with open(name, 'a', encoding='utf-8') as f:
    data = f.write("\n\n" + "("+ a + ")")

a1 = input("\nХочете добавити цитату? (так/ні) ")
while a1 == 'так':
    a2 = input("\nВвведіть цитату: ")
    author = input("Ввведіть автора:")
    a1 = input("\nХочете добавити цитату? (так/ні) ")
    with open(name, 'a', encoding='utf-8') as f:
        data = f.write("\n\n" + a2)
        data = f.write("\n" + "("+ author + ")")


with open(name, 'r', encoding='utf-8') as f:
    print(f.read())
    # lines = f.readlines()
    # authors = []
    # for l in lines:
    #     if l.startswith('('):
    #         l = l.replace("\n", "")
    #         authors.append(l)
    # for a in authors:
    #     print(a)



