
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname vifm
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        A file manager with curses interface
License:        GPL 2.0
URL:            https://github.com/vifm/vifm
Source:         https://github.com/vifm/vifm/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-c++ make pkg-config automake ncurses-devel
BuildRequires: libX11-devel gtk+-devel
BuildRequires: desktop-file-utils libappstream-glib

%description
Vifm is a file manager with curses interface, which provides Vi[m]-like environment for managing objects within file systems, extended with some useful ideas from mutt.

%prep
%autosetup -n %{appname}-master -p1

%build
./scripts/fix-timestamps
./configure --prefix=%{_prefix}
%make_build

%install
%make_install

rm %{buildroot}%{_prefix}/etc/vifm/colors/Default-256.vifm

%if %{with check}
%check
make check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%endif

%files
%license COPYING
%doc README.md
%{_bindir}/vifm
%{_bindir}/vifm-convert-dircolors
%{_bindir}/vifm-pause
%{_bindir}/vifm-screen-split
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/vifm.png

%{_datadir}/bash-completion/completions/*
%{_datadir}/zsh/site-functions/_*
%{_datadir}/man/man1/*.1.gz

%dir %{_datadir}/doc/vifm
%{_datadir}/doc/vifm/*
%dir %{_datadir}/vifm
%{_datadir}/vifm/*

%changelog
