class Computer:
    def __init__(self, username, memory, cpu, gpu, mouse):
        self.__username = username
        self.__memory = memory
        self.__cpu = cpu
        self.__gpu = gpu
        self.__mouse = mouse

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_memory(self):
        return self.__memory

    def set_memory(self, memory):
        self.__memory = memory

    def get_gpu(self):
        return self.__gpu

    def set_gpu(self, gpu):
        self.__gpu = gpu

    def get_cpu(self):
        return self.__cpu

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def get_mouse(self):
        return self.__mouse.getinfo()

    def getinfo(self):
        if self.__mouse is None:
            return self.__username, self.__memory, self.__cpu, self.__gpu
        else:
            return self.__username, self.__memory, self.__cpu, self.__gpu, self.__mouse.getinfo()

    def connect_mouse(self, mouse):
        self.__mouse = mouse
