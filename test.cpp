#include <iostream>
#include <cmath>

// Function to calculate the reward based on depth
double calculateReward(double depth) {
    // Parameters for the Gaussian-like peak
    double a = 4.0;    // Height of the peak
    double b = 30.0;   // Position of the peak
    double c = 10.0;   // Width of the peak

    // Parameters for the exponential tail
    double d = 1;   // Exponential decay factor
    double e = 100.0;   // Decay rate

    // Gaussian-like peak term
    double peak = a * exp(-pow(depth - b, 2) / (2 * c * c));

    // Exponential decay term
    double decay = -d * exp(depth / e);

    // Total reward
    return int((peak + decay) * 100);
}

int main() {
    // Output the reward for a range of depths
    std::cout << "Depth\tReward" << std::endl;
    for (int depth = 0; depth <= 120; depth++) {
        double reward = calculateReward(depth);
        std::cout << depth << "\t" << reward << std::endl;
    }
    return 0;
}
