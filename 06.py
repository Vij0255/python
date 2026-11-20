# # 練習１:変数を3つ
# mochimono = "かばん"
# mochimono2 = "さいふ"
# mochimono3 = "スマホ"
# print(mochimono)
# print(mochimono2)
# print(mochimono3)

#  練習１:リストを作る
# tensu = [82, 91, 75, 68, 95]
# print(tensu)
# print(len(tensu))

#  練習２:番号で取り出す
# tensu = [82, 91, 75, 68, 95]
# print(tensu[0])
# print(tensu[4])

#  練習２:後ろから2番目
# tensu = [82, 91, 75, 68, 95]
# print(tensu[2])
# print(tensu[-2])
# print(tensu[len(tensu)-2])

#  練習２:範囲の外
# tensu = [82, 91, 75, 68, 95]
# print(tensu[-1])
# print(tensu[5])

#  練習２:append
# tensu = []
# tensu.append(82)
# tensu.append(91)
# print(tensu)

#  練習２:大きい順に上位2人
# tensu = [82, 91, 75, 68, 95]
# tensu.sort(reverse=True)
# print(tensu)
# print("1位", tensu[0], "点")
# print("2位", tensu[1], "点")

#  練習２:forで回す
# tensu = [72, 82, 91]
# for t in tensu:
#     print(tensu,[t])


# tensu=[75,82,91]
# for t in tensu:
#     print(t+5 )
# print(tensu)

# tensu=[75,82,91]
# goukei=0
# for t in tensu:
#     goukei=goukei+t
# print(goukei)
# print(f"{goukei/len(tensu):.1f}")

# tensu = [82, 91, 75, 68, 95]

# saikou = tensu[0]

# for t in tensu:
#     if t > saikou:
#         saikou = t
#     print(t,saikou)
# print("最高点は", saikou)

# tensu = [82, 55, 75, 48, 95]
# for t in tensu:
#     if t <= 60:
#         print(t)

# iro=(255, 0, 0 )    
# print(iro[0])
# print(len(iro))
# for c in iro:
#     print(c)
  
# tanjoubi = (2005,4,1)
# print(tanjoubi)
# print(tanjoubi[0],"年")
# print(tanjoubi[1],"月")
# print(tanjoubi[2],"日")

# 練習6：クラスの成績

# tensu = []

# for i in range(5):
#     ten = int(input("点数？"))
#     tensu.append(ten)
# goukei = sum(tensu)
# print("合計", goukei)
# print("平均", goukei / len(tensu))

# 練習7：買い物カゴ
# kago = []
# while True:
#     n = int(input("値段？ "))
#     if n == 0:
#         break
#     kago.append(n)
# print("合計", sum(kago))

# 練習8：順番待ち
# machi = ["吉田", "山本", "大野"]   
# yonda = machi.pop(0)               
# print(yonda + "さんどうぞ")         
# print(machi)                        