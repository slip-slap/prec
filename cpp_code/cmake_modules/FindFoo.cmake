# the `pkg_check_modules` function is created with this call
find_package(PkgConfig REQUIRED)
message("pkgconfig found: " ${PKG_CONFIG_FOUND})
message("pkgconfig version: " ${PKG_CONFIG_VERSION_STRING})
pkg_check_modules(Opencv4 REQUIRED Opencv4)

set(FOO_LIBRARY "haha")




