cmake_minimum_required(VERSION 3.12)

project(pamcore-Test
        VERSION 0.1.0
        DESCRIPTION "pam-core - tester"
        HOMEPAGE_URL ""
        LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_executable(${PROJECT_NAME}  example.cpp)

#target_include_directories(example 
#    PRIVATE ${CONAN_INCLUDE_DIRS}
#)
                                           
target_link_libraries(${PROJECT_NAME}
    PRIVATE CONAN_PKG::pokerstars-plib
    PRIVATE CONAN_PKG::pokerstars-commlib
    PRIVATE CONAN_PKG::pam-core
 )

message(STATUS "Include directories: ${CONAN_INCLUDE_DIRS}")

 set(PASSERTLVL $<IF:$<CONFIG:Debug>,5,4>)
 set(PTRACELVL $<IF:$<CONFIG:Debug>,5,3>)
 
 add_compile_definitions(
    LINUX
    PPOSIX
    __STDC_LIMIT_MACROS
    __STDC_CONSTANT_MACROS
    PASSERTLVL=${PASSERTLVL}
    PTRACELVL=${PTRACELVL}
)

# CTest is a testing tool that can be used to test your project.
# enable_testing()
# add_test(NAME example
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND example)
