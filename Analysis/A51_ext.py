# This is the A51_ext Algorithm implemented in python to avoid dealing with timing simulation of verilator.
from bitarray import bitarray

class LFSR:
    output = None
    def __init__(self, taps, init):
        self.states = init
        self.taps = taps # do not include last bit in taps, feedback is set to originally
        max_tap = max(self.taps)

    
    def tick(self):
        feedbackBit = self.states[-1]
        for i in self.taps:
            feedbackBit = feedbackBit ^ self.states[i]
        # left shift as in presentaiton (move all down one bit)
        # feedback as MSB, my python works the opposite direction
        self.states = [feedbackBit] + self.states[:-1]   
    
class A51_Stream:
    def __init__(self,initData, filename) -> None:
       # len of SR1: 19 bits, SR2, 22 bits, SR3 23 bits
       if len(initData) != 64:
           print("Wrong input len.")
        
       SR1Init = initData[0:19]
       # Polynomial: x^19+x^18+x^17+x^14+1
       SR1Taps = [17,16,13] # taps are poly -1 as 0 based indexing
       self.SR1 = LFSR(SR1Taps,SR1Init)

       SR2Init = initData[19:41]
       # Polynomial: x^22+x^21+1
       SR2Taps = [20] # taps are poly -1 as 0 based indexing
       self.SR2 = LFSR(SR2Taps,SR2Init)

       SR3Init = initData[41:64] # python slice is x:n to include elements x-n-1
       # Polynomial: x^23+x^22+x^21+x^8+1
       SR3Taps = [21,20,7] # taps are poly -1 as 0 based indexing
       self.SR3 = LFSR(SR3Taps,SR3Init)
       self.filename = filename
    
    def tickXTimes(self,numClks):
        output = bitarray()
        for _ in range(numClks):
            bitMajority =  (self.SR1.states[8] & self.SR2.states[10]) ^ (self.SR1.states[8] & self.SR3.states[10]) ^ (self.SR2.states[10] & self.SR3.states[10])
            if self.SR1.states[8] == bitMajority:
                self.SR1.tick()
            if self.SR2.states[10] == bitMajority:
                self.SR2.tick()
            if self.SR3.states[10] == bitMajority:
                self.SR3.tick()

            # addition of AND for reduction of interdependence
            self.SR3.states[0] = self.SR1.states[0] & self.SR2.states[0]

            output.append(self.SR1.states[-1] ^ self.SR2.states[-1] ^ self.SR3.states[-1])
        with open(self.filename + ".bin", "wb") as f:
            output.tofile(f)