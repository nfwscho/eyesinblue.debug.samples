// g++ main.cpp -o main

#include<iostream>

using namespace std;

class Rectangle {
	int width, height;
	public:
	void set_values (int,int);
	int area() {return width*height;}
};

void Rectangle::set_values (int x, int y) {
	width = x;
	height = y;
}

long factorial(int n);

int main()
{
	Rectangle rect;
	rect.set_values (3,4);

	cout << "area: " << rect.area();  

	int n(0);
	cin >> n;
	long val=factorial(n);
	cout << val;
	cin.get();



	return 0;
}

long factorial(int n)
{
	long result(1);
	while(n--)
	{
		result*=n;
	}
	return result;
}


