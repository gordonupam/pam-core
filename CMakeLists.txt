cmake_minimum_required(VERSION 3.12)

project(pam-core
        VERSION 1.0.0
        DESCRIPTION "pam-core static library"
        HOMEPAGE_URL ""
        LANGUAGES CXX
        )

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Let Conan do it's magic.
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

set(sources
    "src/protocols/sitemasks.cpp"
    "src/protocols/sglimits.cpp"
)

add_library(${PROJECT_NAME} )

target_include_directories(${PROJECT_NAME}
        PRIVATE src/protocols
        PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/generated
    )

target_sources( ${PROJECT_NAME}
            PRIVATE ${sources}
    )

target_link_libraries(${PROJECT_NAME} 
    PRIVATE CONAN_PKG::pokerstars-plib
    PRIVATE CONAN_PKG::pokerstars-commlib
    PRIVATE CONAN_PKG::fmt
)


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