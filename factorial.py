

def FirstFactorial(num):
    if num == 1:
        return num
    return FirstFactorial(num-1) * num


print(FirstFactorial(8))