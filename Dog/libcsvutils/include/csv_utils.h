#include <string>
#include <list>
class CSVReader{
	public:
		CSVReader(std::string file_Path,std::string file_Name);
		CSVReader(const CSVReader & another);
		std::list<std::list<std::string>>& GetFile();
		~CSVReader();
	private:
		std::list<std::list<std::string>> m_File;
		std::string m_File_Path;
		std::string m_File_Name;
		std::string m_Field_Separator;
};
