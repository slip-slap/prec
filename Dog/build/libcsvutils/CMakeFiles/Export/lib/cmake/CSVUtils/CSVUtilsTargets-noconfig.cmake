#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "CSVUtils::CSVUtils" for configuration ""
set_property(TARGET CSVUtils::CSVUtils APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(CSVUtils::CSVUtils PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_NOCONFIG "CXX"
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libCSVUtils.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS CSVUtils::CSVUtils )
list(APPEND _IMPORT_CHECK_FILES_FOR_CSVUtils::CSVUtils "${_IMPORT_PREFIX}/lib/libCSVUtils.a" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
