#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telnetlib
 
HOST = "10.1.202.4"
PORT = "4001"
import time

def dump_basic(adr):



    tn = telnetlib.Telnet(HOST, PORT)
    print "Connected to Telnet"

    tn.write("\n")
    tn.write("/A"+adr+"\r\n")
    print tn.read_until("\n")
    tn.write("/?!\r\n")
    print tn.read_until("\n")
    print "Communication established"

    tn.write('\x06')
    tn.write("044")
    # 040
    tn.write("\r\n")

    answer = tn.read_until("!")

    print answer
    time.sleep(10)
    tn.close()




def dump_profiles(adr):
    tn = telnetlib.Telnet(HOST, PORT)
    print "Connected to Telnet"

    tn.write("\n")
    tn.write("/A"+adr+"\r\n")
    print tn.read_until("\n")
    tn.write("/?!\r\n")
    print tn.read_until("\n")
    print "Communication established, dumping data for address " + adr

    tn.write('\x06')
    tn.write("040")
    # 040
    tn.write("\r\n")

    answer = tn.read_until("!")

    print answer

    tn.close()

    time.sleep(10)




#513.0020447 alejka referencyjna 12 lamp
#513.0020438 alejka novalux
#513.0020453 swietlowki

#read_time("513.0020455")

dump_basic("513.0020455")
dump_profiles("513.0020455")

dump_basic("513.0020447")
dump_profiles("513.0020447")

dump_basic("513.0020438")
dump_profiles("513.0020438")

dump_basic("513.0020453")
dump_profiles("513.0020453")

