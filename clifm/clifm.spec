%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname clifm

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        a CLI-based, shell-like, and non-curses terminal file manager written in C: simple, fast, extensible, and lightweight as hell
License:        GPL 2.0
URL:            https://github.com/leo-arch/clifm
Source:         https://github.com/leo-arch/clifm/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-c++ make pkg-config 
BuildRequires: desktop-file-utils libappstream-glib libcap-devel libacl-devel readline-devel

Requires: libcap libacl readline
# for remote filesystems support
Requires: fuse-sshfs curlftpfs cifs-utils

%description
CliFM is a completely command-line-based, shell-like file manager able to perform all the basic operations you may expect from any other file manager.

%prep
%autosetup -n %{appname}-master -p1

%build
make %{?_smp_mflags}

%install
install -pDm755 clifm %{buildroot}%{_bindir}/%{appname}
install -pDm644 misc/clifm.desktop %{buildroot}%{_datadir}/applications/*.desktop

install -pDm644 images/logo/clifm.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/*.svg

install -pDm644 misc/completions.bash %{buildroot}%{_datadir}/bash-completion/completions/clifm
install -pDm644 misc/completions.zsh %{buildroot}%{_datadir}/zsh/site-functions/_clifm

gzip --best misc/manpage
install -pDm644 misc/manpage.gz %{buildroot}%{_datadir}/man/man1/clifm.1.gz

install -d %{buildroot}%{_datadir}/clifm
cp -r plugins %{buildroot}%{_datadir}/clifm
cp -r functions %{buildroot}%{_datadir}/clifm

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg

%{_datadir}/bash-completion/completions/clifm
%{_datadir}/zsh/site-functions/_clifm
%{_datadir}/man/man1/clifm.1.gz
%{_datadir}/clifm

%changelog
