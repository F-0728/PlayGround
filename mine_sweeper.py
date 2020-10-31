import random

print("""---Welcome to Minesweeper.

---ルール説明
・100マス中に地雷が10個あります。
・開始すると盤面が表示されます。
  番地指定はアルファベット→数字の順でお願いします。
  対応させるの面倒なので小文字で入力してください。
  ex)
   右上角・・・a9
・表示される数は周囲(最大)8マスにある地雷の数です。

---いつものことですが修正・デバッグにご協力くださると幸いです。

---Press Enter to Start.
""")

start = input()

a = [" " for i in range(100)]

def printout(x, y):
 return "    ".join(str(a[i]) for i in range(x, y))

def output():
 print("     0    1    2    3    4    5    6    7    8    9")
 print("  -------------------------------------------------")
 print("a | ", printout(0, 10))
 print("  | ")
 print("b | ", printout(10, 20))
 print("  | ")
 print("c | ", printout(20, 30))
 print("  | ")
 print("d | ", printout(30, 40))
 print("  | ")
 print("e | ", printout(40, 50))
 print("  | ")
 print("f | ", printout(50, 60))
 print("  | ")
 print("g | ", printout(60, 70))
 print("  | ")
 print("h | ", printout(70, 80))
 print("  | ")
 print("i | ", printout(80, 90))
 print("  | ")
 print("j | ", printout(90, 100))


output()
print()
print()
print()

num = [i for i in range(100)]
random.shuffle(num)
mine = num[:10]
mine.sort()
default = [0 for i in range(100)]

for i in range(10):
 if mine[i] == 0:
  default[1] += 1
  default[10] += 1
  default[11] += 1
  
 elif mine[i] == 9:
 	default[8] += 1
 	default[18] += 1
 	default[19] += 1
 	
 elif mine[i] == 90:
  default[80] += 1
  default[81] += 1
  default[91] += 1
  
 elif mine[i] == 99:
  default[88] += 1
  default[89] += 1
  default[98] += 1
  
 elif mine[i] % 10 == 0:
  default[mine[i] - 10] += 1
  default[mine[i] - 9] += 1
  default[mine[i] + 1] += 1
  default[mine[i] + 10] += 1
  default[mine[i] + 11] += 1
  
 elif mine[i] % 10 == 9:
 	default[mine[i] - 11] += 1
 	default[mine[i] - 10] += 1
 	default[mine[i] - 1] += 1
 	default[mine[i] + 9] += 1
 	default[mine[i] + 10] += 1
 	
 elif mine[i] // 10 == 0:
  default[mine[i] - 1] += 1
  default[mine[i] + 1] += 1
  default[mine[i] + 9] += 1
  default[mine[i] + 10] += 1
  default[mine[i] + 11] += 1
  
 elif mine[i] // 10 == 9:
  default[mine[i] - 11] += 1
  default[mine[i] - 10] += 1
  default[mine[i] - 9] += 1
  default[mine[i] - 1] += 1
  default[mine[i] + 1] += 1
  
 else:
  default[mine[i] - 11] += 1
  default[mine[i] - 10] += 1
  default[mine[i] - 9] += 1
  default[mine[i] - 1] += 1
  default[mine[i] + 1] += 1
  default[mine[i] + 9] += 1
  default[mine[i] + 10] += 1
  default[mine[i] + 11] += 1

for i in range(10):
 default[mine[i]] = 9

def select_henkan(x):
 list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
 try:
  return list.index(x)
 except:
  return

