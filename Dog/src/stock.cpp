#include "stock.h"
#include <QFile>
#include <QDebug>

Stock::Stock(){
}
Stock::~Stock(){
}

void Stock::addStockNode(StockNode &node){
    m_stock.push_back(node);
}

QList<StockNode>& Stock::getStock(const QString& stock_code){
    return *m_all_stock.find(stock_code);
}

QList<StockNode>& Stock::getStock(){
    return m_stock;
}

QList<QString>& Stock::getListedCompany(){

    QString file_name = "SSE_listed_company_info.csv";
    if(m_listed_company.size() == 0){
        QFile file(file_name);
        if (!file.open(QIODevice::ReadOnly)) {
                qDebug() << file.errorString();
            }
        while(!file.atEnd()){
            QByteArray line = file.readLine();
            QString first_item = QString(line.split(',').first());
            m_listed_company.push_back(first_item);
        }
    }
    return m_listed_company;
}

void Stock::readStocks(QString path){
        QString file_name = "000031.csv";
        QFile file(file_name);
        if (!file.open(QIODevice::ReadOnly)) {
                std::cout<<"wrong read"<<std::endl;
            }
        while(!file.atEnd()){
            QByteArray line = file.readLine();
            QList<QByteArray> line_list = line.split(',');
            int counter=0;
            for(QList<QByteArray>::iterator itr=line_list.begin(); itr!=line_list.end();itr++, counter++){
                StockNode s;
                if(counter == 1){
                    s.setOpenPrice((*itr).toDouble());
                }
                if(counter == 2){
                    s.setHighPrice((*itr).toDouble());
                }
                if(counter == 3){
                    s.setLowPrice((*itr).toDouble());
                }
                std::cout<<s<<std::endl;
				addStockNode(s);
            }
        }
}
