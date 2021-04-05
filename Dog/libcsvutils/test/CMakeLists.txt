#find_package(CSVUtils REQUIRED)
#target_link_libraries(demo CSVUtils::CSVUtils)
message("test module")

add_executable(demo test_csv.cpp ${CMAKE_SOURCE_DIR}/src/csv_utils.cpp)
target_include_directories(demo 
	PUBLIC ${CMAKE_SOURCE_DIR}/include
	PRIVATE ${CMAKE_SOURCE_DIR}/src
	)

#message(${CMAKE_CURRENT_SOURCE_DIR})
#message(${CMAKE_SOURCE_DIR})



