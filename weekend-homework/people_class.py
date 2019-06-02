

class Person:
    def __init__(self, fullname='', nationality=''):
        self.name = fullname
        self.nationality = nationality

    # def greeting(self):
    #     return'Hi, my name is', self.name


class Passenger(Person):
    def __init__(self, passport_num, fullname='', nationality=''):
        super().__init__(fullname, nationality)
        self.passport_num = int(passport_num)


class Staff(Person):
    def __init__(self, title='', fullname='', nationality=''):
        super().__init__(fullname, nationality)
        self.title = title

    def assign_job(self, title):
        self.title = title
        return
