%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname codelite
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        A cross platform C/C++/PHP and Node.js IDE written in C++
License:        GPL 2.0
URL:            https://github.com/eranif/codelite
Source:         https://github.com/eranif/codelite/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-c++ cmake pkg-config
BuildRequires: desktop-file-utils libappstream-glib
BuildRequires: wxGTK-devel libssh-devel sqlite-devel gtk3-devel wxBase-devel wxGTK3-devel hunspell-devel glib2-devel lldb-devel

Requires:      wxGTK xterm

%description
CodeLite is a free, open source, cross platform IDE specialized in C, C++, PHP and JavaScript (mainly for backend developers using Node.js) programming languages, which runs best on all major platforms (Windows, macOS and Linux).

%prep
%autosetup -n %{appname}-master -p1

%build
WX_CONFIG="wx-config-gtk3"
export WX_CONFIG
cmake -S . -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release -DWITH_WX_CONFIG=${WX_CONFIG} -DENABLE_LLDB=1 -DWITH_MYSQL=0 -DCMAKE_INSTALL_LIBDIR=lib

%cmake_build

%install
%cmake_install

rm -rf %{buildroot}%{_datadir}/icons/hicolor/*@2x \
    %{buildroot}%{_datadir}/locale/*



%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}
%{_bindir}/codelite-cc
%{_bindir}/codelite-echo
%{_bindir}/codelite-lsp-helper
%{_bindir}/codelite-make
%{_bindir}/codelite-remote
%{_bindir}/codelite-terminal
%{_bindir}/codelite_cppcheck
%{_bindir}/codelite_exec
%{_bindir}/codelite_fix_files
%{_bindir}/codelite_indexer
%{_bindir}/codelite_kill_children
%{_bindir}/codelite_open_helper.py
%{_bindir}/codelite_xterm

%{_datadir}/applications/*.desktop

%dir %{_libdir}/codelite/
%{_libdir}/codelite/*
%dir %{_datadir}/codelite/
%{_datadir}/codelite/*

%{_datadir}/icons/hicolor/*/apps/codelite.png

%{_datadir}/man/man1/codelite-make.1.gz
%{_datadir}/man/man1/codelite.1.gz
%{_datadir}/man/man1/codelite_fix_files.1.gz

%changelog
