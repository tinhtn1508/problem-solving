#include <bits/stdc++.h>

int solution(std::string s) {
    int moves = 0;
    for(int i = 0; i < s.size(); i++) {
        int runLength = 1;
        for (; i + 1 < s.size() && s[i] == s[i+1]; i++) {
            runLength++;
        }
        moves += runLength/3;
    }
    return moves;
}

int main() {
    std::cout << solution("baaabbaabbba") << std::endl;
    return 0;
}