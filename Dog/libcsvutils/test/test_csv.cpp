#include <iostream>
#include "internal.h"
#include "csv_utils.h"

void print(std::list<std::string>& container){
	for(std::list<std::string>::iterator itr=container.begin();itr!=container.end();itr++){
		std::cout<<*itr<<std::endl;
	}
}

int main(){
	std::list<std::string> s = SplitLineByDelimiter("a,b,zhang,liam",",");
	print(s);
	std::cout<<"test project"<<std::endl;
}
