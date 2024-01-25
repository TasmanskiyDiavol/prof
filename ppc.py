import csv

mn = set()
with open("students.csv", encoding = "utf8") as file:
    reader = csv.reader(file, delimiter = ",")
    answer = list(reader)
    #print(answer) вывожу список

    for id, name, title, clas, score in answer:
        if "Хадаров Владимир" in name:
            print("Ты получил:", score, "za project -", title)
        if  score == None:
            mn.add(clas)
           """ узнаём пустые классы
            """
