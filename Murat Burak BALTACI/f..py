'''
# Basit fonksiyon
def selamla() :
    print("selam")
    print("merhaba")
selamla()
#selamla()
#selamla()
'''
'''
def topla():
    s1 = int(input("1.Sayıyı gir:"))
    s2 = int(input("2.sayıyı gir:"))
    toplam = s1 + s2
    print(f"{s1} ve {s2} toplamı: {toplam}")
topla()
'''
'''
# parametre alan fonksiyon
def topla(a,b):
    toplam = a + b # a ve b fonksiyon parametreleri
    print(f"{a} ve {b} toplamı: {toplam}")
    s1 = int(input("1.Sayıyı gir:"))
    s2 = int(input("2.sayıyı gir:"))
    topla(s1,s2)
    topla(7,2)
    topla(7,21)
'''
'''
# parametre default değeri
def topla(a = 0,b = 10): # a ve  b değerleri fonksiyon çağırımıda bir şey girilmez ise ne olacağı...
    toplam = a + b
    print(f"{a} ve {b} toplamı: {toplam}")
    topla(7,2)
    topla(7,21)
    topla(7)
    topla()
'''
'''
# isimli parametre çağırımı
def topla(a=0,b=10): # a ve b değerleri fonksyon çağırımında bir şey girilmez ise ne olacağı...
  toplam = a + b
  print(f"{a} ve {b} toplamı: {toplam}")
topla(7)
topla(b=7) # parametreleri isimle çağırabiliriz.
'''
'''
# değer döndüren fonksiyonlar. return
def topla(s1=0, s2=0):
    #return "toplam"
    return "Ankara" # ilk return sonrası çalışmaz
    return s1*s2
    #return s1+s2
#topla(5,6)
print(topla(8,2))
c = topla(6,9)
print(c)
'''
def menuOlustur(elemanlar):
  enUzun = 0
  for a in elemanlar:
    print(a, len(a))
    if len(a)>enUzun: enUzun=len(a)

  print("╔","═"*(enUzun+4),"╗",sep="")
  for eleman in elemanlar:
    print("║"," "*((enUzun-len(eleman))//2),eleman," "*((enUzun-len(eleman))//2),"║")
  print("╚","═"*(enUzun+4),"╝",sep="")

menuOlustur(["Stok", "Cari", "Muhasebe", "Fatura", "Personel işlemleri"])
menuOlustur(["Stok", "Muhasebe"])

# 201 ╔
# 205 ═
# 187 ╗
# 186 ║
# 200 ╚
# 188 ╝
# 185 ╣
# 204 ╠
 
    

    
                 
