get_directory_property(hasParent PARENT_DIRECTORY)

#[[
if(hasParent)
  message(STATUS "Has a parent scope.")
else()
  message(STATUS "Doesn't have a parent scope.")
endif()
]]

set (SOURCE_CPP 
	"${CMAKE_SOURCE_DIR}/src/stock.cpp"
	"${CMAKE_SOURCE_DIR}/src/stocknode.cpp"
        test.cpp
        teststock.cpp
	)

find_package(GTest REQUIRED)

include_directories(${GTEST_INCLUDE_DIRS})

add_executable(test ${SOURCE_CPP})
target_link_libraries(test ${GTEST_BOTH_LIBRARIES} pthread)


gtest_discover_tests(test)
