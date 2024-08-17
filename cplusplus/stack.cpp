#include<iostream>
#include<stack>
using namespace std;
int main(){
	stack<int> stack;
	stack.push(21);
	stack.push(22);
	stack.push(23);
	stack.push(24);
	stack.push(25);
	stack.pop();
	while (stack.size() != 2){
		cout<<stack.top();
		stack.pop();
	}
	cout<<"\nSize of stck" << stack.size();
}