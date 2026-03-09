from address import Address
from mailing import Mailing

to_address = Address(121609, 'Москва', 'Осенний бульвар', 14, 134)
from_address = Address(354207, 'Сочи', 'Российская', 33, 12)

mailing1 = Mailing(to_address, from_address, 100, '1234545')

print(f'Отправление {mailing1.track} из {mailing1.from_address.index}, '
      f'{mailing1.from_address.city}, {mailing1.from_address.street}, '
      f'{mailing1.from_address.house} - {mailing1.from_address.apartment} '
      f'в {mailing1.to_address.index}, {mailing1.to_address.city}, '
      f'{mailing1.to_address.street}, {mailing1.to_address.house} - '
      f'{mailing1.to_address.apartment}. Стоимость {mailing1.cost} рублей.')
