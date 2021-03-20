
find_package(SFML 2 COMPONENTS graphics audio REQUIRED)

add_executable(demo main.cpp)
target_include_directories(demo PUBLIC "${PROJECT_BINARY_DIR}")
target_link_libraries(demo ${Boost_LIBRARIES})
target_link_libraries(demo sfml-graphics sfml-audio)


