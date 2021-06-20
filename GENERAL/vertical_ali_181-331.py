# makhmadziyoev ali 181-331
import numpy as np
from collections import Counter as counter

def generate_jail(n):
	ma=0
	mb=0
	while ma*mb<n:
		if ma>=mb:
			mb+=1
		else:
			ma+=1
	if ma==0 or mb==0:
		print("Ошибка. Текст не введён.")
		exit()
	return (ma,mb)

def encrypt():
	matrix=np.zeros((ma,mb), dtype=str)
	e=0
	for y in range(ma):
		for x in range(mb):
			matrix[y][x]=orig[e]
			e+=1
			if e==len(orig):
				break
	enc=[]
	if ost==0:
		for g in num:
			for f in range(ma):
				enc.append(matrix[f][g])
	else:
		for g in num:
			if g<ost:
				for f in range(ma):
					enc.append(matrix[f][g])
			else:
				for f in range(ma-1):
					enc.append(matrix[f][g])
	print("Зашифрованный текст: ")
	print("".join(enc))


def decrypt():
	temptrash=np.zeros((ma,mb), dtype=str)
	a=0
	if ost==0:
		for x in range(len(num)):
			for y in range(ma):
				temptrash[y][x]=orig[a]
				a+=1
	else:
		for x in range(len(num)):
			if (num[x]<ost):
				for y in range(ma):
					temptrash[y][num[x]]=orig[a]
					a+=1
			else:
				for y in range(ma-1):
					temptrash[y][num[x]]=orig[a]
					a+=1
	dec=[]
	for t in temptrash:
		for u in t:
			if u!=0:
				dec.append(u)
	print("Расшифрованный текст: ")
	print("".join(dec))
	

# свой алфавит из 32 символов
alp = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
# ввод текста и ключа, а также их проверка
orig=input("\nВведите фразу: ")
# генерация размерности матрицы для фразы 
(ma,mb)=generate_jail(len(orig))
print("Размер матрицы: ",ma,"x",mb)
# вывод фразы в виде матрицы
q=0
for i in range(ma):
	for j in range(mb):
		if j==mb-1:
			print(orig[i*mb+j], end="\n")
			q+=1
		else:
			print(orig[i*mb+j], end=" ")
			q+=1
		if i*mb+j==len(orig)-1:
			break
	if q==len(orig):
		break
print("\nПредупреждение:")
print("Длина ключа в (количество букв в слове или количество чисел) должна быть: ", mb)
key=input("Введите ключ (cлово или числа через пробел): ")
# проверка текста и ключа на "аномалии"
# подразумевается возможность использовать числовой и буквенный ключи 
temp=[]
keykey=[]
if key[0].isdigit():
	temp=key.split()
	for k in temp:
		if k.isdigit():	
			keykey.append(int(k))
		else:
			print("Ошибка. В числовом ключе присутствуют не только числа.")
			exit()
	if len(keykey)!=mb:
		print("Ошибка. Длина ключа не соответствует количеству строк матрицы.")
		exit()
elif len(key)!=mb:
	print("Ошибка. Длина ключа не соответствует количеству строк матрицы.")
	exit()
if(len(keykey)==0):
	check1=0
	for j in orig:
		if j in alp:
			check1+=1
	check2=0
	for j in key:
		if j in alp:
			check2+=1
	if check1>0 and check1<len(orig):
		print("Ошибка. Не все символы текста есть в алфавите.")
		exit()
	elif check2>0 and check2<len(key):
		print("Ошибка. Не все символы ключа есть в алфавите.")
		exit()
	u=0
	ckey=key
	ckey=sorted(ckey)
	trash=[]
	num=[]
	for t in range (len(key)):
		ind=ckey.index(key[t])
		if ind in trash:
			while ind in trash:
				ind+=1
			trash.append(ind)
			num.append(ind)
		else:
			trash.append(ind)
			num.append(ind)
	print(num,"\n")
	
elif len(keykey)>0:
	keykeycount=counter(keykey)
	arrch=[]
	checker=[]
	for i in range(1,mb+1):
		arrch.append(i)
		checker.append(0)
	for k in keykeycount:
		if k<=mb and keykeycount[k]==1:
			for x in range(len(arrch)):
				if k==arrch[x]:
					checker[x-1]+=1
		elif (k>mb):
			print("Ошибка. В числовом ключе есть число больше числа столбцов матрицы.")
			exit()
		elif (keykeycount[k]>1):
			print("Ошибка. В числовом ключе есть повторяющиеся числа.")
			exit()
	if (checker!=[1 for i in range(mb)]):
		print("Ошибка. В числовом ключе должны быть все числа от 1 до", mb, ".c")
		exit()
	num=[i-1 for i in keykey]
	print(num,"\n")

ost=len(orig)%(mb*(ma-1))
ask=input("\nЗашифровать? (д/н): ")
if ask=='д':
	print("\n")
	encrypt()
elif ask=='н':
	print("\n")
	decrypt()
else:
	print('\nОшибка. Повторите с требуемым ответом.\n')
	exit()
