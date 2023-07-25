# Floating Point Numbers

Computers store numbers in binary format. This means that the numbers are stored in the form of 0s and 1s. This is called the binary representation of the number. For example, the number `5` is stored as `101` in binary format. The number 101 is a 3 digit number. This means that the computer uses 3 bits to store the number 5. Similarly, the number `10` is stored as `1010` in binary format.

Often, the number of bits used to store a number is fixed. This means that the computer uses the same number of bits to store all numbers. For example, if the computer uses 8 bits to store a number, then the number `5` will be stored as `00000101`. This is called the fixed point representation of the number. For `float` data type, if the computer uses 16 bits to store a number, then the number `5` will be stored as `0100010100000000` and the number `0.001` will be stored as `0001010000011001`.


This is called the floating point representation of the number.

- The first bit is used to store the sign of the number. it is used to store the sign of the number. The sign is 0 for positive numbers and 1 for negative numbers.
- The next 5 bits are used to store the exponent of the number. It is used to shift the decimal point of the number.
- The last 10 bits are used to store the mantissa of the number. It is used to store the fractional part of the number.