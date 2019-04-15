import math

x = math.sqrt(347991)
upperroot = int(math.ceil(x))
uppersquare = upperroot ** 2
lowerroot = int(math.floor(x))
lowersquare = lowerroot ** 2

merp = [[0 for i in range(0,upperroot)] for i in range(0,upperroot)]

print("Upperroot:" + str(upperroot))
print("Uppersquare:" + str(uppersquare))
print("Lowerroot: " + str(lowerroot))
print("Lowersquare:" + str(lowersquare))