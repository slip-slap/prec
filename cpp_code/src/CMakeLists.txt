find_package(SFML 2 COMPONENTS graphics audio REQUIRED)

#find_package(boost REQUIRED)

find_package(Boost 1.72.0 COMPONENTS locale random chrono REQUIRED)
find_package(CSVUtils REQUIRED)
#message(${Boost_LIBRARIES})
#message(${Boost_INCLUDE_DIRS})

add_executable(demo main.cpp)
target_include_directories(demo PUBLIC "${PROJECT_BINARY_DIR}")
target_include_directories(demo PUBLIC "${Boost_INCLUDE_DIR}")
target_include_directories(demo PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}")

message("cmake include path: " ${Boost_INCLUDE_DIR})
message("cmake include path: " ${CMAKE_CURRENT_SOURCE_DIR})
#target_link_libraries(demo ${Boost_LIBRARIES})

target_link_libraries(demo Boost::locale Boost::random)
target_link_libraries(demo CSVUtils::CSVUtils)
target_link_libraries(demo sfml-graphics sfml-audio)


