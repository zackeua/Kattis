#include <iostream>
#include <string>

std::string fromOctal(const std::string& numberAsString) {
    
    if (numberAsString.find("8") != std::string::npos || numberAsString.find("9") != std::string::npos) {
        return "0";
    }

    long long number = 0;

    for (auto &&letter : numberAsString)
    {
        number *= 8;
        number += letter - '0';
    }

    return std::to_string(number);
}

std::string fromHex(const std::string& numberAsString) {
    long long number = 0;

    for (auto &&letter : numberAsString)
    {
        number *= 16;
        number += letter - '0';
    }

    return std::to_string(number);
}


int main(int argc, char const *argv[])
{
    int P;

    std::cin >> P;

    for (int i = 0; i < P; i++)
    {
        int input;
        std::string number;
        std::cin >> input;
        std::cin >> number;

        std::cout << input << " " << fromOctal(number) << " " << number << " " << fromHex(number) << "\n"; 

    }
    



    return 0;
}
