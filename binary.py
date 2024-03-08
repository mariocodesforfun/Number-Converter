from typing import List

def convert(x: int) -> str:
    """Convert a decimal number to binary."""
    # % - the modulo gives the reminder 
    reminder: int = 0
    binary: List[str]=[]
    binary_number: List[str] = []
    
    while x > 0:
        reminder = x % 2
        x = x // 2
        binary.append(str(reminder))
    
    
    for i in range(len(binary)):
        index: int = len(binary) - 1 - i
        number: str = binary[index]
        if number is not None:
            binary_number.append(number)
    return ''.join(binary_number)



def decimal_to_hexa(x: int):
    """Convert a decimal number to hexadecimal."""
    reminder: int = 0
    hexa: List[str]=[]
    hexa_number: List[str] = []
    
    while x > 0:
        reminder = x % 16
        x = x // 16
        if reminder < 10:
            hexa.append(str(reminder))
        else:
            if reminder == 10:
                hexa.append('A')
            elif reminder == 11:
                hexa.append('B')
            elif reminder == 12:
                hexa.append('C')
            elif reminder == 13:
                hexa.append('D')
            elif reminder == 14:
                hexa.append('E')
            elif reminder == 15:
                hexa.append('F')
    
    for i in range(len(hexa)):
        index: int = len(hexa) - 1 - i
        number: str = hexa[index]
        if number is not None:
            hexa_number.append(number)
    return ''.join(hexa_number)


def decimal_to_octal(x: int):
    """Convert a decimal number to octal."""
    reminder: int = 0
    octal: List[str]=[]
    octal_number: List[str] = []
    
    while x > 0:
        reminder = x % 8
        x = x // 8
        octal.append(str(reminder))
    
    for i in range(len(octal)):
        index: int = len(octal) - 1 - i
        number: str = octal[index]
        if number is not None:
            octal_number.append(number)
    return ''.join(octal_number)

