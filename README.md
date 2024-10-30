# Quite Fine PRNG

A fun project to create a simple Pseudo-Random Number Generator (PRNG) in C++ using basic bitwise operations, multiplication with a prime constant, and time-based operations.

### Overview

This PRNG uses a fixed seed and introduces randomness through a combination of shifting, rotating, multiplication with a prime constant, and the current time to generate numbers. It is intended to be a basic exploration of pseudo-random number generation techniques in C++.

### How It Works

The generator starts with a fixed seed and goes through multiple rounds of transformations, each involving:

    Bitwise XOR and shifts
    Left and right rotations
    Multiplication with a prime constant
    Adding time-based values squared

These transformations aim to create a simple yet interesting approach to random number generation.

### Usage
Compilation

To compile the code, use clang++:

> clang++ -Wc++11-extensions ./rand.cpp -o rand

Running

You can run the compiled executable by providing the number of rounds and an upper bound for the generated random number:

> ./rand <rounds> <upperbound>

For example:

> ./rand 10 100

This will run 10 rounds of the PRNG and print a random number between 0 and 99.

### Code Explanation

Here's a breakdown of the PRNG code:

    Seed: A fixed initial seed value is defined in the code.
    Prime Constant: A large prime constant used to diversify the number generation.
    Rounds: The number of iterations to increase randomness.
    Time Factor: Incorporates the current time to add variability based on runtime.

The transformations performed on the seed in each round include XOR shifts, rotations, and modular arithmetic.

### Example

If you compile and run the program with:

> ./rand 15 50

You might see an output like:

> RN: 23

Each execution will yield different results depending on the rounds, time, and prime-based transformations.
Notes
    
    Do not use this in production.

    This project is meant for fun and learning purposes and should not be used in cryptographic contexts. The algorithm does not guarantee true randomness or resistance to predictability attacks.

    The code is a basic example of how to implement a custom PRNG using C++ with bitwise operations.

### License

This project is licensed under the MIT License - see the LICENSE file for details.