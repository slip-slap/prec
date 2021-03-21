#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <QDebug>
#include "stock.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QString file_name = "SSE_listed_company_info.csv";
    QFile file(file_name);
    if (!file.open(QIODevice::ReadOnly)) {
            qDebug() << file.errorString();
        }
    while(!file.atEnd()){
        QByteArray line = file.readLine();
        QString first_item = QString(line.split(',').first());
        ui->listWidget->addItem(first_item);
    }
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_pushButton_clicked()
{
    qDebug()<<"something";
    plotData();

}

void MainWindow::plotData(){

    QList<StockNode> stock = s.getStock();
    int const size = stock.size();
    QVector<double> y(2);
    for(QList<StockNode>::iterator itr=stock.begin();itr!=stock.end();itr++){
        y.push_back(itr->getOpenPrice());
        qDebug()<<"price is: "<<itr->getOpenPrice();
    }
    QVector<double> x(y.size());
    for(int i=0;i<y.size();i++){
        x[i] = i;
    }
    ui->customPlot->addGraph();
    ui->customPlot->graph(0)->setData(x,y);
    ui->customPlot->xAxis->setRange(0,size);
    ui->customPlot->yAxis->setRange(0,10);
    ui->customPlot->replot();
}

void MainWindow::on_listWidget_itemClicked(QListWidgetItem *item)
{
    qDebug()<<item->text();
    s.readStocks("");
    plotData();	
}
