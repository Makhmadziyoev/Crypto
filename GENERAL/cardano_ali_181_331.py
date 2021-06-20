import numpy as np
import os
import os.path as osp

def next_xy(jail,y,x):
	(q,e)=np.shape(jail)
	j=y
	for i in range(x,e):
		if(jail[j][i]==0):
			return (j,i)
	for b in range(y+1,q):
		for i in range(e):
			if(jail[b][i]==0):
				return (b,i)
	# print("Логическая ошибка.")
	# exit()

def measure(file,n2,m2):
	rowc=0
	colc=0
	for line in file:
		if rowc>=m2:
			print("Ошибка. Слишком большой трафарет.")
			exit()
		cline = line.split()
		for k in cline:
			if colc>=n2:
				print("Ошибка. Слишком большой трафарет.")
				exit()
			colc+=1
		if colc<n2:
			print("Ошибка. Слишком маленький трафарет.")
			exit()
		colc=0
		rowc+=1
	if rowc<m2:
			print("Ошибка. Слишком маленький трафарет.")
			exit()

def rotate(jail, d):
	(q,e)=np.shape(jail)
	if d==0:
		return jail
	elif d==3: # зеркало относительно вертикальной оси
		return np.fliplr(jail)
	elif d==2: # зеркало относительно горизонтальной оси
		return np.flipud(jail)
	elif d==1: # зеркало относительно центра
		return np.flipud(np.fliplr(jail))

def encrypt():
	indarray=[]
	for k in orig:
		if k in alp:
			indarray.append(alp.index(k))
	windarr=np.array(indarray).reshape(4,m*n)
	enc=np.full((m2,n2),0)
	for j in range(4):
		x=0
		y=0
		xjail=rotate(jail,j)
		for i in range(m*n):
			c=windarr[j][i]
			(y,x)=next_xy(xjail,y,x)
			# print(y,x)
			enc[y][x]=c
			x+=1
		# y+=1
	# print("\n",enc)
	# exit()
	enct=[]
	for p in enc:
		for f in p:
			enct.append(alp[f])
	print("\nЗашифрованный текст: ","".join(enct))


def decrypt():
	indarray=[]
	for k in orig:
		if k in alp:
			indarray.append(alp.index(k))
	windarr=np.array(indarray).reshape(m2,n2)
	indarray2=[]
	for j in range(4):
		x=0
		y=0
		xjail=rotate(jail,j)
		for i in range(m*n):
			(y,x)=next_xy(xjail,y,x)
			# print(y,x)
			c=windarr[y][x]
			indarray2.append(c)
			x+=1
		# y+=1
	dec=[]
	for t in indarray2:
		dec.append(alp[t])
	print("\nРасшифрованный текст: ","".join(dec))

# свой алфавит из 32 символов

alp = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
print("\nВыберите размерность решетки.")
m2=int(input("Введите число строк в решетке (2m): "))
if m2%2!=0:
	print("Ошибка. 2m должно быть четным.")
	exit()
n2=int(input("Введите число столбцов в решетке (2n): "))
if n2%2!=0:
	print("Ошибка. 2n должно быть четным.")
	exit()
m=int(m2/2)
n=int(n2/2)

orig=input("Введите фразу: ")
print("\nДлина текста: ",len(orig),"\n")
if (len(orig)<m2*n2):
	print("Ошибка: нельзя оставлять пустые места.")
elif (len(orig)>m2*n2):
	print("Ошибка. Слишком длинный текст для выбранной решетки.")

print("Сгенерируйте файл с трафаретом")
print("traf.txt \n")
path="traf.txt"
if not osp.exists(path):
	print('\nОшибка. Нет файла с трафаретом.\n')
	exit()
elif osp.getsize(path)==0:
	print('\nОшибка. Файл с трафаретом пуст.\n')
	exit()
jail=np.full((m2,n2),-1)
file=open("traf.txt", "r")
measure(file,n2,m2)

rowc=0
colc=0

with open("traf.txt", "r") as f:
    for line in f.readlines():
        cline=line.split()
        for k in cline:
        	jail[rowc][colc]=int(k)
        	colc+=1
        rowc+=1
        colc=0

# print(jail)

file.close()

zeros=0
for j in range(len(jail)):
	for i in range(len(jail[j])):
		if jail[j][i]==0:
			zeros+=1
			if jail[m2-1-j][i]!=1 or jail[j][n2-1-i]!=1 or jail[m2-1-j][n2-1-i]!=1:
				print("Ошибка. В трафарете есть совпадающие отверстия")
				exit()
		elif jail[j][i]<0:
			print("Ошибка. Трафарет должен состоять из чисел 0 и 1.")
			exit()
		elif jail[j][i]>1:
			print("Ошибка. Трафарет должен состоять из чисел 0 и 1.")
			exit()
if zeros==0:
	print("Ошибка. В трафарете нет отверстий.")
	exit()

print("\nТрафарет (0 - отверстие): ")
for i in range(len(jail)):
	for j in range(len(jail[i])):
		if (j==len(jail[i])-1):
			print(jail[i][j], end="\n")
		else:
			print(jail[i][j], end=" ")

# print(jail)
# exit()
ask=input("\nЗашифровать? (д/н): ")
if ask=='д':
	encrypt()
elif ask=='н':
	decrypt()
else:
	print('\nОшибка. Повторите с требуемым ответом.\n')
	exit()

