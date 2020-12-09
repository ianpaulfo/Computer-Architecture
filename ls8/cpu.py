"""CPU functionality."""

import sys

HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.registers = [0] * 8
        self.registers[7] = 0xF4
        self.pc = 0 
        self.ram = [0] * 256
        self.halted = False

    def load(self, filename):
        """Load a program into memory."""

        address = 0
        # For now, we've just hardcoded a program:
        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

        """
        store value in memory
        """
        pass

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def ram_read(self, address):
        """
        read from memory
        """
        return self.ram[address]

    def ram_write(self, value, address):
        self.ram[address] = value


    def run(self):
        """Run the CPU."""
        while not self.halted:
            instruction_to_execute = self.ram_read(self.pc)
            opperand_a = self.ram_read(self.pc + 1)
            opperand_b = self.ram_read(self.pc + 2)
            self.execute_intstruction(instruction_to_execute, opperand_a, opperand_b)

    def execute_intstruction(self, instruction, opperand_a, opperand_b):
        if instruction == HLT:
            self.halted = True
            self.pc += 1
        elif instruction == PRN:
            print(self.registers[opperand_a])
            self.pc += 2
        elif instruction == LDI:
            self.registers[opperand_a] = opperand_b
            self.pc += 3
        else:
            print('I dont know what to do.')