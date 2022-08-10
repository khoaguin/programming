// Input: The first line contains an integer d (the distance between 2 cities). 
//        The second line contains an integer m (the maximum miles a car can travel on a full tank). 
//        The third line specifies an integer n (the number of gas stops between 2 cities). 
//        Finally, the last line contains integers stop_1, stop_2, ..., stop_n (distances along the way).
// Output: The minimum number of refills needed. 
//         We assume that the car starts with a full tank. 
//         If it is not possible to reach the destination, output −1.


#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using std::cin;
using std::cout;
using std::vector;
using std::max;


// Recursive solution
int refills(int location, int dist, int tank, vector<int> & stops, int passed_stop) {
    // Base case: when we reach the final destination
    if (location + tank >= dist) {
        return 0;
    }
    // Base case: when we cannot reach the final destination
    ++passed_stop;
    if ((stops.size() == 0) || (stops[0] - location > tank)) {
        return -passed_stop;
    }
    // Recursive case: Refuel at the furthest reachable station
    int last_stop = location;
    while ((stops.size() > 0) && (stops[0] - location <= tank)) {
        last_stop = stops[0];
        stops.erase(stops.begin());
    }
    // std::cout << "last stop = " << last_stop << "\n";

    return 1 + refills(last_stop, dist, tank, stops, passed_stop);
}


int main() {
    int d = 0;  // the distance between 2 cities
    cin >> d;
    int m = 0;  // maximum miles a car can go with a full tank
    cin >> m;
    int n = 0;  // number of stops
    cin >> n;

    vector<int> stops(n);  // distances of gas stops compared to the starting point
    for (size_t i = 0; i < n; ++i)
        cin >> stops.at(i);

    cout << refills(0, d, m, stops, 0) << "\n";

    return 0;
}
