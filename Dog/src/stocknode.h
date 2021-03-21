#include <iostream>
#include <string>
#include <QList>

#ifndef STOCK_HEADER
#define STOCK_HEADER 20
class StockNode{
    private:
        std::string m_date;
        double m_open_price;
        double m_high_price;
        double m_low_price;
		
    public:
        StockNode();
		StockNode(const StockNode &node);
        double getOpenPrice() const;
        double getHighPrice() const;
        double getClosePrice() const;
        void setOpenPrice(double);
        void setHighPrice(double);
        void setLowPrice(double);

    friend std::ostream& operator<<(std::ostream& out, const StockNode& node){
            out<<"open price: "<<node.m_open_price<<", high price: "<<node.m_high_price
              << " ,low price: "<<node.m_low_price;
            return out;
    }
};
#endif
