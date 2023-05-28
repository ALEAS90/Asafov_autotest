class Cats:
    def __init__(self, name, breed, age):

        self.name = name
        self.breed = breed
        self.age = age

    def print_data(self):
        print(
            f'Имя: {self.name}\n'
            f'Возраст: {self.age}\n'
            f'порода: {self.breed}\n'

        )

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Возраст: {self.age}\n'
            f'порода: {self.breed}\n'
        )
sema = Cats('sema', 'сфинкс', 1)

murzik = Cats('murzik', 'мейн-кун', 2)

print(sema)
print(murzik)

cats_list = [sema, murzik]
for cat in cats_list:
    cat.print_data()


