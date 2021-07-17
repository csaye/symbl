index = 0
pointer = 0
byte = 256

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

# processes given char
def process(char):
    if char == '>': increment_pointer()
    else if char == '<': decrement_pointer()

# parses given program
def parse(program):
    global index
    while index < len(program):
        char = program[index]
        process(char)
        index += 1
