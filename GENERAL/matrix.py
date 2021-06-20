import numpy as np

def encrypt():
    mencrypt=np.array([])
    im=np.array(index_matrix)
    # print(arrr)
    # умножение ключевой матрицы на вектор в цикле
    for k in im:
        enc=arrr.dot(k)
        # print("\n",enc,"\n")
        mencrypt=np.append(mencrypt, enc)
    pa=[]
    # print("\n", mencrypt)
    # переход к единому вектору чисел
    for x in mencrypt:
        pa.append(int(x))
    print("Зашифрованный текст:\n")
    for x in pa:
        print(x, end=' ')
    print("\n")

def decrypt():
    temp_num=[]
    # обратная матрица
    inv_arr=np.linalg.inv(arrr)
    # умножение обратной матрицы на векторы в цикле
    for k in num_vectors:
        dec=inv_arr.dot(k)
        for x in dec:
            temp_num.append(int(round(x)))
    decrypt=[]
    # переход к единой строке
    for a in temp_num:
        decrypt.append(alp[a-1])
    print("Расшифрованный текст: ", "".join(decrypt), "\n")

# свой алфавит из 32 символов
alp = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
# ввод ключевых параметров
bs=int(input("\nВведите размер блока: "))
ma=int(input("Введите количество строк ключевой матрицы: "))
if bs!=ma:
    print("Защита. Во избежание ошибок в алгоритме введите равные параметры.")
    exit()
mb=ma
# ввод ключевой матрицы
for row in range(0,ma):
    if row==0:
        arr=[]
    for column in range(0,mb):
        if column==0:
            ar=[]
            o=int(input("Введите А[{0}][{1}]: ".format(row+1,column+1)))
            ar.append(o)
        elif column==mb-1:
            o=int(input("Введите А[{0}][{1}]: ".format(row+1,column+1)))
            ar.append(o)
            arr.append(ar)
        else:
            o=int(input("Введите А[{0}][{1}]: ".format(row+1,column+1)))
            ar.append(o)
arrr=np.array(arr)
# проверка обратимости
if np.linalg.det(arrr) == 0:
    print("Ошибка. Матрица необратима.")
    exit()
# выбор пути зашифровки или расшифровки
ask=input("\nЗашифровать? (д/н): ")
if ask=='д':
    orig = input("Введите фразу: ")
    if len(orig)%bs != 0:
        print("Защита. Во избежание ошибок в алгоритме введите другой размер блока.")
        exit()
    index_array = []
    # запись единого вектора с порядками букв 
    for i in orig:
        if i in alp:
            ind = alp.index(i) + 1
            index_array.append(ind)
    index_matrix = []
    k = -1
    # разделение на векторы по размеру блока
    for x in range(0, len(orig), bs):
        if x % bs == 0:
            a = []
            k += 1
            for y in range(0, bs):
                if y == bs - 1:
                    a.append(index_array[k * bs + y])
                    index_matrix.append(a)
                else:
                    a.append(index_array[k * bs + y])
    encrypt()
elif ask=='н':
    orig = input("Введите числа через пробел: ")
    print("\n")
    # запись целочисленных значений из полученной строки
    temp_array = orig.split()
    num_array=[]
    for n in temp_array:
        num_array.append(int(n))
    # разделение единого вектора по размеру блока
    num_vectors=[]
    k = -1
    for x in range(0, len(num_array), bs):
        if x % bs == 0:
            a = []
            k += 1
            for y in range(0, bs):
                if y == bs - 1:
                    a.append(num_array[k * bs + y])
                    num_vectors.append(a)
                else:
                    a.append(num_array[k * bs + y])
    decrypt()
else:
    print('\nОшибка. Повторите с требуемым ответом.\n')
    exit()