# globals
index = 0
byte = 256
bytelist = [0 for i in range(byte)]
pointer = 0

# increments pointer by one
def increment_pointer():
    global pointer
    if pointer >= byte - 1: pointer = 0
    else pointer += 1

# decrements pointer by one
def decrement_pointer():
    global pointer
    if pointer <= 0: pointer = byte - 1
    else pointer -= 1

# increments byte at pointer by one
def increment_byte():
    if bytelist[pointer] >= byte - 1: bytelist[pointer] = 0
    else bytelist[pointer] += 1

# decrements byte at pointer by one
def decrement_byte():
    if bytelist[pointer] <= 0: bytelist[pointer] = byte - 1
    else bytelist[pointer] -= 1

# processes given char
def process(char):
    if char == '>': increment_pointer()
    elif char == '<': decrement_pointer()
    elif char == '+': increment_byte()
    elif char == '-': decrement_byte()

# parses given program
def parse(program):
    global index
    while index < len(program):
        char = program[index]
        process(char)
        index += 1
