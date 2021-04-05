#include "csv_utils.h"
#include "internal.h"
#include <iostream>
#include "fstream"

std::list<std::string> SplitLineByDelimiter(std::string line, std::string separator){
	if(line.size() == 0){std::cout<<"line is empty";}
	if(line.size() != 1 ){std::cout<<"field separator is illegal";}
	std::list<std::string> lineField;
	int pos1 = 0;
	int pos2 = 0;
  	for (int i=0;i<line.size();i++){
	  	if(line[i] == ','){
			pos2 = i;
			std::string field1 = line.substr(pos1,pos2-pos1);
			pos1 = pos2+1;
			//push field
			lineField.push_back(field1);
	  	}
	}
	return lineField;
}

CSVReader::CSVReader(std::string file_Path, std::string file_Name){
	m_File_Path = file_Path;
	m_File_Name = file_Name;
}
CSVReader::CSVReader(const CSVReader & another){
	std::cout<<"this is copy constructor"<<std::endl;
}

CSVReader::~CSVReader(){
	std::cout<<"destroy an object"<<std::endl;
}

std::list<std::list<std::string>>& CSVReader::GetFile(){
	// if the m_File hasn't been created 
	if(m_File.size() == 0){
		std::ifstream in(m_File_Name.append(m_File_Name));
		// read a line and encapulate into a std::list<std::string>
		std::string line;
		if(in.is_open()){
			while(getline(in, line)){
				std::list<std::string> lineField = SplitLineByDelimiter(line,m_Field_Separator);
				m_File.push_back(lineField);
			}
		}
        else std::cout << "Unable to open file"<<std::endl;;
	}
	return m_File;
}



