cmake_minimum_required(VERSION 3.23)
project(PackageTest)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(KEEP_RPATHS)

set(CMAKE_C_COMPILER ${CONAN_BIN_DIRS_LLVM}/clang)
set(CMAKE_OSX_DEPLOYMENT_TARGET 10.12)
set(CMAKE_OSX_SYSROOT ${CONAN_MACOS-SDK_ROOT})

add_executable(test_package test_package.c)
target_link_libraries(test_package ${CONAN_LIBS})
