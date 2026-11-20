# # 練習0:input　を　int() で　数にする
# # print("年齢を入力してください")
# # nenrei = int(input())
# # print("年齢", nenrei + 1, "歳です")
# # 練習1:計算の記号
# # print(10/4)
# # print(10//4)
# # print(10%4)
# # print(10**2)
# namae = ("鈴木")
# nenrei = 18

# print("私は" + namae + "です")
# # print(f"私は{namae}です。年齢は{nenrei}歳です") # f-string
# bmi = 62/(1.72**2)
# print(f"BMIは{bmi}です")
# print(f"BMIは{bmi:.1f}です") 
# denchi = 15
# if denchi < 20:
#     print("充電してください")

# 練習３:if/else
# taiju = 70

# if taiju > 60:
#     print("60kgより重い")
# else:
#     print("60kg以下です")
# bmi = 25

# if bmi < 18.5:
#     print("やせ")
# elif bmi < 25:
#     print("標準")
# else:
#     print("肥満")
# 練習5:BMI を計算して、判定する
print("身長(m)を入力してください")
shinchou = float(input())
print("体重(kg)を入力してください")
taiju = float(input())

bmi = taiju / (shinchou ** 2)
print(f"BMIは{bmi:.1f}です")
if bmi < 18.5:
    print("判定: やせ")
elif bmi < 25:
    print("判定: 標準")
else:
    print("判定: 肥満") 