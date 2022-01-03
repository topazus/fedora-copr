
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname zig
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        General-purpose programming language and toolchain for maintaining robust, optimal, and reusable software
License:        MIT
URL:            https://github.com/ziglang/zig
Source:         https://github.com/ziglang/zig/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-c++ cmake pkg-config
BuildRequires: clang lld llvm-libs clang-devel llvm-devel lld-devel


%description
A general-purpose programming language and toolchain for maintaining robust, optimal, and reusable software.

%prep
%autosetup -n %{appname}-master -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
    -DZIG_PREFER_CLANG_CPP_DYLIB=true
%cmake_build

%install
%cmake_install


%if %{with check}
%check
%ctest
%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}

%changelog
