# age = 19
# money = 20000
# chicken = 20000
# beer = 10000
# drink = 5000
# if money >= chicken:
#     print("치킨을 먹는다.")
# if money >= beer and age >= 20:
#     print("맥주를 먹는다.")
# if drink <= money - chicken:
#     print("음료수를 먹는다.")

# age = 19
# money = 20000
# chicken = 20000
# beer = 10000
# drink = 5000
# if money >= chicken:
#     print("치킨을 먹는다.")
#     money = money - chicken
# if money >= beer and age >= 20:
#     print("맥주를 먹는다.")
#     money = money - beer
# if money >= drink:
#     print("음료수를 먹는다.")
#     money = money - drink

# age = 19
# money = 50000
# chicken = 20000
# beer = 10000
# drink = 5000
# if money >= chicken + beer + drink and age >= 20:
#     print("치킨, 맥주, 음료수 먹는다.")
# elif money >= chicken + beer and age >= 20:
#     print("치킨, 맥주 먹는다.")
# elif money >= chicken + drink:
#     print("치킨, 음료수 먹는다.")
# elif money >= chicken:
#     print("치킨 먹는다.")
# elif money >= beer + drink:
#     print("맥주, 음료수를 먹는다.")

age = 19
money = 50000
chicken = 20000
beer = 10000
drink = 5000
if money >= chicken:
    print("치킨을 먹는다.")
    if money - chicken >= beer and age >= 20:
        print("맥주를 먹는다.")
        if money - chicken - beer >= drink:
            print("음료수를 먹는다.")
