# globals
index = 0
byte = 256
bytelist = [0 for i in range(byte)]
pointer = 0
program = None

# increments pointer by one
def increment_pointer():
    global pointer
    if pointer >= byte - 1: pointer = 0
    else: pointer += 1

# decrements pointer by one
def decrement_pointer():
    global pointer
    if pointer <= 0: pointer = byte - 1
    else: pointer -= 1

# increments byte at pointer by one
def increment_byte():
    if bytelist[pointer] >= byte - 1: bytelist[pointer] = 0
    else: bytelist[pointer] += 1

# decrements byte at pointer by one
def decrement_byte():
    if bytelist[pointer] <= 0: bytelist[pointer] = byte - 1
    else: bytelist[pointer] -= 1

# outputs byte at pointer
def output_byte():
    char = chr(bytelist[pointer])
    print(char, end='')

# outputs number at pointer
def output_num():
    num = bytelist[pointer]
    print(num)

# ends loop if byte at pointer zero
def loop_start():
    global index
    if not bytelist[pointer]:
        loops = 1
        while index < len(program) - 1 and loops > 0:
            index += 1
            if program[index] == '[': loops += 1
            elif program[index] == ']': loops -= 1

# loops if byte at pointer nonzero
def loop_end():
    global index
    if bytelist[pointer]:
        loops = 1
        while index < len(program) - 1 and loops > 0:
            index -= 1
            if program[index] == '[': loops -= 1
            elif program[index] == ']': loops += 1

# sets byte at pointer to given value
def set_byte(value):
    bytelist[pointer] = min(max(0, value), byte - 1)

# processes given char
def process(char):
    if char == '>': increment_pointer()
    elif char == '<': decrement_pointer()
    elif char == '+': increment_byte()
    elif char == '-': decrement_byte()
    elif char == '.': output_byte()
    elif char == ':': output_num()
    elif char == '[': loop_start()
    elif char == ']': loop_end()
    elif char.isalpha(): set_byte(ord(char))
    elif char.isdecimal(): set_byte(int(char))

# parses given program
def parse(prog):
    global index, program
    program = prog
    while index < len(program):
        char = program[index]
        process(char)
        index += 1
