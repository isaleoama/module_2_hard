a = 'Ответы: '
def out_red(text):
    print("\033[36m{}".format(text))
out_red("------------- "
        "Слишком древний шифр"
        "--------------")
def count_pas(n):
    password = list()
    for i in range(1,n):
        for j in range(i+1,n):
            if n % (i + j) == 0:
                an = str(i) + str(j)
                password.append(an)
    return password

n = int(input('Число на первом камне? :'))
while (n < 3 or n > 20):
    n = int(input('Не верное число, введи верное: '))

result = str()
results = count_pas(n)
for i in range(len(results)):
    result += results[i]
print('Вводим на втором камне:', result)