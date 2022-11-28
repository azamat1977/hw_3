class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def __str__(self):
        return f'\nComputer will works faster if add to CPU size {self.__cpu} at list memory size {self.__memory} and up'


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def __str__(self):
        return f'\nLast version of smartphones have 3 slots of sim-cards and can be used with following companies {self.__sim_cards_list}.'

    def call(self, sim_card_number, call_to_number):
        self.__sim_card_number = sim_card_number
        self.__call_to_number = call_to_number
        print(f'Making call on number: {self.__sim_card_number} from sim-card-1: "Beeline" with number": {self.__call_to_number}.')


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list, location):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)
        self.__location = location

    def __str__(self):
        return f'\nNew version of MY smartfone has CPU: {self.cpu}'


comp_parametrs = Computer(4, 12)
print(comp_parametrs)


call_number = Phone('"MegaCom", "Verizon", "SaimaTelekom"')
print(call_number)
call_number.call('+996-11-22-3344', '+7-55-66-7788')