while 1:
 select_input = input()
 try:
  select = int(str(select_henkan(select_input[0])) + select_input[1])
 except:
  continue
 
 a[select] = default[select]
 
 hashi = [i for i in range(10)]
 hashi.extend([i + 90 for i in range(10)])
 hashi.extend([10, 19, 20, 29, 30, 39, 40, 49, 50, 59, 60, 69, 70, 79, 80, 89])
 semi_hashi_yoko = [i + 1 for i in range(8)] 
 semi_hashi_yoko_2 = [i + 91 for i in range(8)]
 semi_hashi_tate = [10 * (i + 1) for i in range(8)]
 semi_hashi_tate_2 = [10 * (i + 1) + 9 for i in range(8)]
 
 if select not in hashi:
  if a[select] == 0:
   if default[select + 1] == 0:
    a[select + 1] = 0
   if default[select - 1] == 0:
    a[select - 1] = 0
   if default[select + 10] == 0:
    a[select + 10] = 0
   if default[select - 10] == 0:
    a[select - 10] = 0
   if default[select - 11] == 0:
    a[select - 11] = 0
   if default[select - 9] == 0:
    a[select - 9] = 0
   if default[select + 9] == 0:
    a[select + 9] = 0
   if default[select + 11] == 0:
    a[select + 11] = 0
    
 if select in hashi:
  if a[select] == 0:
   if select == 0:
   	if default[1] == 0:
   	 a[1] = 0
   	if default[10] == 0:
   	 a[10] = 0
   	if default[11] == 0:
   	 a[11] = 0
 
   if select == 9:
    if default[8] == 0:
     a[8] = 0
    if default[18] == 0:
     a[18] = 0
    if default[19] == 0:
     a[19] = 0
    
   if select == 90:
    if default[80] == 0:
     a[80] = 0
    if default[81] == 0:
     a[81] = 0
    if default[91] == 0:
     a[91] = 0
     
   if select == 99:
    if default[88] == 0:
     a[88] = 0
    if default[89] == 0:
     a[89] = 0
    if default[98] == 0:
     a[98] = 0
     
   elif select in semi_hashi_yoko:
    if default[select + 1] == 0:
     a[select + 1] = 0
    if default[select - 1] == 0:
     a[select - 1] = 0
    if default[select + 10] == 0:
     a[select + 10] = 0
    if default[select + 9] == 0:
     a[select + 9] = 0
    if default[select + 11] == 0:
     a[select + 11] = 0
     
   elif select in semi_hashi_yoko_2:
    if default[select + 1] == 0:
     a[select + 1] = 0
    if default[select - 1] == 0:
     a[select - 1] = 0
    if default[select - 10] == 0:
     a[select - 10] = 0
    if default[select - 9] == 0:
     a[select - 9] = 0
    if default[select - 11] == 0:
     a[select - 11] = 0
     
   elif select in semi_hashi_tate:
    if default[select + 1] == 0:
     a[select + 1] = 0
    if default[select - 9] == 0:
     a[select - 9] = 0
    if default[select - 10] == 0:
     a[select - 10] = 0
    if default[select + 10] == 0:
     a[select + 10] = 0
    if default[select + 11] == 0:
     a[select + 11] = 0
     
   elif select in semi_hashi_tate_2:
    if default[select - 1] == 0:
     a[select - 1] = 0
    if default[select - 10] == 0:
     a[select - 10] = 0
    if default[select + 10] == 0:
     a[select + 10] = 0
    if default[select - 11] == 0:
     a[select - 11] = 0
    if default[select + 9] == 0:
     a[select + 9] = 0
      
 for i in range(30):
  for num in range(100):
   if num not in hashi:
    if a[num] == 0:
     a[num + 1] = default[num + 1]
     a[num - 1] = default[num - 1]
     a[num + 10] = default[num + 10]
     a[num - 10] = default[num - 10] 
     a[num - 9] = default[num - 9]
     a[num + 9] = default[num + 9]
     a[num - 11] = default[num - 11]
     a[num + 11] = default[num + 11]
    
   if num == 0:
    if a[0] == 0:
     a[1] = default[1]
     a[10] = default[10]
     a[11] = default[11]
    
   if num == 9:
    if a[9] == 0:
     a[8] = default[8]
     a[18] = default[18]
     a[19] = default[19]
    
   if num == 90:
    if a[90] == 0:
     a[80] = default[80]
     a[91] = default[91]
     a[81] = default[81]
   
   if num == 99:
    if a[99] == 0:
     a[89] = default[89]
     a[88] = default[88]
     a[98] = default[98]
   
   elif num in semi_hashi_tate:
    if a[num] == 0:
     a[num + 1] = default[num + 1]
     a[num + 10] = default[num + 10]
     a[num - 10] = default[num - 10]
     a[num - 9] = default[num - 9]
     a[num + 11] = default[num + 11]
      
   elif num in semi_hashi_tate_2:
    if a[num] == 0:
     a[num - 1] = default[num - 1]
     a[num + 10] = default[num + 10]
     a[num - 10] = default[num - 10]
     a[num + 9] = default[num + 9]
     a[num - 11] = default[num - 11]
   
   elif num in semi_hashi_yoko:
    if a[num] == 0:
     a[num + 1] = default[num + 1]
     a[num - 1] = default[num - 1]
     a[num + 10] = default[num + 10]
     a[num + 9] = default[num + 9]
     a[num + 11] = default[num + 11]

   elif num in semi_hashi_yoko_2:
    if a[num] == 0:
     a[num + 1] = default[num + 1]
     a[num - 1] = default[num - 1]
     a[num - 10] = default[num - 10]
     a[num - 9] = default[num - 9]
     a[num - 11] = default[num - 11]
 
 output()

 if select in mine:
 	print("Game over...")
 	break

 print()
 print()
 print()
 
 if a.count(" ") == 10:
  print("Congratulations!!!")
  break
