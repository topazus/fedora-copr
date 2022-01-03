%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname intel-igc
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        An LLVM based compiler for OpenCL™ targeting Intel Gen graphics hardware architecture.
License:        Intel
URL:            https://github.com/intel/intel-graphics-compiler
Source0:        https://github.com/intel/intel-graphics-compiler/archive/%{igc_commit}/igc-%{version}.tar.gz

BuildRequires: gcc-c++ cmake pkg-config
BuildRequires: flex bison git

%description
The Intel® Graphics Compiler for OpenCL™ is an LLVM based compiler for OpenCL™ targeting Intel Gen graphics hardware architecture.

%prep
%autosetup -n %{appname}-master -p1

git clone -b release/10.x https://github.com/llvm/llvm-project llvm-project

pushd llvm-project/llvm/projects

git clone -b ocl-open-100 https://github.com/intel/opencl-clang opencl-clang
git clone -b llvm_release_100 https://github.com/KhronosGroup/SPIRV-LLVM-Translator llvm-project/llvm/projects/llvm-spirv
popd

git clone https://github.com/intel/intel-graphics-compiler igc

git clone https://github.com/intel/vc-intrinsics vc-intrinsics

git config --global user.email "topazus@outlook.com"
git config --global user.name "Felix Wang"

%build
mkdir build
pushd build

%cmake
%cmake_build
popd

%install
cd build
%cmake_install

%check


%files
%license LICENSE*
%doc README.md


%changelog
