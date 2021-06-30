#pragma once

#include <vector>
#include <iostream>

class Operation{
	public: 
		virtual float forward() = 0; 
		virtual float backward() = 0; 
};
