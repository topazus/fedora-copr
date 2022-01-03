%global debug_package %{nil}
%global build_number 212.5080.54

Name:           clion
Version:        2021.2.1
Release:        1%{?dist}
Summary:        A cross-platform IDE for C and C++
License:        custom
URL:            https://www.jetbrains.com/clion/
Source0:        https://download.jetbrains.com/cpp/CLion-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/topazus/fedora-copr/main/clion/clion.desktop


BuildRequires:  pkg-config desktop-file-utils

%description
A cross-platform IDE for C and C++.

%prep
%autosetup -n clion-%{version} -p1

# Replace python shebangs to make them compatible with fedora
find -type f -name "*.py" -exec sed -e 's|/usr/bin/env python|%{__python3}|g' \
                                    -i "{}" \;

find -type f -name "*.sh" -exec sed -e 's|/bin/sh|/usr/bin/sh|g' \
                                    -i "{}" \;

# Remove files for other CPU architectures
rm -rf lib/pty4j-native/linux/aarch64
rm -rf lib/pty4j-native/linux/arm
rm -rf lib/pty4j-native/linux/mips64el
rm -rf lib/pty4j-native/linux/ppc64le

# Remove files for other OS
rm -rf plugins/cwm-plugin/quiche-native/darwin-aarch64
rm -rf plugins/cwm-plugin/quiche-native/darwin-x86-64
rm -rf plugins/cwm-plugin/quiche-native/win32-x86-64

# remove bundled jre
rm -rf jbr

%build

%install
mkdir -p %{buildroot}/opt/%{name}
cp -a * %{buildroot}/opt/%{name}

install -pDm644 bin/clion.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -pDm644 bin/clion.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

install -pDm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%dir /opt/%{name}
/opt/%{name}/*

%changelog
