#include <stdio.h>
#include <stdint.h>


#define SR1_WIDTH 19
#define SR2_WIDTH 22
#define SR3_WIDTH 23

int main(uint8_t key){
    //load
    uint8_t LFSR1 = 0;
    uint8_t LFSR2 = 0;
    uint8_t LFSR3 = 0;
    uint8_t bitPOS = 1;
    for (int i = 0; i < 64; i++) {
        
        uint8_t data_in = (key & bitPOS);

        if (i < 19) {
            LFSR1 = LFSR1 | data_in;
        } 
        else if (i < 41) {
            LFSR2 = LFSR2 | data_in;
        } 
        else {
            LFSR3 = LFSR3 | data_in;
        }
        bitPOS = bitPOS << 1;
    }
    LFSR2 = LFSR2 >> 19; // lfsr is held in bottom 22 bits
    LFSR2 = LFSR3 >> 41;// lfsr is held in bottom 23 bits
    
    for(int tick = 0; tick < 1e6; tick++){
        //feedback
        // Polynomial: x^19+x^18+x^17+x^14+1
        uint8_t fb1 = ((LFSR1 >> 18) ^ (LFSR1 >> 17) ^ (LFSR1 >> 14))) & 1;
        // Polynomial: x^22+x^21+1
        uint8_t fb2 = ((LFSR2 >> TAP2_1) ^ (LFSR2 >> TAP2_2)) & 1;
        // Polynomial: x^23+x^22+x^21+x^8+1
        uint8_t fb3 = ((LFSR3 >> TAP3_1) ^ (LFSR3 >> TAP3_2)) & 1;


        uint8_t output = ((LFSR1 >> SR1_WIDTH-1) & 1) ^ ((LFSR2 >> SR2_WIDTH-1) & 1) ^ ((LFSR3 >> SR3_WIDTH-1) & 1)
        uint8_t output = out1 ^ out2 ^ out3;
    }
}

uint8_t 8 tic