#pragma once
#include "operation.h"
#include <iostream>

class Constant: public Operation
{
	public:
		Constant(float input){
			this->input = input;
		}

		float forward() override {
			return this->input;
		}
		
		float backward() override{
			return 0;
		}

		Constant operator+(Constant& c2 ){
			return Constant(this->input + c2.forward());
		}

	private:
		float input;
};

