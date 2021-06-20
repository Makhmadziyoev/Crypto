import numpy as np
def ct(d, value, defval):
    if value in d:
    	return d[value]
    return defval
def invers(d):
	h={}
	for k,v in d.items():
		h[v]=k
	return h
# перевод текста в хекс-строку
def hexp(text):
	return "".join(['{0:02x}'.format(ct(alf,k,0xFF)) for k in text])
# перевод хекс-строки в текст
def hexc(hext):
	temx=[hext[i:i+2] for i in range(0, len(hext), 2)]
	return "".join([ct(ialf,int(i,16),"D") for i in temx])
# операция прибавления константы С1 по модулю 2**32
def c1(x):
	t=x+0x01010101
	if t<2**32:
		return t
	else:
		return t-2**32
# операция прибавления константы С2 по модулю 2**32
def c2(x):
	t=x+0x01010104
	if t<2**32:
		return t
	else:
		return (t-2**32)+1

s=[
["C","4","6","2","A","5","B","9","E","8","D","7","0","3","F","1"],
["6","8","2","3","9","A","5","C","1","E","4","7","B","D","0","F"],
["B","3","5","8","2","F","A","D","E","1","7","4","C","9","6","0"],
["C","8","2","1","D","4","F","6","7","0","A","5","3","E","9","B"],
["7","F","5","A","8","1","6","D","0","9","3","E","B","4","2","C"],
["5","D","F","6","9","2","C","A","B","7","8","1","4","3","E","0"],
["8","E","2","5","6","9","1","C","F","4","B","0","D","A","3","7"],
["1","7","E","D","0","5","8","3","4","F","A","6","9","C","B","2"]
]
# алгоритм сдвига
def fx(a,x):
	k=(a+x)%(2 ** 32)
	xx='{0:08x}'.format(k)
	tomb=[]
	for i,c0 in enumerate(xx[::-1]):
		c1=s[i][int(c0,16)]
		tomb.append(c1)
	b32='{0:032b}'.format(int("".join(tomb[::-1]),16))
	b32_rot=b32[11:32]+b32[0:11]
	i32=int(b32_rot,2)
	return i32
# вспомогательная функция для сдвига
def step(a0,b0,x):
	a1=b0
	b1=a0^fx(b0,x)
	return (a1,b1)

# алгоритм обработки хекс-строк на сдвиг
def g_mix(text, secret):
	if type(text)!=str:
		print("Текст должен быть строкой.")
		exit()
	if type(secret)!=str:
		print("Ключ должен быть строкой.")
		exit()
	if len(text)!=16:
		print("Длина текста должна быть 64 бита.")
		exit()
	if len(secret)!=64:
		print("Длина ключа должна быть 256 бит.")
		exit()
	(ax, bx) = [text[i:i+8] for i in range(0, len(text), 8)]
	a=int(ax, 16)
	b=int(bx, 16)

	kx=[secret[i:i+8] for i in range(0, len(secret), 8)]
	k=[int(p, 16) for p in kx]
	x=[]
	for i in range(3):
		for j in range(len(k)):
			x.append(k[j])
	for j in range(len(k)):
		x.append(k[len(k)-j-1])
	ai=a
	bi=b
	for i in range(32):
		(ai,bi)=step(ai,bi,x[i])
	return '{0:08x}'.format(bi)+'{0:08x}'.format(ai)

def g_gamma(iv, secret, steps):
	if type(iv)!=str:
		print("IV должен быть строкой.")
		exit()
	if type(secret)!=str:
		print("Ключ должен быть строкой.")
		exit()
	if len(iv)!=16:
		print("Длина IV должна быть 64 бита.")
		exit()
	if len(secret)!=64:
		print("Длина ключа должна быть 256 бит.")
		exit()

	(n4x,n3x) = [iv[i:i+8] for i in range(0, len(iv), 8)]
	n3=0
	n4=int(n4x, 16)
	gamma=[]
	ivn='{0:08x}'.format(n4)+'{0:08x}'.format(n3)
	gamma.append(g_mix(ivn,secret))
	for i in range(steps-1):
		n3=(n3+1)%(2**32)
		ivn='{0:08x}'.format(n4)+'{0:08x}'.format(n3)
		gamma.append(g_mix(ivn,secret))
	return gamma
# алгоритм наложения гаммы
def g_ctr(gamma, blocks):
	ctr=[]
	if len(gamma)!=len(blocks):
		print("Ошибка! Разные количества блоков текста и гаммы.")
		exit()
	for i, g in enumerate(gamma):
		b=blocks[i]
		ctr.append('{0:016x}'.format(int(g,16)^int(b,16)))
	return ctr

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

# свой алфавит из 32 символов
alf = {'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ж': 7, 'з': 8, 'и': 9, 'й': 10, 'к': 11, 'л': 12, 'м': 13, 'н': 14, 'о': 15, 'п': 16, 'р': 17, 'с': 18, 'т': 19, 'у': 20, 'ф': 21, 'х': 22, 'ц': 23, 'ч': 24, 'ш': 25, 'щ': 26, 'ъ': 27, 'ы': 28, 'ь': 29, 'э': 30, 'ю': 31, 'я': 32}
ialf=invers(alf)


ask=input("Выбирете шифрование(Ш) или расшифрование(Р)")
if ask=='Ш':
	orig=input("Введите исходное сообщение: ")
	keykey=input("Введите ключ: ")
	iv=input("Введите IV: ")
	if len(iv)!=8:
		print("Ошибка. Для данного стандарта используются 8 хекс-символов")
		exit()
	iv+="00000000"
	orighex=hexp(orig)
	keyhex=hexp(keykey)
	(arrayhex,l)=padding(orighex)
	g=g_gamma(iv,keyhex,len(arrayhex))
	gctr=g_ctr(g,arrayhex)
	print("Зашифрованное сообщение: ", "".join(gctr))

elif ask=='Р':
	orig=input("Введите зашифрованное сообщение: ")
	keykey=input("Введите ключ: ")
	iv=input("Введите IV: ")
	if len(iv)!=8:
		print("Ошибка.")
		exit()
	iv+="00000000"
	keyhex=hexp(keykey)
	(arrayhex,l)=padding(orig)
	g=g_gamma(iv,keyhex,len(arrayhex))
	gctr=g_ctr(g,arrayhex)
	dectext=hexc("".join(gctr))
	print("Расшифрованное сообщение: ", dectext)

else:
	print('Ошибка.')
	exit()
