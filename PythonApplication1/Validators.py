from abc import ABC,ABCMeta
class Validators(ABC):
    """Абстрактный класс в котором инициализоравана абстрактная проверка файла"""
    def validator(self)-> None:
        pass

    #Компоновщик
class Validator(Validators):
    """ Реальный класс наследованный от Абстрактного для добавления валидаторов или их исключения"""
    
     # Список проверок в него можно добавлять валидаторы и удалять их из списка
    def __init__(self):
        self.validators = []
     # Метод добавления нового валидатора
    def addValidator(self,validator:Validators):
        self.validators.append(validator)
     #Метод удаления валидатора
    def removeValidator(self,validator:Validators):
        self.validators.remove(validator)
    


class Valid1(Validators):
    """Непосредственно 1-ый валидатор"""
    def validator(self): #Тут какая-то проверка на валидность и возврат 0 true если проверка прошла 
        return 0

class Valid2(Validators):
    """Непосредственно 2-ой валидатор"""
    def validator(self): #Тут какая-то проверка на валидность и возврат 0 true если проверка прошла 
        return 1
        
    # Ниже можно добавлять любые валидаторы