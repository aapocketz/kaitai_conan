from conans import ConanFile, CMake, tools


class KaitaiStructCppStlConan(ConanFile):
    name = "kaitai-struct-cpp-stl"
    version = "0.9"
    license = "MIT"
    author = "Aaron Paquette <apaquette@syncopatedengr.com>"
    url = "https://github.com/aapocketz/kaitai_conan"
    description = "kaitai struct conan library"
    topics = ("parsers", "streams", "dsl")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        self.run("git clone --depth  1 --branch 0.9 https://github.com/kaitai-io/kaitai_struct_cpp_stl_runtime.git")
       

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="kaitai_struct_cpp_stl_runtime")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="kaitai_struct_cpp_stl_runtime")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["kaitai_struct_cpp_stl_runtime"]

