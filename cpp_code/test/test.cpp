//#include "gtest/gtest.h"
//#include <boost/test/unit_test.hpp>
//#define BOOST_TEST_MAIN test 
/*
int get(){return 4;}
TEST(a, b){
	ASSERT_EQ(4, get());
}
*/
/*
int main(int argc, char **argv){

	return RUN_ALL_TESTS();
}

int add(int a, int b){return a+b;}

BOOST_AUTO_TEST_CASE(FailTest)
{
    BOOST_CHECK_EQUAL(5, add(2,3));
}

*/

#include "gtest/gtest.h"

int add(int a, int b){return a+b;}
TEST(SquareRootTest, PositiveNos) { 
    EXPECT_EQ (1, add(1,0));
    EXPECT_EQ (25, add(5, 20));
    EXPECT_EQ (6, add(3,3));
}


int main() {
  ::testing::InitGoogleTest();
  return RUN_ALL_TESTS();
}


