#include <fstream>
#include <vector>
#include "stock.h"

Stock::Stock(){
}
Stock::~Stock(){
}

void Stock::addStockNode(StockNode &node){
    m_stock.push_back(node);
}

std::list<StockNode>& Stock::getStock(const std::string& stock_code){
     return m_all_stock.find(stock_code)->second;
}

std::list<StockNode>& Stock::getStock(){
    return m_stock;
}

std::list<std::string>& Stock::getListedCompany(){

	std::string root_folder = "/Users/kismet/Documents/github/prec/Dog/data/data/stock/company_information/SSE_listed_company_info.csv";
    if(m_listed_company.size() == 0){
        std::fstream file(root_folder);
        std::string line;
          std::ifstream myfile (root_folder);
          if (myfile.is_open())
          {
            while ( getline (myfile,line) )
            {
              //std::cout << line << '\n';
			  for (int i=0;i<line.size();i++){
				  if(line[i] == ','){
					std::string field1 = line.substr(0,i-3);
					m_listed_company.push_back(field1);
					break;
				  }
			  }
            }
            myfile.close();
          }
          else std::cout << "Unable to open file"<<std::endl;;
    }
    return m_listed_company;
}

std::vector<std::vector<std::string>> readCsv(std::string file_name){
	    std::vector<std::vector<std::string>> file_result;
        std::fstream file(file_name);
        std::string line;
          std::ifstream myfile (file_name);
          if (myfile.is_open())
          {
			std::cout<<"**open file**"<<std::endl;
            while ( getline (myfile,line) )
            {
			  int pos1 = 0;
              int pos2 = 0; 
			  std::vector<std::string> line_result;
			  for (int i=0;i<line.size();i++){
				  if(line[i] == ','){
					pos2 = i;
					std::string field1 = line.substr(pos1,pos2-pos1);
					pos1 = pos2+1;
					//push field
					line_result.push_back(field1);
				  }
			  }
			  // push line code
			  file_result.push_back(line_result);
            }
            myfile.close();
          }
          else std::cout << "Unable to open file"<<std::endl;;
		  return file_result;
}
void Stock::readStocks(std::string path){
		std::string root_folder = "/Users/kismet/Documents/github/prec/Dog/data/data/stock/stock_history_data/";

		for(std::list<std::string>::iterator itr = m_listed_company.begin();itr !=m_listed_company.end();itr++){
			if(itr == m_listed_company.begin()){itr++;}
			std::string path_to_file = root_folder;
			std::string stock_code = *itr;
			path_to_file.append(stock_code);
			path_to_file.append(".csv");
			//std::cout<<path_to_file<<std::endl;
			std::vector<std::vector<std::string>> file_result = readCsv(path_to_file);
			std::list<StockNode> stock_node_result;
			for(int i=0; i<file_result.size();i++){
				if(i==0){i++;}
				std::vector<std::string> line_result = file_result[i];
				StockNode s;
				for(int m = 0; m< line_result.size();m++){
					s.setOpenPrice(std::stod(line_result[1]));
				}
				stock_node_result.push_back(s);
			}
			std::map<std::string, std::list<StockNode>>::iterator itr_map = m_all_stock.begin();
			m_all_stock.insert(itr_map, std::pair<std::string, std::list<StockNode>>(stock_code, stock_node_result));
		}
}

