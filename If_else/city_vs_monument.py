city_name = input('Enter the name of city : ')


if city_name == 'Delhi'.casefold():
    print('Red Fort')
elif city_name == 'Agra'.casefold():
    print('Taj Mahal')
elif city_name == 'Jaipur'.casefold():
    print('Hawa Mahal')
else:
    print('city-name-not-found')
