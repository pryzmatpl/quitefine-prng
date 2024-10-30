// Quite fine PRNG
// Compile with clang++ -Wc++11-extensions ./rand.cpp -o rand
#include <iostream>
#include <cstdlib>
#include <cstdint>
#include <chrono>
#include <optional>

const uint64_t seed = 0x5C4E18FBA0276AE4;
const uint64_t prime_constant = 6364136223846793005ULL;

int main(int argc, char** argv) {
    if (argc < 2) {        
        std::cerr << "Usage: " << argv[0] << " <rounds> <upperbound>\n";        
        return 1;
    }

    int rounds = std::atoi(argv[1]);
    int upperBound = std::atoi(argv[2]);
    uint64_t randomNum = seed;

    for (int a = 0; a < rounds; a++) {
        const auto times = std::chrono::seconds(std::time(NULL)).count();
        randomNum ^= (randomNum >> 13);
        randomNum = (randomNum << 7) | (randomNum >> (64 - 7)); //OR Step!
        randomNum *= prime_constant;
        randomNum += times*times;
        randomNum ^= (randomNum << 5);
        randomNum = randomNum % 0xFFFFFFFF;
    }
    
    std::cout << "RN: " << randomNum % upperBound << "\n";
    
    return 0;
}
