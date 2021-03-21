set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

find_package(QT NAMES Qt6 Qt5 COMPONENTS Core Widgets PrintSupport REQUIRED)
find_package(Qt${QT_VERSION_MAJOR} COMPONENTS Core Widgets PrintSupport REQUIRED)
if(Qt5_FOUND)
	#	message("qt found")
endif(Qt5_FOUND)


FILE(GLOB_RECURSE PROJECT_SOURCES
	"${CMAKE_SOURCE_DIR}/src/*.cpp"
	"${CMAKE_SOURCE_DIR}/src/*.h"
	"${CMAKE_SOURCE_DIR}/src/*.ui"
	)


if(${QT_VERSION_MAJOR} GREATER_EQUAL 6)
    qt_add_executable(Dog
        ${PROJECT_SOURCES}
    )
else()
    if(ANDROID)
        add_library(Dog SHARED
            ${PROJECT_SOURCES}
        )
    else()
        add_executable(Dog
            ${PROJECT_SOURCES}
        )
    endif()
endif()

#find_package(Qt5)


target_include_directories(Dog PUBLIC "${PROJECT_BINARY_DIR}")
target_link_libraries(Dog PRIVATE Qt${QT_VERSION_MAJOR}::Widgets Qt${QT_VERSION_MAJOR}::PrintSupport Qt${QT_VERSION_MAJOR}::Core)
