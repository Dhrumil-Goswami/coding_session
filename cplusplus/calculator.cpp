#include<iostream>
using namespace std;

int main(){
    char opration;
    float num1, num2;
    cout << "Enter Operation to perform (+,-,*,/): ";
    cin >> opration;
    cout << "Enter two numbers \n";
    cin >> num1 >> num2;
    switch(opration){
        case '+':
            cout << "Result" << num1 + num2;
            break;
        case '-':
            cout << "Result" << num1 - num2;
            break;
            
        case '*':
            cout << "Result" << num1 * num2;
            break;
        
        case '/':
            if (num2 != 0)
                cout << "Result" << num1 / num2;
            
            else
                cout<< "wrong input divide by zero not possible";
            break;
        default:
            cout<< "Invaqlid oprator";
        
        }
    return 0;
}