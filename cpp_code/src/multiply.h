#include "operation.h"
#include <vector>


class Multiply: public  Operation
{
	public:
		Multiply(Operation* input1, Operation* input2)
		{
			this->inputs.push_back(input1);
			this->inputs.push_back(input2);
		}

		float forward() override 
		{
			return this->inputs[0]->forward() *  this->inputs[0]->forward();
		}

		float backward() override
		{
			return 0;
		}

	private:
		std::vector<Operation*> inputs;
};
