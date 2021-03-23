#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <list>
#include <string>
#include <QMessageBox>
#include <QDebug>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->menubar->setNativeMenuBar(false);// display menubar
    std::list<std::string> listed_company = s.getListedCompany();
    //s.readStocks("");
    for(std::list<std::string>::iterator itr=listed_company.begin();itr!=listed_company.end();itr++){
         ui->listWidget->addItem(itr->c_str());
    }
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_pushButton_clicked()
{
    qDebug()<<"something";
    QMessageBox::about(this, "title","this is");

}

void MainWindow::plotData(std::string stock_code){
    std::list<StockNode> stock_data = s.getStock(stock_code);

    int const size = stock_data.size();
    QVector<double> y(2);
    double max_price = -1;
    for(std::list<StockNode>::iterator itr=stock_data.begin();itr!=stock_data.end();itr++){
        y.push_back(itr->getOpenPrice());
        if(itr->getOpenPrice() > max_price){max_price = itr->getOpenPrice();}
        qDebug()<<"price is: "<<itr->getOpenPrice();
    }
    QVector<double> x(y.size());
    for(int i=0;i<y.size();i++){
        x[i] = i;
    }
    ui->customPlot->addGraph();
    ui->customPlot->graph(0)->setData(x,y);
    ui->customPlot->xAxis->setRange(0,size);
    ui->customPlot->yAxis->setRange(0,int(max_price));
    ui->customPlot->replot();

}

void MainWindow::on_listWidget_itemClicked(QListWidgetItem *item)
{
    plotData(item->text().toStdString());
}

void MainWindow::on_actionOpen_triggered()
{
    QMessageBox::information(this,"","");
}
