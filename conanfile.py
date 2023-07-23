from conans import ConanFile, CMake


class AtfMsgsConan(ConanFile):
    name = "pam-core"
    version = "1.0.0"
    license = "<Put the package license here>"
    author = "gordonu@flutterint.com"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "PAM core static library"
    topics = ("plib", "c++", "core", "platform")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"
    exports_sources = "src/protocols/*", "src/coreserver/srvshared/*", "CMakeLists.txt"
    requires = [
        "pokerstars-plib/[~1.0.0]",
        "pokerstars-commlib/2.2.0",
         "openssl/3.1.1",

        "fmt/9.1.0"
        ]

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="src")
       # self.copy("*.cpp", dst="include/coreserver/srvshared/dbm", src="src/coreserver/srvshared/dbm")
       # self.copy("*.cpp", dst="include/coreserver/srvshared/LoginDbm", src="src/coreserver/srvshared/LoginDbm")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["pam-core"]
        self.cpp_info.includedirs = ["include/protocols", "include/coreserver/srvshared" ]
