
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname fish


Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        The user-friendly command line shell
License:        GPL
URL:            https://github.com/fish-shell/fish-shell
Source:         https://github.com/fish-shell/fish-shell/archive/master/fish-shell-master.tar.gz

BuildRequires: gcc-c++ cmake pkg-config ninja-build
BuildRequires: desktop-file-utils libappstream-glib
BuildRequires: ncurses-devel gettext gettext-devel pcre2-devel sphinx python3-devel python3-sphinx

# tab completion wants man-db
Recommends: man-db man-pages groff-base

%description
Fish is a smart and user-friendly command line shell for macOS, Linux, and the rest of the family. fish includes features like syntax highlighting, autosuggest-as-you-type, and fancy tab completions that just work, with no configuration required.

%prep
%autosetup -n fish-shell-master -p1

%build
%cmake . -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%post
if [ "$1" = 1 ]; then
  if [ ! -f %{_sysconfdir}/shells ] ; then
    echo "%{_bindir}/fish" > %{_sysconfdir}/shells
    echo "/bin/fish" >> %{_sysconfdir}/shells
  else
    grep -q "^%{_bindir}/fish$" %{_sysconfdir}/shells || echo "%{_bindir}/fish" >> %{_sysconfdir}/shells
    grep -q "^/bin/fish$" %{_sysconfdir}/shells || echo "/bin/fish" >> %{_sysconfdir}/shells
  fi
fi
 
%postun
if [ "$1" = 0 ] && [ -f %{_sysconfdir}/shells ] ; then
  sed -i '\!^%{_bindir}/fish$!d' %{_sysconfdir}/shells
  sed -i '\!^/bin/fish$!d' %{_sysconfdir}/shells
fi

%files
%license COPYING
%{_bindir}/fish*

%{_sysconfdir}/fish/config.fish

%{_datadir}/applications/*.desktop

%dir %{_datadir}/doc/fish
%{_datadir}/doc/fish/
%{_datadir}/fish/*

%{_mandir}/man1/*.1.gz

%{_datadir}/locale/*
%{_datadir}/pixmaps/fish.png
%{_datadir}/pkgconfig/fish.pc

%changelog
