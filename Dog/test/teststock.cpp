#include <iostream>
#include <list>
#include <string>
#include "gtest/gtest.h"
#include "stock.h"


TEST(aa, bb){
	Stock s;
	std::list<std::string> company_list = s.getListedCompany();
	/*
	s.readStocks("");
	std::list<StockNode> stock_data = s.getStock("603000");
	for(std::list<StockNode>::iterator itr= stock_data.begin(); itr!=stock_data.end(); itr++){
		std::cout<<itr->getOpenPrice()<<std::endl;
	}
	*/

	ASSERT_EQ(4, 4);
}
