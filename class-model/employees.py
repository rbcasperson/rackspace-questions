class Employee(Object):
    def __init__(self, first_name, last_name, pay_rate, yearly_vacation):
        self.first_name = first_name
        self.last_name = last_name
        self.pay_rate = pay_rate
        self.yearly_vacation = yearly_vacation

    def get_name(self):
        return "{0}, {1}".format(self.last_name, self.first_name)

    def get_pay_rate(self):
        return self.pay_rate

    def get_yearly_vacation(self):
        return self.yearly_vacation

class IndependantWorker(Employee):
    pass

class Contractor(IndependantWorker):
    pass

class Temporary(IndependantWorker):
    pass
