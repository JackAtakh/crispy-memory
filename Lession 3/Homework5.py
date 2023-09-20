all_products = {'Весь склад': {}}
korzina = []

while True:
    admin = input('Что хотите сделать? ')
    if admin.lower() == 'добавить':
        pr_name = input('Введите название продукта: ')
        pr_count = int(input('Введите количество: '))
        all_products['Весь склад'][pr_name] = pr_count
        print('Продукт успешно добавлен!')
    elif admin.lower() == 'продукты':
        print(all_products)
    elif admin.lower() == 'купить':
        print(all_products)
        user_product = input('Какой товар желаете купить? ')
        if user_product in all_products['Весь склад']:
            user_count = int(input('Сколько желаете? '))
            all_products['Весь склад'][user_product] -= user_count
            order = (user_product, user_count)
            korzina.append(order)
            print('Ваш заказ добавлен в корзину!')
        else:
            print('Такого продукта нет!')






