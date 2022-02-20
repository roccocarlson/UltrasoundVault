# Winter Wonderhack 2022
# Feb 18-20
# Rocco Carlson

import pyminizip
import os
import ggwave
import pyaudio

class vault:
    
    def __init__(self, vaultName):
        self.vaultName = vaultName
        self.status = False
        
        self.p = pyaudio.PyAudio()
        
        self.stream = self.p.open(format=pyaudio.paFloat32, channels=1, rate=48000, input=True, frames_per_buffer=1024)
        self.instance = ggwave.init() 
        
        print("Listening...")
        try:
            while True:
                data = self.stream.read(1024, exception_on_overflow=False)
                res = ggwave.decode(self.instance, data)
                if (not res is None):
                    try:
                        key_received = res.decode("utf-8")
                        self.password = key_received
                        break
                    except:
                        pass
        except KeyboardInterrupt:
            pass
        
        ggwave.free(self.instance)
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        
        try:
            print("Searching for vault...")
            pyminizip.uncompress(self.vaultName+".zip", self.password, "/Users/roccocarlson/Desktop/ggwaveTest/src",1)
            self.status = True
            print("Vault found, unlocked")
        except:
            print("No vault found, creating vault...")
            with open(self.vaultName+".txt", "w+") as file:
                file.write("Website".ljust(20) + "Username".ljust(20) + "Password".ljust(20) + "\n")
            self.status = True
            print("Vault created with name: "+self.vaultName)
            
    def printEntries(self):
        if self.status == True:
            with open(self.vaultName+".txt","r") as file:
                contents = file.read()
                print(contents)
                return contents
        else:
            print("Vault Locked!")
            return ""
    
    def newEntry(self, website, username, password):
        if self.status == True:
            with open(self.vaultName+".txt","a") as file:
                file.write(website.ljust(20)+username.ljust(20)+password+"\n")
        else:
            print("Vault Locked!")
                   
    def lockVault(self):
        pyminizip.compress(self.vaultName+".txt", None, self.vaultName+".zip", self.password, 5)
        self.status = False
        os.remove(self.vaultName+".txt")