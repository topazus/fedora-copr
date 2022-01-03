Name:     miktex
Version:  21.3
Release:  1%{?dist}
Summary:  Modern C/C++ implementation of TeX & Friends for Windows, macOS and Linux
License:  GNU
URL:      https://github.com/MiKTeX/miktex
Source0:  %{url}/archive/%{version}/miktex-%{version}.tar.gz

BuildRequires: gcc-g++
BuildRequires: cmake
BuildRequires: gcc-g++

BuildRequires: apr-devel
BuildRequires: apr-util-devel
BuildRequires: bzip2-devel
BuildRequires: cairo-devel
BuildRequires: expat-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: fribidi-devel
BuildRequires: gd-devel
BuildRequires: gmp-devel
BuildRequires: graphite2-devel
BuildRequires: harfbuzz-devel
BuildRequires: harfbuzz-icu
BuildRequires: hunspell-devel
BuildRequires: icu
#BuildRequires: jpeg-devel
BuildRequires: log4cxx-devel
BuildRequires: lzma-sdk-devel
BuildRequires: mpfr-devel
BuildRequires: libmspack-devel
BuildRequires: openssl-devel
BuildRequires: pixman-devel
BuildRequires: libpng-devel
BuildRequires: poppler-devel
BuildRequires: popt-devel
BuildRequires: potrace-devel
BuildRequires: uriparser-devel
BuildRequires: zziplib-devel
BuildRequires: poppler-qt5

BuildRequires: bison flex
BuildRequires: qt5-qtbase-devel qt5-qtscript-devel qt5-qttools-devel qt5-qttools-static

BuildRequires: libxslt
BuildRequires: libcurl-devel
BuildRequires: boost-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-qttools

%description
MiKTeX is a modern C/C++ implementation of TeX & Friends for Windows, macOS and Linux.

%prep
%autosetup -n miktex-%{version} -p1

%build
%cmake \
  -DCMAKE_INSTALL_PREFIX=/opt/miktex \
  -DWITH_UI_QT=ON

%cmake_build %{?_smp_mflags}

%install
%cmake_install
install -Dm644 opt/miktex/share/applications/miktex-console.desktop usr/share/applications/miktex-console.desktop
sed -i 's/^Exec=miktex-console$/Exec=\/opt\/miktex\/bin\/miktex-console/' usr/share/applications/miktex-console.desktop
cp -R opt/miktex/share/applications/icons usr/share/

mv opt/miktex/man usr/share/man

%file
/opt/miktex/*
%{_datadir}/applications/miktex-console.desktop

%changelog
