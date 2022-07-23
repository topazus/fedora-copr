%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname chez-scheme

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        dialect and implementation of the language Scheme which is a type of Lisp
License:        Apache
URL:            https://github.com/cisco/ChezScheme
#Source0:

BuildRequires:  make gcc tar lua wget git
BuildRequires:  ncurses-devel libuuid-devel libX11-devel

%description
Chez Scheme is both a programming language and an implementation of that language, with supporting tools and documentation.

%prep
git clone --depth=1 https://github.com/cisco/ChezScheme.git .

wget https://raw.githubusercontent.com/topazus/fedora-copr/main/chez-scheme/install-permissions.lua
lua install-permissions.lua

%build
#./configure --installprefix=%{buildrooot}/usr
./configure --installbin=%{_bindir} --installlib=%{_libdir} \
    --installman=%{_mandir} --temproot=%{buildroot} --threads
%make_build

%install
%make_install

%files
/usr/bin/petite
/usr/bin/scheme
/usr/bin/scheme-script
/usr/lib64/csv*/examples/
/usr/lib64/csv*/ta6le/
/usr/share/man/man1/petite.1.gz
/usr/share/man/man1/scheme.1.gz

%changelog
