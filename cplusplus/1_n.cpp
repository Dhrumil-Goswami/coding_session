// #include<iostream>
// using namespace std;
// int main(){
// 	cout<< "Hello world\nhii"<<"\n"<<"checking";
// 	return 0;
// }
// int main(){
// 	int num;
// 	cout<< "enter the number: ";
// 	cin>>num;
// 	cout << "your number is :" << num;

// }
// #include<iostream>
// using namespace std;
// int main(){
// 	int num1, num2;
// 	cout<<"enter number 1";
// 	cin>>num1;
// 	cout<< "enter number 2";
// 	cin>>num2;
// 	co
// }

// #include<iostream>
// #include<climits>
// using namespace std;

// int main(){
// 	cout << "Minimum intger numbers: " << INT_MIN << endl;
// 	cout << "Maximum intger numbers: " << INT_MAX << endl;
// 	return 0;
// }

#include<iostream>
#include<climits>
using namespace std;

void checkLimits(int value){
	if (value > INT_MAX){
		cout << "Exceeded maximum limits";
	}else if (value < INT_MAX){
		cout << "Exceeded minimum limits";
	}
	else{
		cout << "its within the range";
	}

}
void checkLimits(short val){
	if (val > SHRT_MAX){
		cout << "Exceeded short maximum limit" << endl;
	}else if(val < SHRT_MIN){
		cout << "Exceeded shot minimum limit" << endl;
	}
	else{
		cout << "its within the raneg";
	}

}
int main (){
	int value = 12345;
	short val = 32767;
	checkLimits(value);
	checkLimits(value) ;
	return 0;
}