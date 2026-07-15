text = input('Введите любое слово: ').lower()
if text==text[::-1]:
    print('The palindromm')
else:
    print("The not pallindromm")