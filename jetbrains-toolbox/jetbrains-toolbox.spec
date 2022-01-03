%global debug_package %{nil}
%global appname jetbrains-toolbox

Name:           %{appname}
Version:        1.20.8804
Release:        1%{?dist}
Summary:        Manage your JetBrains IDEs the easy way
License:        custom:jetbrains
URL:            https://www.jetbrains.com/toolbox-app/
Source0:        https://download.jetbrains.com/toolbox/jetbrains-toolbox-1.20.8804.tar.gz
Source1:        https://raw.githubusercontent.com/topazus/fedora-copr/main/jetbrains-toolbox/LICENSE
Source2:        https://raw.githubusercontent.com/topazus/fedora-copr/main/jetbrains-toolbox/icon.svg
Source3:        https://raw.githubusercontent.com/topazus/fedora-copr/main/jetbrains-toolbox/jetbrains-toolbox.desktop

BuildRequires: pkg-config
BuildRequires: desktop-file-utils libappstream-glib

Requires: java-11-openjdk

%description
Manage your JetBrains IDEs the easy way

%prep
%autosetup -n %{appname}-%{version} -p1

%build

%install
install -pDm755 jetbrains-toolbox %{buildroot}%{_bindir}/%{appname}

install -pDm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/jetbrains-toolbox.desktop
install -pDm644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/jetbrains-toolbox.svg

install -pDm644 %{SOURCE3} %{buildroot}%{_datadir}/jetbrains-toolbox/LICENSE

%check

%files
%{_bindir}/%{appname}
%{_datadir}/applications/jetbrains-toolbox.desktop
%{_datadir}/icons/hicolor/scalable/apps/jetbrains-toolbox.svg
%{_datadir}/jetbrains-toolbox/LICENSE

%changelog
