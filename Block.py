class Block:
    __width = None
    __height = None
    __priority = None
    __initial_priority_range = 1
    __final_priority_range = 99
    __maximum_block_width = 4
    __minimum_block_width = 1

    def __init__(self,width,height,priority):
        self.__width = width
        self.__height = height
        self.__priority = priority

    def __str__(self):
        res = str(self.__width) + "×" + str(self.__height) + ", пріоритет = " + str(self.__priority)
        return res

    def __lt__(self, other):
        return self.__priority < other.get_priority()

    def __repr__(self):
        res = "w = " + str(self.__width) + ", h = " + str(self.__height) + ", p = " + str(self.__priority)
        return res

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_priority(self):
        return self.__priority

    def check_the_correctness_of_the_block_data(self, width, height, priority):
        if priority < self.__initial_priority_range or priority > self.__final_priority_range:
            return False
        if width < self.__minimum_block_width or width > self.__maximum_block_width:
            return False
        if height < self.__minimum_block_width or height > self.__maximum_block_width:
            return False
        if width == 4:
            if height != 1:
                return False
        return True