add_test( a.b /Users/kismet/Documents/github/prec/Dog/build/test/test [==[--gtest_filter=a.b]==] --gtest_also_run_disabled_tests)
set_tests_properties( a.b PROPERTIES WORKING_DIRECTORY /Users/kismet/Documents/github/prec/Dog/build/test)
add_test( aa.bb /Users/kismet/Documents/github/prec/Dog/build/test/test [==[--gtest_filter=aa.bb]==] --gtest_also_run_disabled_tests)
set_tests_properties( aa.bb PROPERTIES WORKING_DIRECTORY /Users/kismet/Documents/github/prec/Dog/build/test)
set( test_TESTS a.b aa.bb)