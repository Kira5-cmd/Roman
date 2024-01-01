# constants 
ROMAN_NO_SYSTEM = ["M", 'XM', 'D', 'XD', 'C','XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
INT_NO_SYSTEM = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

#errors
class NotTrueDiv(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ZeroNotInRoman(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class NotIntegerError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class NegIntError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

#some minor function
def isnegative(no):
    return not(no == abs(no))

class Roman:
    """roman no class"""
    def __init__(self, no:int) -> None:
        if not isinstance(no, int):
            raise NotIntegerError("no should be integer")
        
        elif isnegative(no):
            raise NegIntError("negative is not allowed")
        
        if no == 0:
            raise ZeroNotInRoman("Zero is not in Roman")
        
        self.__int_no = no
        self.__roman_no = Roman.__change_int_to_Roman(no)
        self.__current_no = 0

    def __add__(self, otherno):
        sum = self.__int_no + otherno.__int_no
        return Roman(sum)
    
    def __sub__(self, otherno):
        diff = self.__int_no - otherno.__int_no
        return Roman(diff)
    
    def __mul__(self, otherno):
        return Roman(self.__int_no * otherno.__int_no)
    
    def __str__(self) -> str:
        return self.__roman_no
    
    def __repr__(self) -> str:
        return f"Roman({self.__int_no})"
    
    def __index__ (self):
        return self.__int_no
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__current_no < self.__int_no:
            self.__current_no += 1
            return Roman(self.__current_no)
        else:
            self.__current_no = 0
            raise StopIteration
    
    def __truediv__(self, otherno):
        raise NotTrueDiv("can't true div roman no")   

    def __floordiv__(self, otherno):
        return Roman(self.__int_no// otherno.__int_no)  
    
    def __mod__(self, otherno):
        return Roman(self.__int_no % otherno.__int_no)
    
    def __len__(self):
        return len(self.__roman_no)

    def __divmod__(self, otherno) -> tuple[int]:
        return (self.__int_no//otherno.__int_no, self.__int_no%self.__int_no)

    def __eq__(self, otherno):
        return self.__int_no == otherno.__int_no
    
    def __le__(self, otherno):
        return self.__int_no <= otherno.__int_no
    
    def __lt__(self, otherno):
        return self.__int_no < otherno.__int_no
    
    def __gt__(self, otherno):
        return self.__int_no > otherno.__int_no
    
    def __ge__(self, otherno):
        return self.__int_no >= otherno.__int_no

    @staticmethod
    def change_into_int(roman:int):
        roman = reversed(roman)
        no = 0
        previous_val = 0
        for char in roman:
            integer = INT_NO_SYSTEM[ROMAN_NO_SYSTEM.index(char)]
            if integer < previous_val:
                no -= integer
            else:
                no += integer
            previous_val = integer
        return no


    @staticmethod
    def __change_int_to_Roman(no:int):
        roman_no = ""
        index = 0
        roman_value = ""
        while no != 0:
            integer = INT_NO_SYSTEM[index]
            questioent , remainder = divmod(no, integer)
            no = remainder
            for i in range(questioent):
                roman_value += ROMAN_NO_SYSTEM[index]
            index += 1
        return roman_value

if __name__ == "__main__":
    a = Roman(1)