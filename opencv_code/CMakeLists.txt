cmake_minimum_required(VERSION 3.10)

project(foo VERSION 1.0)

set(CMAKE_CXX_STANDARD 11)

message(${CMAKE_HOST_SYSTEM})


find_package(Boost 1.72.0 COMPONENTS locale)
find_package( OpenCV REQUIRED )



message(${CMAKE_CURRENT_SOURCE_DIR})
include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable(opengl main.cpp)
target_link_libraries(opengl ${OpenCV_LIBS}) # ${OPENGL_gl_LIBRARY})







#find_library(BOOST_LIBRARY 
#	NAMES libboost_locale-mt.a
#	PATHS /usr/local/Cellar/boost/1.72.0_3/lib)
#find_path(BOOST_INCLUDES 
#	  	 boost/locale.hpp 
#		 boost/algorithm/string/case_conv.hpp
#		 /usr/local/Cellar/boost/1.72.0_3/include)
