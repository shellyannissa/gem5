#include <bits/stdc++.h>
using namespace std;

int windowSize = 16;
int targetDistance = 30;

int func(int distance) {
// Bell-shaped reward function centered around targetDistance
    double sigma = windowSize / 2.0;
    double exponent = -std::pow(distance - targetDistance, 2) / (2 * std::pow(sigma, 2));
    return static_cast<int>(std::exp(exponent) * 100); // Scale the reward
}

int main() {
    for (int i = 0; i < 128; i++) {
        cout << i << " => " << func(i) << "\n";
    }
    return 0;
}