message("welcome to my cmake module")
find_package(PkgConfig)
pkg_check_modules(Opencv4 REQUIRED Opencv4)


message("pkg: " ${OGG_LINK_LIBRARIES})
message("pkg: " ${OGG_INCLUDE_DIRS})



