from conans import ConanFile, CMake, tools
import os
import platform

class WuQuantConan(ConanFile):
    name = 'wuquant'

    source_version = '2.0.0'
    package_version = '2'
    version = '%s-%s' % (source_version, package_version)

    build_requires = (
        'llvm/5.0.2-7@vuo+conan+llvm/stable',
        'macos-sdk/11.0-0@vuo+conan+macos-sdk/stable',
    )
    settings = 'os'
    url = 'https://www.ece.mcmaster.ca/~xwu/cq.c'
    license = 'Free to distribute'
    description = 'Wu\'s Color Quantizer'
    generators = 'cmake'
    build_dir = '_build'
    exports_sources = '*'

    def build(self):
        cmake = CMake(self)
        cmake.definitions['CMAKE_C_FLAGS'] = '-Oz'
        cmake.definitions['CMAKE_C_COMPILER'] = self.deps_cpp_info['llvm'].rootpath + '/bin/clang'
        if platform.system() == 'Darwin':
            cmake.definitions['CMAKE_OSX_ARCHITECTURES'] = 'x86_64;arm64'
            cmake.definitions['CMAKE_OSX_DEPLOYMENT_TARGET'] = '10.12'
            cmake.definitions['CMAKE_OSX_SYSROOT'] = self.deps_cpp_info['macos-sdk'].rootpath

        tools.mkdir(self.build_dir)
        with tools.chdir(self.build_dir):
            cmake.configure(source_dir='..', build_dir='.', args=[])
            cmake.build()

    def package(self):
        if platform.system() == 'Darwin':
            libext = 'dylib'
        elif platform.system() == 'Linux':
            libext = 'so'

        self.copy('*.h', dst='include')
        self.copy('libwuquant.%s' % libext, src=self.build_dir, dst='lib')
        self.copy('%s.txt' % self.name, dst='license')

    def package_info(self):
        self.cpp_info.libs = ['wuquant']
