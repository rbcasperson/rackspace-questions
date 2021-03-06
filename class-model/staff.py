class Employee(object):
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

class IndependentWorker(Employee):
    def __init__(self, first_name, last_name, pay_rate, agency_name, label):
        Employee.__init__(self, first_name, last_name, pay_rate, 0)
        self.agency_name = agency_name
        self.label = label

    def get_name(self):
        return "{0}, {1} [ {2} ]".format(self.last_name, self.first_name, self.label)

    def get_agency(self):
        return self.agency_name

class Contractor(IndependentWorker):
    def __init__(self, first_name, last_name, pay_rate, agency_name):
        IndependentWorker.__init__(self, first_name, last_name, pay_rate, agency_name, "C")

class Temporary(IndependentWorker):
    def __init__(self, first_name, last_name, pay_rate, agency_name):
        IndependentWorker.__init__(self, first_name, last_name, pay_rate, agency_name, "T")
