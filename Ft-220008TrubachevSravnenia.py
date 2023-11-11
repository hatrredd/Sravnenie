kf = []; kfR = []
count = int(input("Введите количество критериев для сравнения: "))
while count < 1:
    count = int(input("Вы ввели некорректное количество критериев, попробуйте ещё раз: "))
for i in range(count):
    for k in range(count-1):
        if i <= k:
            print("Насколько критерий", i+1, "приоритетнее критерия", k+2)
            ratio = int(input("Введите коэффициент: "))
            while ratio < 1:
                ratio = int(input("Вы ввели некорректный коэффициент, попробуйте ещё раз: "))
            kf.append(int(ratio))
for j in range(len(kf)):
    ratioR = round(1/(kf[j]), 2)
    kfR.append(ratioR)
summ = round(sum(kf) + count + sum(kfR),2)
for q in range(count):
    result = [1]; u = 0
    while len(result) != count:
        if u < len(kf):
            result.append(kf[0])
            kf.pop(0)
            u += 1
        else:
            u = 0
            result.append(kfR[0])
            kfR.pop(0)
            u += 1
    print("Коэффициент критерия", q+1 , "-", round(sum(result)/summ, 2))