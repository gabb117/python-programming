#class person

class Person:

    def __init__(self,name,surname,telephone,cellphone):
        self.__name = name
        self.__surname = surname
        self.__telephone = telephone
        self.__cellphone = cellphone

    def set_name(self,name):
        self.__name = name

    def set_surname(self,surname):
        self.__surname = surname

    def set_telephone(self,telephone):
        self.__telephone = telephone

    def set_cellphone(self,cellphone):
        self.__cellphone = cellphone

    def get_name(self):
        return self.__name
    
    def get_surname(self):
        return self.__surname

    def get_telephone(self):
        return self.__telephone

    def get_cellphone(self):
        return self.__cellphone

    def __str__(self):
        return "Name: " + self.__name + "\nSurname: " + self.__surname + "\nTelephone: " + self.__telephone + "\nCellphone: " + self.__cellphone

    def get_all_info(self):
        return self.__name + ";" + self.__surname + ";" + self.__telephone + ";" + self.__cellphone
