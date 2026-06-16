from address import Address
from mailing import Mailing

address = Address("543000", "Уфа", "Советская", "4", "25")
address2 = Address("110220", "Пермь", "Ленина", "5", "26")
mailing = Mailing(to_address=address, from_address=address2,
                  cost=500, track="3429")


print(f"Отправление: {mailing.track} из{address} в{address2}.Стоимость\
{mailing.cost} рублей.")
