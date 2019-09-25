#!/usr/bin/env python3

# Copyright (c) 2019 Iain Menzies-Runciman
# 
# Licensed under the MIT License:
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

class Eeprom:
    def __init__(self):
        self.header = b''
        self.board_name = b''
        self.version = b''
        self.serial_number = b''
        self.configuration_options = b''
        self.reserved1 = b''
        self.reserved2 = b''
        self.reserved3 = b''
        self.user_data = b''

    def read(self):
        try:
            with open("/sys/bus/i2c/devices/0-0050/eeprom", "rb") as eeprom:
                self.header = eeprom.read(4)
                self.board_name = eeprom.read(8)
                self.version = eeprom.read(4)
                self.serial_number = eeprom.read(12)
                self.configuration_options = eeprom.read(32)
                self.reserved1 = eeprom.read(6)
                self.reserved2 = eeprom.read(6)
                self.reserved3 = eeprom.read(6)
                self.user_data = eeprom.read(4018)
        except FileNotFoundError:
            print("Cannot find the eeprom file")

if __name__ == "__main__":
    eeprom = Eeprom()
    eeprom.read()
    print("Header: ", end="") 
    for byte in eeprom.header:
        print("{:02X}".format(byte), end=" ")
    print("")

    print("Board Name: {} ".format(eeprom.board_name.decode()))
    print("Board Name (Hex): ", end="") 
    for byte in eeprom.board_name:
        print("{:02X}".format(byte), end=" ")
    print("")

    print("Version: {}".format(eeprom.version.decode())) 
    print("Version (Hex): ", end="") 
    for byte in eeprom.version:
        print("{:02X}".format(byte), end=" ")
    print("")

    print("Serial Number: {}".format(eeprom.serial_number.decode())) 
    print("Serial Number (Hex): ", end="") 
    for byte in eeprom.serial_number:
        print("{:02X}".format(byte), end=" ")
    print("")

    print("Configuration Options: ", end="")
    for byte in eeprom.configuration_options:
        print("{:02X}".format(byte), end=" ")
    print("")

    print("Reserved 1: ", end="")
    for byte in eeprom.reserved1:
        print("{:02X}".format(byte), end=" ")
    print("")

    print("Reserved 2: ", end="")
    for byte in eeprom.reserved2:
        print("{:02X}".format(byte), end=" ")
    print("")

    print("Reserved 3:", end="")
    for byte in eeprom.reserved3:
        print("{:02X}".format(byte), end=" ")
    print("")

    print("User Data: ", end="")
    for byte in eeprom.user_data:
        if byte == 255:
            break
        print("{:02X}".format(byte), end=" ")
    print("")
