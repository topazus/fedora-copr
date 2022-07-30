%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname flameshot

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Powerful yet simple to use screenshot software
License:        GPL
URL:            https://github.com/flameshot-org/flameshot
#Source:

BuildRequires:  gcc-c++ cmake
BuildRequires:  qt5-qtbase-devel qt5-linguist qt5-qtsvg-devel

Requires:       qt5-qtbase qt5-qtsvg-devel

%description
Powerful yet simple to use screenshot software.

%prep
git clone --depth=1 https://github.com/flameshot-org/flameshot.git .

%build
%cmake
%cmake_build

%install
%cmake_install

%check

%files
/usr/bin/flameshot
/usr/share/applications/org.flameshot.Flameshot.desktop

/usr/share/bash-completion/completions/flameshot
/usr/share/zsh/site-functions/_flameshot
/usr/share/fish/vendor_completions.d/flameshot.fish

/usr/share/dbus-1/interfaces/org.flameshot.Flameshot.xml
/usr/share/dbus-1/services/org.flameshot.Flameshot.service
/usr/share/flameshot/translations/*.qm
/usr/share/icons/hicolor/*/apps/*.png
/usr/share/icons/hicolor/scalable/apps/*.svg
/usr/share/man/man1/flameshot.1.gz
/usr/share/metainfo/org.flameshot.Flameshot.metainfo.xml

%changelog
