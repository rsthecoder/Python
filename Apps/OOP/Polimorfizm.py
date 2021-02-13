# Bu ornegin adi polimorfizm -> Bu terimsel ifade kullanilabilir
class One:
    var = 100

    def my_def(self):
        return self.var

class Two(One):
    var = 200

obj = Two()

print(obj.my_def())