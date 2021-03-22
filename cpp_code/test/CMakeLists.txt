find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})

add_executable(testa test.cpp)
target_link_libraries(testa ${GTEST_BOTH_LIBRARIES} pthread)

##gtest_discover_tests(testa)
enable_testing()
add_test(me testa)

#find_package (Boost COMPONENTS system filesystem unit_test_framework REQUIRED)
#include_directories (
#                     ${Boost_INCLUDE_DIRS}
#                     )
#add_definitions (-DBOOST_TEST_DYN_LINK)
#add_executable (Test test.cpp)
#target_link_libraries (Test
#                       ${Boost_FILESYSTEM_LIBRARY}
#                       ${Boost_SYSTEM_LIBRARY}
#                       ${Boost_UNIT_TEST_FRAMEWORK_LIBRARY}
#                       )

#enable_testing()
#add_test(me Test)

