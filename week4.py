# # # 練習1:for の形
# # for i in range(3):
# #    print("こんにちは")

# # print("おわり")
# # 練習2:数が２つのrange
# # for i in range (2, 6):
# #    print(i)

# # 練習2:数が3つのrange
# # for i in range (0, 10, 3):
# #     print(i)

# # for i in range (0, 10, ):
# #    print(i)

# # 練習3:3 の段
# dan=3


# # for i in range(1, 10):
# #     print(dan, "x", i, "=", dan * i)


# # for i in range(1, 4):
# #     for j in range(1, 4):
# #         print(i, "x", j, "=", i * j)
# for dan in range (1, 10):
#     for i in range(1, 10):
#         print(dan, "x", i, "₌", dan * i)

# goukei = 0

# for i in range(1, 101):
#     goukei = goukei + i

# print(goukei)

# goukei = 0

# for i in range(1, 6):
#     goukei = goukei + i

# print(goukei)


# goukei = 0

# for i in range(1, 6):

#     # goukei = goukei + i
#     print(i, goukei)
# print(goukei)

# for i in range(1, 101):
#     goukei = goukei + i

# print(goukei, "円")

# goukei = 0

# for i in range(1, 101):
#     goukei = goukei + i

# print(goukei, "円")
# dan =int(input("なんの段"))
# for i in range (1, 10):
#     print(dan, "x", i, "=",dan * i)
saigo = int(input("何日分"))
goukei = 0

for i in range(1, saigo + 1):
    goukei = goukei + i

print(goukei)
