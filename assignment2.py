# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import socket
import sys
import argparse

import socket
import sys
import argparse

class Assignment2:

    age = 0
    name = ""
    modString = ""
    host = ""

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Task 1 (Constructor)

    def __init__(self, age = 0):
        self.age = age

# Task 2 (sayWelcome)

    def sayWelcome(self, name = "User"):

        self.name = name
        print("Welcome to the assignment, {0}!  ".format(self.name) + "Haven't seen you for {0}".format(self.age) + " years!")

# Task 3 (List)

    def doubleList(self, list = []):

        result_list = []
        pos = 0

        while pos < len(list):
            string = list[pos] + list[pos]
            result_list.append(string)
            pos = pos + 1

        pos = 0
        while pos < len(list):

            if (pos + 1)%2 != 0:
                result_list.append(list[pos])
            pos = pos + 1

        pos = 0
        while pos < len(list):

            if (pos + 1) % 2 == 0:
                result_list.append(list[pos])
            pos = pos + 1

        return result_list

#Task 4 (String Manipulation)

    def modifyString(self, name = ""):

        pos = 0
        help = ""
        result = []
        myString = name

        while pos < len(name):

            if (pos + 1) % 3 == 0 and ord(myString[pos]) >= 97 and ord(myString[pos]) <= 122:
                result.append(chr(ord(myString[pos]) - 32))
            elif (pos + 1) %  3 != 0 and (pos + 1) %  4 == 0 and ord(myString[pos]) >= 65 and ord(myString[pos]) <= 90:
                result.append(chr(ord(myString[pos]) + 32))
            elif (pos + 1) % 3 != 0 and (pos + 1) % 4 != 0 and (pos + 1) % 5 == 0:
                result.append(chr(32))
            else:
                result.append(myString[pos])
            pos = pos +1

        for x in result:
            help = help + x

        return help

#Task 5 (Loop and Conditional statements)

    def isGoodPassword(password = ""):

        upLet = 0
        lowLet = 0
        specLet = 0
        num =  0

        if len(passw) < 9:
           return False
        else:
            pos = 0
            while pos < len(password):

                if(ord(password[pos]) >= 97 and ord(password[pos]) <= 122):
                    lowLet = lowLet + 1
                elif(ord(password[pos]) >= 65 and ord(password[pos]) <= 90):
                    upLet = upLet + 1
                elif password[pos].isdigit():
                    num = num + 1
                elif (ord(password[pos]) == 44 or ord(password[pos]) == 46 or ord(password[pos]) == 35 or ord(password[pos]) == 40):
                    specLet = specLet + 1

                pos = pos + 1

            if(upLet > 2 or lowLet > 1) and (specLet > 1 or num > 0):
                return True
            else:
                return False

# Task 6 (Socket)
    def connectTcp(self, host = "", port = 0):


        try:
            self.host = socket.gethostbyname(host)
            print("Good Host")
        except:
            print("Could not connect to host")
            return False
        try:
            self.sock.connect((host, port))
            return True
        except socket.error:
            return False

        self.sock.close()






