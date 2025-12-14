"""Вычисление самой выгодной траты энергии в игре Pixels"""

import classes as cl
import settings as st
import time as t
import random as r
import color as clr


if __name__ == '__main__':
    price_items = {'Cooking Mix': 10}
    print(f'|{"ITEM":^30}|{"PRICE":^10}|')
    for i in sorted(cl.Items.get()):
        try:
            item = cl.Items(i[1])
            price_items[i[0]] = item.price
            print(f'|{i[0]:^30}|{price_items[i[0]]:^10}|')
            t.sleep(r.randint(3, 7))
        except (Exception,):
            print(f"{clr.red}|{'Ошибка получения цены ' + i[0]:^41}|{clr.end}")
            price_items[i[0]] = 0

    print()
    value_list = []
    for i in st.items_data:
        if i == 'Plants':
            for j in st.items_data["Plants"]:
                price = price_items[j]
                cost_coin = st.items_data["Plants"][j][0]
                cost_energy = st.items_data["Plants"][j][1]
                value = round((price - cost_coin) / cost_energy, 2)
                value_list.append([value, price, j])
        elif i == 'Mine':
            for j in st.items_data["Mine"]:
                value = 0
                for h in st.items_data["Mine"][j]:
                    value += round(price_items[h[0]]*h[1], 2)
                value_list.append([value, 0, j])
        elif i == 'Craft':
            for j in st.items_data["Craft"]:
                cost_coin = 0
                for k in st.items_data["Craft"][j][:-1]:
                    cost_coin += price_items[k[0]] * k[1]
                price = price_items[j]
                cost_energy = st.items_data["Craft"][j][-1]
                value = round((price - cost_coin) / cost_energy, 2)
                value_list.append([value, price, j])

    value_list.sort(reverse=True)
    print(f'|{"ITEM":^30}|{"PRICE":^10}|{"VALUE":^10}|{"COMPONENTS":^76}|')
    for i in value_list:
        i.reverse()
        components = []
        if i[0] in st.items_data['Craft']:
            for j in st.items_data["Craft"][i[0]][:-1]:
                components.append(j[1])
                components.append(j[0])
                components.append('+')
            print(f'|{i[0]:^30}|{i[1]:^10}|{i[2]:^10}| {" ".join(map(str,components[:-1])):<75}|')
        else:
            print(f'|{i[0]:^30}|{i[1]:^10}|{i[2]:^10}|')




