class House:

    def __init__(self,code,price,rooms,sm,elevator,condominuim,garage,address,pc,town_hall,province,owner):

        self.__code = code
        self.__price = price
        self.__rooms = rooms
        self.__sm = sm
        self.__elevator = elevator
        self.__condominuim = condominuim
        self.__garage = garage
        self.__address = address
        self.__pc = pc
        self.__town_hall = town_hall
        self.__province = province
        self.__owner = owner

    def set_code(self,code):
        self.__code = code

    def set_price(self,price):
        self.__price = price

    def set_rooms(self,rooms):
        self.__rooms = rooms

    def set_sm(self,sm):
        self.__sm = sm

    def set_elevator(self,elevator):
        self.__elevator = elevator

    def set_condominium(self,condominuim):
        self.__condominuim = condominuim

    def set_grage(self,garage):
        self.__garage = garage

    def set_address(self,address):
        self.__address = address

    def set_pc(self,pc):
        self.__pc = pc

    def set_town_hall(self,town_hall):
        self.__town_hall = town_hall

    def set_province(self,province):
        self.__town_hall = town_hall

    def set_owner(self,owner):
        self.__owner = owner

    def get_code(self):
        return self.__code

    def get_price(self):
        return self.__price 

    def get_rooms(self):
        return self.__rooms

    def get_sm(self):
        return self.__sm

    def get_elevator(self):
        return self.__elevator

    def get_condominium(self):
        return self.__condominuim

    def get_grage(self):
        return self.__garage

    def get_address(self):
        return self.__address

    def get_pc(self):
        return self.__pc

    def get_town_hall(self):
        return self.__town_hall

    def get_province(self):
        return self.__town_hall 

    def get_owner(self):
        return self.__owner

    def __str__(self):
        return "Code: " + self.__code + "\n\tPrice: "+ str(format(self.__price,".2f")) + "\n\t" + "€\n\tN. rooms: " + str(self.__rooms) + "\n\tSquare meters: " + str(self.__sm) + "\n\tElevator: " + self.__elevator + "\n\tCondominium: " + self.__condominuim + "\n\tGarage: " + self.__garage + "\n\tAddress: " + self.__address + "\n\tPostal code: " + self.__pc + "\n\tTown Hall: " + self.__town_hall + "\n\tProvince: " + self.__province + "\n\tOwner: " + self.__owner.get_all_info()

    def get_all_info(self):
        return self.__code + ","+ str(format(self.__price,".2f")) + ","  + str(self.__rooms) + "," + str(self.__sm) + "," + self.__elevator + "," + self.__condominuim + "," + self.__garage + "," + self.__address + "," + self.__pc + "," + self.__town_hall + "," + self.__province + "," + self.__owner.get_all_info()
