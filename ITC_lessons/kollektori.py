



print('Василий, ваша задолженность составляет 100 рублей.')

money = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? '))

while money <= 100:
	print('Маловато, Василий. Давайте ещё раз.')
	money = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? '))
print('Отлично, Василий! Вы погасили долг. Спасибо!')


