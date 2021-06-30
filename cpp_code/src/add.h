#include "operation.h"
#include <vector>
#include <iostream>


class Add: public Operation {
	public:
		Add(Operation* input1, Operation* input2){
			this->inputs.push_back(input1);
			this->inputs.push_back(input2);
		}
		float forward() override{
			std::cout<<"call forward"<<std::endl;
			return inputs[0]->forward() + inputs[1]->forward();
		}
		float backward() override{
			return 0;
		}
	public:
		std::vector<Operation*> inputs;
		float output;
};


