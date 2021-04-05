cmake_minimum_required(VERSION 3.5)

project(Dog LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_INSTALL_PREFIX /Users/kismet/Desktop/temp_install)

add_library(CSVUtils ./src/csv_utils.cpp)

target_compile_options(CSVUtils PRIVATE -Werror)

target_include_directories(CSVUtils 
	PUBLIC
		$<INSTALL_INTERFACE:include>
		$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
	PRIVATE
		${CMAKE_CURRENT_SOURCE_DIR}/src
)

install(TARGETS CSVUtils
	EXPORT CSVUtils-export
	LIBRARY DESTINATION lib
	ARCHIVE DESTINATION lib
	)
install(EXPORT CSVUtils-export
	FILE CSVUtilsTargets.cmake
	NAMESPACE CSVUtils::
	DESTINATION lib/cmake/csv_utils
	)

install(
	FILES ${CMAKE_CURRENT_SOURCE_DIR}/include/csv_utils.h
	DESTINATION "include/csv_utils"
	)

install(
	FILES ${CMAKE_CURRENT_SOURCE_DIR}/cmake/CSVUtilsConfig.cmake
	DESTINATION "lib/cmake/csv_utils"
)	


add_subdirectory(test)

#message(${CMAKE_CURRENT_SOURCE_DIR})
#message(${CMAKE_SOURCE_DIR})
