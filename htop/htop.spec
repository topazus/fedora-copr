%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname htop

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        an interactive process viewer
License:        GPLv2+
URL:            https://github.com/htop-dev/htop
Source:         %{url}/archive/main/%{appname}-main.tar.gz

BuildRequires: gcc make pkg-config
BuildRequires: ncurses-devel automake autoconf
BuildRequires: desktop-file-utils

%description
htop is a cross-platform interactive process viewer.

%prep
%autosetup -n %{appname}-main -p1

%build
./autogen.sh

%configure \
  --enable-openvz \
  --enable-vserver \
  --enable-taskstats \
  --enable-unicode \
  --with-sensors \
  --enable-cgroup
 
%make_build

%install
%make_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license COPYING
%doc README.md
%{_bindir}/%{appname}
%{_datadir}/pixmaps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/applications/*.desktop
%{_datadir}/man/man1/htop.1*

%changelog
