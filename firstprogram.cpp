#include <iostream>

// Function to calculate factorial
unsigned long long factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

int main() {
    int num;

    // Get user input
    std::cout << "Enter a non-negative integer: ";
    std::cin >> num;

    // Check for negative input
    if (num < 0) {
        std::cerr << "Error: Factorial is not defined for negative numbers.\n";
        return 1;
    }

    // Calculate and display the factorial
    unsigned long long result = factorial(num);
    std::cout << "Factorial of " << num << " is: " << result << std::endl;

    return 0;
}
