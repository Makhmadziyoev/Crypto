import numpy as np

# геттер для индексов буквы в матричном алфавите
def findinds(matrix, object):
    ara=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == object:
                ara.append(i)
                ara.append(j)
                return ara

def encrypt():
	# разделение текста на биграммы
	bigramms=[]
	c=0
	flag=True
	while(flag==True):
		if(c!=len(orig)-1):
			if(orig[c]!=orig[c+1]):
				bigramm=[]
				bigramm.append(orig[c])
				bigramm.append(orig[c+1])
				bigramms.append(bigramm)
				c+=2
			else:
				bigramm = []
				bigramm.append(orig[c])
				bigramm.append(fixsym)
				bigramms.append(bigramm)
				c+=1
		else:
			bigramm = []
			bigramm.append(orig[c])
			bigramm.append(fixsym)
			bigramms.append(bigramm)
			c+=2
		if (c>len(orig)):
			flag=False
	# запись зашифрованных букв в единую строку
	etext=[]
	for g in bigramms:
		inds1=findinds(malp, g[0])
		inds2=findinds(malp, g[1])
		if inds1[0]==inds2[0]:
			newind11=int(inds1[0])
			newind12=int((inds1[1]+1)%6)
			newind21=int(inds2[0])
			newind22=int((inds2[1]+1)%6)
			etext.append(malp[newind11][newind12])
			etext.append(malp[newind21][newind22])
		elif inds1[1]==inds2[1]:
			newind11=int((inds1[0]+1)%5)
			newind12=int((inds1[1]))
			newind21=int((inds2[0]+1)%5)
			newind22=int((inds2[1]))
			etext.append(malp[newind11][newind12])
			etext.append(malp[newind21][newind22])
		else:
			newind11=int(inds1[0])
			newind12=int(inds2[1])
			newind21=int(inds2[0])
			newind22=int(inds1[1])
			etext.append(malp[newind11][newind12])
			etext.append(malp[newind21][newind22])
	print("\nЗашифрованный текст: ", "".join(etext))
	# print("\nБиграммы:\n")
	# for i in range (0,len(etext),2):
	# 	print(etext[i], end="")
	# 	print(etext[i+1], end="\n")

def decrypt():
	print("\n")
	# разделение текста на биграммы
	bigramms = []
	c = 0
	flag = True
	while (flag == True):
		if (c != len(orig)):
			bigramm = []
			bigramm.append(orig[c])
			bigramm.append(orig[c + 1])
			bigramms.append(bigramm)
			c += 2
		if (c>len(orig)-1):
			flag=False
	dtext=[]
	# запись расшифрованных букв в единую строку
	for g in bigramms:
		inds1=findinds(malp, g[0])
		inds2=findinds(malp, g[1])
		if inds1[0]==inds2[0]:
			newind11=int(inds1[0])
			newind12=int((inds1[1]-1)%6)
			newind21=int(inds2[0])
			newind22=int((inds2[1]-1)%6)
			dtext.append(malp[newind11][newind12])
			dtext.append(malp[newind21][newind22])
		elif inds1[1]==inds2[1]:
			newind11=int((inds1[0]-1)%5)
			newind12=int((inds1[1]))
			newind21=int((inds2[0]-1)%5)
			newind22=int((inds2[1]))
			dtext.append(malp[newind11][newind12])
			dtext.append(malp[newind21][newind22])
		else:
			newind11=int(inds1[0])
			newind12=int(inds2[1])
			newind21=int(inds2[0])
			newind22=int(inds1[1])
			dtext.append(malp[newind11][newind12])
			dtext.append(malp[newind21][newind22])
	print("Расшифрованный текст: ", "".join(dtext))

#свой алфавит из 30 символов
alp = ['а','б','в','г','д','е','ж','з','и','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ь','ы','э','ю','я']
# ф - вставляется между одинаковыми буквами и в конце строки при нечетной длине
fixsym='ф'
# ввод и проверка лозунга
ll=input("\nВведите лозунг: ")
if(len(ll)>1):
	for i in range(0,len(ll)-1):
		for k in range (i+1,len(ll)):
			if ll[i] in alp and ll[k] in alp:
				if ll[i]==ll[k]:
					print("Ошибка. Попробуйте другой лозунг. \n")
					exit()
			else:
				print("Ошибка. Попробуйте другой лозунг. \n")
				exit()
elif(ll not in alp or ll==''):
	print("Ошибка. Попробуйте другой лозунг. \n")
	exit()
# создание копии алфавита без букв лозунга
calp=alp
for u in ll:
	for t in calp:
		if t==u:
			calp.remove(t)
# преобразование исходного алфавита в матрицу в соответствии с лозунгом
malp=[]
p=0
r=0
for i in range(0,5):
	a=[]
	for g in range(0,6):
		if p<len(ll):
			a.append(ll[p])
			p+=1
		else:
			a.append(calp[r])
			r+=1
		if(g==5):
			malp.append(a)

print("\nПолученный алфавит:\n")
for j in malp:
	print(" ".join(j))

orig = input("\nВведите фразу: ")
# выбор пути
ask=input("\nЗашифровать? (д/н): ")
if ask=='д':
	encrypt()
elif ask=='н':
	if(len(orig)%2!=0):
		print("Ошибка. Повторите с чётной длиной зашифрованного текста.")
		exit()
	else:
		decrypt()
else:
	print('\nОшибка. Повторите с требуемым ответом.\n')
	exit()