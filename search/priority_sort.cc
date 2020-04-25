#include <bits/stdc++.h>

using ContainerType = std::pair<std::string, int>;

int main() {
    std::vector<ContainerType> vec {{"A", 1}, {"A", 5}, {"TT", 5}, {"A", 2}};
    
    std::sort(vec.begin(), vec.end(), [](const ContainerType& lhs, const ContainerType& rhs){
            if (lhs.first < rhs.first) return true;
            if (lhs.first == rhs.first) return lhs.second < rhs.second;
            return false;});
    
    for (const auto& i : vec) {
        std::cout << i.first << ":" << i.second << std::endl;
    }
}