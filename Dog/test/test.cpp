#include "gtest/gtest.h"

int get(){return 4;}
TEST(a, b){
	ASSERT_EQ(4, get());
}

/*
int main(int argc, char **argv){

	return RUN_ALL_TESTS();
}
*/


