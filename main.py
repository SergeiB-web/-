# Найти сумму и произведение цифр введённого трёхзначного натурального числа.
# Например, если введено число 325,
# то сумма его цифр равна 10 (3+2+5),
# а произведение - 30 (325).

chislo = int(input("Введі треххначное"))
if 100<=chislo<=999:
    sum = int(str(chislo)[0]) + int(str(chislo)[1]) + int(str(chislo)[2])
    proizved = int(str(chislo)[0]) * int(str(chislo)[1]) * int(str(chislo)[2])
    print (sum)
    print(proizved)