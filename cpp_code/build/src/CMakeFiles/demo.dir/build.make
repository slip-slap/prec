# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.17

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /opt/local/bin/cmake

# The command to remove a file.
RM = /opt/local/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/kismet/Documents/github/prec/cpp_code

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/kismet/Documents/github/prec/cpp_code/build

# Include any dependencies generated for this target.
include src/CMakeFiles/demo.dir/depend.make

# Include the progress variables for this target.
include src/CMakeFiles/demo.dir/progress.make

# Include the compile flags for this target's objects.
include src/CMakeFiles/demo.dir/flags.make

src/CMakeFiles/demo.dir/main.cpp.o: src/CMakeFiles/demo.dir/flags.make
src/CMakeFiles/demo.dir/main.cpp.o: ../src/main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/kismet/Documents/github/prec/cpp_code/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/CMakeFiles/demo.dir/main.cpp.o"
	cd /Users/kismet/Documents/github/prec/cpp_code/build/src && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/demo.dir/main.cpp.o -c /Users/kismet/Documents/github/prec/cpp_code/src/main.cpp

src/CMakeFiles/demo.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/demo.dir/main.cpp.i"
	cd /Users/kismet/Documents/github/prec/cpp_code/build/src && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/kismet/Documents/github/prec/cpp_code/src/main.cpp > CMakeFiles/demo.dir/main.cpp.i

src/CMakeFiles/demo.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/demo.dir/main.cpp.s"
	cd /Users/kismet/Documents/github/prec/cpp_code/build/src && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/kismet/Documents/github/prec/cpp_code/src/main.cpp -o CMakeFiles/demo.dir/main.cpp.s

# Object files for target demo
demo_OBJECTS = \
"CMakeFiles/demo.dir/main.cpp.o"

# External object files for target demo
demo_EXTERNAL_OBJECTS =

src/demo: src/CMakeFiles/demo.dir/main.cpp.o
src/demo: src/CMakeFiles/demo.dir/build.make
src/demo: /usr/local/lib/libboost_locale-mt.dylib
src/demo: /usr/local/lib/libboost_random-mt.dylib
src/demo: /Users/kismet/Desktop/temp_install/lib/libCSVUtils.a
src/demo: /usr/local/lib/libsfml-graphics.2.5.1.dylib
src/demo: /usr/local/lib/libsfml-audio.2.5.1.dylib
src/demo: /usr/local/lib/libboost_chrono-mt.dylib
src/demo: /usr/local/lib/libboost_system-mt.dylib
src/demo: /usr/local/lib/libboost_thread-mt.dylib
src/demo: /usr/local/lib/libsfml-window.2.5.1.dylib
src/demo: /usr/local/lib/libsfml-system.2.5.1.dylib
src/demo: src/CMakeFiles/demo.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/kismet/Documents/github/prec/cpp_code/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable demo"
	cd /Users/kismet/Documents/github/prec/cpp_code/build/src && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/demo.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/CMakeFiles/demo.dir/build: src/demo

.PHONY : src/CMakeFiles/demo.dir/build

src/CMakeFiles/demo.dir/clean:
	cd /Users/kismet/Documents/github/prec/cpp_code/build/src && $(CMAKE_COMMAND) -P CMakeFiles/demo.dir/cmake_clean.cmake
.PHONY : src/CMakeFiles/demo.dir/clean

src/CMakeFiles/demo.dir/depend:
	cd /Users/kismet/Documents/github/prec/cpp_code/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/kismet/Documents/github/prec/cpp_code /Users/kismet/Documents/github/prec/cpp_code/src /Users/kismet/Documents/github/prec/cpp_code/build /Users/kismet/Documents/github/prec/cpp_code/build/src /Users/kismet/Documents/github/prec/cpp_code/build/src/CMakeFiles/demo.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/CMakeFiles/demo.dir/depend

