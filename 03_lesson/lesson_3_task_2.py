from smartphone import Smartphone
catalog = [
    Smartphone("Apple", "iPhone 17", "+79224395524"),
    Smartphone("HONOR", "X9d", "+79660523432"),
    Smartphone("Samsung", "Galaxy S25", "+79260553457"),
    Smartphone("HUAWEI", "Pura 80", "+79346785321"),
    Smartphone("Xiaomi", "Redmi 15C", "+74953042356")
]
for phone in catalog:
    print(f"{phone.stamp} - {phone.model} ({phone.number})")
