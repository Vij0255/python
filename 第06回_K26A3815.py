# =============================================================
# 第6回 課題　成績管理
# Week 6 Assignment  Score manager
# =============================================================
# つかいかた / How to use:
#   1. ファイル名の「学籍番号」を自分の学籍番号に変える
#      Rename the file: replace 学籍番号 with your student ID
#   2. 「ここから書く」の下にコードを書く / Write below "ここから書く"
tensu = [82, 91, 75, 68, 95]
goukei = 0
for t in tensu:
    goukei = goukei + t

print(f"合計は {goukei} 点です")
heukin = goukei / len(tensu)
saikou = tensu[0]
for t in tensu:
    if t > saikou:
        saikou = t

print(f"平均は {heukin:.1f} 点です")
print(f"最高点は {saikou} 点です") 
# 
#  3. ▷ ボタンで実行 / Run with the ▷ button
#   4. Lv.1〜Lv.3 とおまけを、全部このファイルに書いて出す
#      Write every level in this one file and submit it
#   見出しの行（# --- Lv.1 … --- など）は消さないでください
#   Do not delete the heading lines (# --- Lv.1 … --- etc.)
# =============================================================

# --- Lv.1 【必須】60点 ---
# 5人ぶんの点数 / Scores of 5 students
tensu = [82, 91, 75, 68, 95]

# 合計を出す（見本）/ Calculate the total (example)
goukei = 0
for t in tensu:
    goukei = goukei + t

print(f"合計は {goukei} 点です")
goukei
# --- ここから書く / Write from here ---
# 1. 平均を出す（合計 ÷ 人数）。小数第1位まで表示する
#    Average = total / number of students (1 decimal place)
#    ヒント / hint: len(tensu)、f"{heikin:.1f}"
# 2. 最高点を探す / Find the highest score
#    ヒント / hint: 1人目を最高だと思っておいて、残りと比べる



heikin = goukei / len(tensu)
print(f"平均は {heikin:.1f} 点です")

saikou = tensu[0]
for t in tensu:
    if t > saikou:
        saikou = t

print(f"最高点は {saikou} 点です")



# --- Lv.2 【標準】+20点 ---
# 人数を決めず、0 を入れるまで受け付けて、合計・平均・最高点を出す
# Keep asking for scores until 0 is entered, then show total, average and highest
#   形は授業の練習7（買い物カゴ）と同じです / Same shape as Practice 7 (shopping cart):

kago = []
while True:
    ten = int(input("点数: "))
    if ten == 0:
        break
    kago.append(ten)
#   0人のときに平均を計算しないこと / Do not divide by zero
# --- ここから書く / Write from here ---
if len(kago) == 0:
    print("点数が入力されませんでした")

else:
    goukei2 = 0
    for t in kago:
        goukei2 = goukei2 + t
    heikin2 = goukei2 / len(kago)
    saikou2 = kago[0]
    for t in kago:
        if t > saikou2:
            saikou2 = t
    print(f"合計は {goukei2} 点です")
    print(f"平均は {heikin2:.1f} 点です")
    print(f"最高点は {saikou2} 点です")



# --- Lv.3 【挑戦】+20点 ---
# 1. 平均以上の点数だけを表示する / Show only scores above the average
# 2. 高い順に並べ替えて上位3人を出す / Sort and show the top 3
#    ヒント / hint: tensu.sort(reverse=True)。1位は0番、2位は1番、3位は2番
# --- ここから書く / Write from here ---

print("--- 平均以上の点数 ---")
for t in tensu:
    if t >= heikin:
        print(f"{t} 点")

tensu.sort(reverse=True)
print("--- 上位3人 ---")
print(f"1位: {tensu[0]} 点")
print(f"2位: {tensu[1]} 点")
print(f"3位: {tensu[2]} 点")




# --- おまけ ---
# ToDoリスト：メニューで 追加・削除・一覧 ができるようにする（+5点）
# To-do list with add / delete / show (+5 points)
# やる人は、下の行の先頭の「# 」を消してから書き足す
# If you do this, remove "# " at the start of the lines below first
#
todo = []

while True:
    print("--------------------")
    print("1: 追加  2: 削除  3: 一覧  0: 終了")
    erabu = int(input())

    if erabu == 0:
        print("終わります")
        break
    if erabu == 1:
        naiyou = input("追加する内容: ")
        todo.append(naiyou)
        print("追加しました")

    elif erabu == 2:
        if len(todo) == 0:
            print("ToDoがありません")
        else:
            bangou = int(input("削除する番号: "))
            if 1 <= bangou <= len(todo):
                todo.pop(bangou - 1)
                print("削除しました")
            else:
                print("その番号はありません")   


    elif erabu == 3:
        if len(todo) == 0:
            print("ToDoがありません")
        else:
            for i in range(len(todo)):
                print(f"{i + 1}: {todo[i]}")  




    else:
        print("0〜3 を入力してください")   
#     # --- ここから書く / Write from here ---
#     # erabu が 1 なら追加、2 なら削除、3 なら一覧
#     # 削除は todo.pop(番号 - 1)：画面の1番はリストの0番

