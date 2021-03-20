cmake_minimum_required(VERSION 3.10)

project(foo VERSION 1.0)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Werror -std=c++14")
SET(CMAKE_CXX_FLAGS_DEBUG "-O0")
SET(CMAKE_C_FLAGS_DEBUG "-O0")
#message(${PROJECT_SOURCE_DIR})
#message(${CMAKE_CURRENT_BINARY_DIR})

list(APPEND CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake_modules/")
find_package(foo REQUIRED)

message("cmake module path: " ${CMAKE_MODULE_PATH})

message(${CMAKE_FIND_LIBRARY_PREFIXES})
message(${CMAKE_FIND_LIBRARY_SUFFIXES})
message("install prefix path: " ${CMAKE_INSTALL_PREFIX})
message("prefix path: " ${CMAKE_PREFIX_PATH})
message("library path: " ${CMAKE_LIBRARY_PATH})
message("module path: " ${CMAKE_MODULE_PATH})
message("system library path: " ${CMAKE_SYSTEM_LIBRARY_PATH})
message("include path: " ${CMAKE_INCLUDE_PATH})
message(":  " ${CMAKE_SYSTEM_PREFIX_PATH})

message("apple value: " ${APPLE})
message("apple value: " ${CMAKE_HOST_SYSTEM})
message("apple value: " ${CMAKE_HOST_SYSTEM_NAME})


message("binary path: " ${CMAKE_CURRENT_BINARY_DIR})
message("source dir: " ${CMAKE_CURRENT_SOURCE_DIR})

configure_file(ProjectConfig.h.in ProjectConfig.h)


#find_package(Boost 1.72.0 COMPONENTS locale REQUIRED)
#message(${Boost_LIBRARIES})
#message(${Boost_INCLUDE_DIRS})
#find_package(OpenCV)

find_package(Boost 1.72 CONFIG)
# Check for libray, if found print message, include dirs and link libraries.
if(Boost_FOUND)
    message("Boost Found")
    include_directories(${Boost_INCLUDE_DIRS})
	message(${Boost_INCLUDE_DIRS})
elseif(NOT Boost_FOUND)
    error("Boost Not Found")
endif()


#message(${CMAKE_CURRENT_SOURCE_DIR})
#message(${OpenCV_INCLUDE_DIRS})
#include_directories(${Boost_INCLUDES_DIRS})
#Jinclude_directories(${SFML_INCLUDES_DIRS})
include_directories(${SFML_INCLUDES_LIBRARIES})
message("include path: " ${CMAKE_INCLUDE_PATH})
#add_test(cmake_test ${EXECUTABLE_OUTPUT_PATH}/demo)

#find_package(GTest REQUIRED)
#include_directories(${GTEST_INCLUDE_DIRS})
#add_executable(test test.cpp)
#target_link_libraries(test ${GTEST_BOTH_LIBRARIES} pthread)
#gtest_discover_tests(test)

#ADD_SUBDIRECTORY(googletest)
#include_directories(${gtest_SOURCE_DIR}/include ${gtest_SOURCE_DIR})
#add_executable(test test.cpp)
#target_link_libraries(test gtest gtest_main)
#add_test(test test)
add_subdirectory(src)
add_subdirectory(test)





#find_library(BOOST_LIBRARY 
#	NAMES libboost_locale-mt.a
#	PATHS /usr/local/Cellar/boost/1.72.0_3/lib)
#find_path(BOOST_INCLUDES 
#	  	 boost/locale.hpp 
#		 boost/algorithm/string/case_conv.hpp
#		 /usr/local/Cellar/boost/1.72.0_3/include)
