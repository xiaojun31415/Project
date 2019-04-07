//arrstruc.cpp--an array of structres

#include<iostream>

struct inflatable
{
	char name[20];
	float volume;
	double price;
};

int main()
{
	using namespace std;
	inflatable guests[2] = {       //initizing an array of sructs
		{ "bambi", 0.5, 21.99 },   //first structure  in array
		{ "Godzilla",2000,565.99 }  //neat structure  in array
	};
	cout << "The guests " << guests[0].name << " and " << guests[1].name << "\n have a combined volume" << guests[0].volume + guests[1].volume << " cubic feet.\n";
	return 0;
}