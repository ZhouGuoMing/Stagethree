from animal import *
class Cat(Animal):
    '''
    创建子类【猫】，继承【动物类】，
    重写父类的__init__方法，继承父类的属性，
    添加一个新的属性，毛发 = 短毛，
    添加一个新的方法， 会捉老鼠，
    重写父类的【会叫】的方法，改成【喵喵叫】
    '''


    def __init__(self,animal_name,animal_coloer,animal_sex,animal_age):
        super().__init__(animal_name,animal_coloer,animal_sex,animal_age)
        self.cat_name=animal_name
        self.cat_coloer=animal_coloer
        self.cat_sex=animal_sex
        self.cat_age=animal_age
        self.hair = "Short hair"
    def Catchmice(self):
        print(f"{self.cat_name}会捉老鼠")
    def call(self):
        #super(Cat, self).call()
        print(f"{self.cat_name}会喵喵叫")




if __name__ == '__main__':
    cat=Cat("tom","red","10","male")
    print(cat.animal_name)
    print(cat.cat_coloer)
    print(cat.hair)
    cat.call()
    cat.Catchmice()