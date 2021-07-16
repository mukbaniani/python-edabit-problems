import unittest
from Employee import Employee


class TestEmployee(unittest.TestCase):
    def test_Employee(self):
        john = Employee('John Doe')
        mary = Employee('Mary Major', salary=120000)
        richard = Employee('Richard Roe', salary=110000, height=178)
        giancarlo = Employee('Giancarlo Rossi', salary=115000, height=182, nationality='Italian')
        peng = Employee('Peng Zhu', salary=500000, height=185, nationality='Chinese', subordinates=[i.lastname for i in (john, mary, richard, giancarlo)])


        self.assertEqual(john.lastname, 'Doe', 'John\'s lastname should be "Doe"')
        self.assertEqual(mary.salary, 120000, 'Mary\'s salary should be 120000')
        self.assertEqual(richard.height, 178, 'Richard\'s height should be 178')
        self.assertEqual(giancarlo.nationality, 'Italian', 'Giancarlo\'s nationality should be "Italian"')
        self.assertEqual(peng.subordinates, ['Doe', 'Major', 'Roe', 'Rossi'], 'Peng\'s subordinates should be a list containing 4 strings')


if __name__ == '__main__':
    unittest.main()