#include "stocknode.h"
#include <iostream>

StockNode::StockNode(){
    //std::cout<<"create stock object"<<std::endl;
}

StockNode::StockNode(const StockNode &node){
	std::cout<<"copy constructor"<<std::endl;
	this->m_date = node.m_date;
	this->m_open_price = node.m_open_price;
	this->m_high_price = node.m_high_price;
	this->m_low_price = node.m_low_price;
}

double StockNode::getOpenPrice() const {
    return m_open_price;
}

double StockNode::getHighPrice() const {
    return m_high_price;
}

double StockNode::getClosePrice() const {
    return m_low_price;
}

void StockNode::setOpenPrice(double open_price){
    this->m_open_price = open_price;
}

void StockNode::setHighPrice(double high_price){
    this->m_high_price = high_price;
}

void StockNode::setLowPrice(double low_price){
    this->m_low_price = low_price;
}

