def func():
    var = 0
    print(var)
    var += 1

class test:
    var = 0
    def func(self):
        print(self.var)
        self.var += 1

test = test()
for i in range(3):
    func()
    test.func()