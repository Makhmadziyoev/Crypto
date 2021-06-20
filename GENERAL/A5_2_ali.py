import numpy as np

def creamthepie(d, value, defval):
    if value in d:
    	return d[value]
    return defval

def lickthecream(d):
	h={}
	for k,v in d.items():
		h[v]=k
	return h
# перевод текста в хекс-строку
def hexpie(text):
	return "".join(['{0:02x}'.format(creamthepie(dic,k,0xFF)) for k in text])
# перевод хекс-строки в текст
def hexcream(hext):
	temx=[hext[i:i+2] for i in range(0, len(hext), 2)]
	return "".join([creamthepie(idic,int(i,16),"D") for i in temx])

def load(iv,secret):
	r1=np.zeros(19, np.int32)
	r2=np.zeros(22, np.int32)
	r3=np.zeros(23, np.int32)
	r4=np.zeros(17, np.int32)
	for x in [*secret,*iv]:
		r1[0]=r1[0]^x
		r2[0]=r2[0]^x
		r3[0]=r3[0]^x
		r4[0]=r4[0]^x
		r1=np.roll(r1,1)
		r2=np.roll(r2,1)
		r3=np.roll(r3,1)
		r4=np.roll(r4,1)
	r4[3]=1
	r4[7]=1
	r4[10]=1
	for x in range(99):
		majority = get_majority(r4[3], r4[7], r4[10])
		if r4[10] == majority:
			x_bit = r1[18] ^ r1[17] ^ r1[16] ^ r1[13]
			temp1 = np.roll(r1, 1)
			temp1[0]=x_bit
			r1=temp1
		if r4[3] == majority:
			x_bit = r2[20] ^ r2[21]
			temp2 = np.roll(r2, 1)
			temp2[0]=x_bit
			r2=temp2
		if r4[7] == majority:
			x_bit = r3[20] ^ r3[21] ^ r3[22]
			temp3 = np.roll(r3, 1)
			temp3[0]=x_bit
			r3=temp3
		x_bit=r4[16]^r4[11]
		temp4=np.roll(r4,1)
		temp4[0]=x_bit
		r4=temp4
	return(r1,r2,r3,r4)


def a_gamma(iv,secret,steps):
	if len(iv)!=22:
		print("Ошибка. Длина iv должна быть 22 бита.")
		exit()
	if len(secret)!=64:
		print("Ошибка. Длина ключа должна быть 64 бит.")
		exit()
	(r1,r2,r3,r4)=load(iv,secret)
    # print("r2: ", r2)
    # print("r3: ", r3)
	gamma=[]
	for x in range(steps):
		majority = get_majority(r4[3], r4[7], r4[10])
		if r4[10] == majority:
			x_bit = r1[18] ^ r1[17] ^ r1[16] ^ r1[13]
			temp1 = np.roll(r1, 1)
			temp1[0]=x_bit
			r1=temp1
		if r4[3] == majority:
			x_bit = r2[20] ^ r2[21]
			temp2 = np.roll(r2, 1)
			temp2[0]=x_bit
			r2=temp2
		if r4[7] == majority:
			x_bit = r3[20] ^ r3[21] ^ r3[22]
			temp3 = np.roll(r3, 1)
			temp3[0]=x_bit
			r3=temp3
		x_bit=r4[16]^r4[11]
		temp4=np.roll(r4,1)
		temp4[0]=x_bit
		r4=temp4
		x1=r1[18]^get_majority(r1[12],r1[14],r1[15])
		x2=r2[21]^get_majority(r2[9],r2[13],r2[16])
		x3=r3[22]^get_majority(r3[13],r3[16],r3[18])
		output = x1 ^ x2 ^ x3
		gamma.append(output)
	# print(gamma)
	kg="".join(['{0:d}'.format(i) for i in gamma])
	kx=[kg[i:i+64] for i in range(0, len(kg), 64)]
	pio=['{0:016x}'.format(int(i,2)) for i in kx]
	# print(pio)
	return pio

def get_majority(a,b,c):
    if a + b + c > 1:
        return 1
    else:
        return 0

def binpie(hext):
	return [int(i,2) for i in '{0:064b}'.format(int(hext,16))]

def ivpie(frame):
	x=(frame % (0x400000))
	return [int(i,2) for i in '{0:022b}'.format(x)]

# вспомогательная функция
# для дополнения текста, не кратного 64 битам
def xrand(n):
	x=""
	if n%2!=0:
		n-=1
		x+="0"
	for i in range(int(n/2)):
		x+='{0:02x}'.format(np.random.randint(1,33))
	return x
# алгоритм разбиения хекс-строки текста на блоки
def padding(hext):
	l=len(hext)
	freak=l%16
	if freak>0:
		hext+=xrand(16-freak)
	return ([hext[i:i+16] for i in range(0, len(hext), 16)],l)

def g_ctr(gamma, blocks):
	ctr=[]
	if len(gamma)!=len(blocks):
		print("Ошибка! Разные количества блоков текста и гаммы.")
		exit()
	for i, g in enumerate(gamma):
		b=blocks[i]
		ctr.append('{0:016x}'.format(int(g,16)^int(b,16)))
	return ctr

# свой алфавит из 32 символов
dic = {'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ж': 7, 'з': 8, 'и': 9, 'й': 10, 'к': 11, 'л': 12, 'м': 13, 'н': 14, 'о': 15, 'п': 16, 'р': 17, 'с': 18, 'т': 19, 'у': 20, 'ф': 21, 'х': 22, 'ц': 23, 'ч': 24, 'ш': 25, 'щ': 26, 'ъ': 27, 'ы': 28, 'ь': 29, 'э': 30, 'ю': 31, 'я': 32}
idic=lickthecream(dic)

ask=input(" (Ш/Р): ")
if ask=='Ш':
	orig=input("Введите исходное сообщение: ")
	keykey=input("Введите ключ: ")
	iv=int(input("Введите IV: "))
	orighex=hexpie(orig)
	keyhex=hexpie(keykey)
	keybin=binpie(keyhex)
	ivpie=ivpie(iv)
	(arrayhex,l)=padding(orighex)
	g=a_gamma(ivpie,keybin,len(arrayhex)*64)
	gctr=g_ctr(g,arrayhex)
	print("Зашифрованный текст: ", "".join(gctr))

elif ask=='Р':
	orig=input("Введите зашифрованное сообщение: ")
	keykey=input("Введите ключ: ")
	iv=int(input("Введите IV: "))
	keyhex=hexpie(keykey)
	keybin=binpie(keyhex)
	ivpie=ivpie(iv)
	(arrayhex,l)=padding(orig)
	g=a_gamma(ivpie,keybin,len(arrayhex)*64)
	gctr=g_ctr(g,arrayhex)
	cream=hexcream("".join(gctr))
	print("Расшифрованный текст: ", cream)

else:
	print('\nОшибка. Повторите с требуемым ответом.\n')
	exit()