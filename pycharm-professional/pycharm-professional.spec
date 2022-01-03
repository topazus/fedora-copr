%global debug_package %{nil}

Name:           pycharm-professional
Version:        2021.2.1
Release:        1%{?dist}
Summary:        The Python IDE for Professional Developers
License:        custom
URL:            https://www.jetbrains.com/pycharm/
Source0:        https://download.jetbrains.com/python/pycharm-professional-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/topazus/fedora-copr/main/pycharm-professional/pycharm-professional.desktop

BuildRequires: pkg-config desktop-file-utils

%description
The Python IDE for Professional Developers.

%prep
%autosetup -n pycharm-%{version} -p1

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

rm -rf **/*.dll
rm -rf **/*.dylib

# remove bundled jre
rm -rf jbr

%build

%install
mkdir -p %{buildroot}/opt/%{name}
cp -a * %{buildroot}/opt/%{name}

install -pDm644 bin/pycharm.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -pDm644 bin/pycharm.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

install -pDm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
if [ "$1" = 1 ]; then
  if [ ! -f %{_sysconfdir}/profile.d/jetbrains-jre.sh ] ; then
    echo "export PYCHARM_JDK=/usr/lib/jvm/jetbrains-jre" > %{_sysconfdir}/profile.d/jetbrains-jre.sh
  else
    grep -q "^export PYCHARM_JDK=/usr/lib/jvm/jetbrains-jre$" %{_sysconfdir}/profile.d/jetbrains-jre.sh || echo "export PYCHARM_JDK=/usr/lib/jvm/jetbrains-jre" >> %{_sysconfdir}/profile.d/jetbrains-jre.sh
fi

%postun
if [ "$1" = 0 ] && [ -f %{_sysconfdir}/profile.d/jetbrains-jre.sh ] ; then
  sed -i '\!^export PYCHARM_JDK=/usr/lib/jvm/jetbrains-jre!d' %{_sysconfdir}/profile.d/jetbrains-jre.sh
fi

%files
%dir /opt/%{name}
/opt/%{name}/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop

%changelog
