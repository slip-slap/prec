#include "stocknode.h"
#include <list>
#include <map>
#include <string>

#ifndef STOCK_NODE_HEADER
#define STOCK_NODE_HEADER 10
class Stock{
	public:
		Stock();
		~Stock();
		void addStockNode(StockNode& node);
        void readStocks(std::string path);
        std::list<StockNode>& getStock();
        std::list<StockNode>& getStock(const std::string &stock_name);
        std::list<std::string>& getListedCompany();

	private:
        std::list<StockNode> m_stock;
        std::map<std::string, std::list<StockNode>> m_all_stock;
        std::list<std::string> m_listed_company;

};
#endif
