#include "stocknode.h"
#include <QList>
#include <QMap>
#include <QString>

#ifndef STOCK_NODE_HEADER
#define STOCK_NODE_HEADER 10
class Stock{
	public:
		Stock();
		~Stock();
		void addStockNode(StockNode& node);
        void readStocks(QString path);
        QList<StockNode>& getStock();
        QList <StockNode>& getStock(const QString &stock_name);
        QList<QString>& getListedCompany();

	private:
        QList<StockNode> m_stock;
        QMap<QString, QList<StockNode>> m_all_stock;
        QList<QString> m_listed_company;

};
#endif
