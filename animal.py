class Animal:
    '''
    比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
    '''
    def __init__(self,animal_name,animal_coloer,animal_age,animal_sex):
        #初始化属性
        self.animal_name=animal_name
        self.animal_coloer=animal_coloer
        self.animal_age=animal_age
        self.animal_sex=animal_sex

    def call(self):
        print(f"{self.animal_name[0]}会叫")
    def run(self):
        print(f"{self.animal_name[1]}会跑")

if __name__ == '__main__':
    animal=Animal(["tom","ben"],"red","10","male")
    print(f"动物名字是：{animal.animal_name[1]}")
    print(f"动物性别是：{animal.animal_sex}")
    print(f"动物年龄是：{animal.animal_age}")
    print(f"动物颜色是：{animal.animal_coloer}")
    animal.call()
    animal.run()