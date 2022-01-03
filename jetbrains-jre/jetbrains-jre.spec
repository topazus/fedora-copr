%global debug_package %{nil}
%global __brp_check_rpaths %{nil}

Name:           jetbrains-jre
Version:        11.0.12
Release:        1%{?dist}
Summary:        Runtime environment based on OpenJDK for running IntelliJ Platform-based products on Windows, macOS, and Linux
License:        GPL
URL:            https://github.com/JetBrains/JetBrainsRuntime
Source:         https://cache-redirector.jetbrains.com/intellij-jbr/jbr_jcef-11_0_12-linux-x64-b1649.1.tar.gz

BuildRequires: pkg-config

%description
JetBrains Runtime is a fork of OpenJDK available for Windows, Mac OS X, and Linux. It includes a number enhancements in font rendering, HiDPI support, ligatures, performance improvements, and bugfixes.

%prep
%autosetup -n jbr -p1

%build


%install
mkdir -p %{buildroot}%{_prefix}/lib/jvm/jetbrains-jre
cp -a * %{buildroot}%{_prefix}/lib/jvm/jetbrains-jre

%check


%files
%dir %{_prefix}/lib/jvm/jetbrains-jre
%{_prefix}/lib/jvm/jetbrains-jre/*

%changelog
