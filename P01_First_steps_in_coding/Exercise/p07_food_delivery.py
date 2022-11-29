count_chicken_menu = int(input())
count_fish_menu = int(input())
count_vegan_menu = int(input())

price_chicken_menu = 10.35
price_fish_menu = 12.40
price_vegan_menu = 8.15
price_for_delivery = 2.50
total_sum_of_menus = count_chicken_menu * price_chicken_menu + count_fish_menu * \
            price_fish_menu + count_vegan_menu * price_vegan_menu
price_dessert = 0.20 * total_sum_of_menus

price_for_order = total_sum_of_menus + price_dessert + price_for_delivery

print(price_for_order)
