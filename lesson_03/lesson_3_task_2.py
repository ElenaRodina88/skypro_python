from smartphone import Smartphone

smartphone1 = Smartphone('Honor', 'Magic8 Pro', '+7-987-123-45-67')
smartphone2 = Smartphone('Honor', 'X9c', '+7-000-111-22-33')
smartphone3 = Smartphone('Xiaomi', 'REDMI Note 15', '+7-111-111-22-33')
smartphone4 = Smartphone('Xiaomi', '13 Lite', '+7-000-000-22-33')
smartphone5 = Smartphone('iPhone', 'iPhone 16', '+7-000-000-00-00')

catalog = [smartphone1, smartphone2, smartphone3, smartphone4, smartphone5]

for smartphone in catalog:
    print(f'{smartphone.brand} - {smartphone.model}. {smartphone.number}')
