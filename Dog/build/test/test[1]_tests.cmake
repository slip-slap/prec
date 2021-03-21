add_test( a.b /Users/kismet/Desktop/temp/Dog/build/test/test [==[--gtest_filter=a.b]==] --gtest_also_run_disabled_tests)
set_tests_properties( a.b PROPERTIES WORKING_DIRECTORY /Users/kismet/Desktop/temp/Dog/build/test)
set( test_TESTS a.b)
