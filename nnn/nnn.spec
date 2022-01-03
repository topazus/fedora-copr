%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname nnn
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        n³ The unorthodox terminal file manager
License:        BSD-2-Clause
URL:            https://github.com/jarun/nnn
Source:         https://github.com/jarun/nnn/archive/master/%{appname}-master.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  desktop-file-utils

%description
nnn (n³) is a full-featured terminal file manager. It's tiny and nearly 0-config with an incredible speed.

%prep
%autosetup -n %{appname}-master -p1


%build
make

%install
make install PREFIX=%{buildroot}%{_prefix}

make install-desktop PREFIX=%{buildroot}%{_prefix}

install -pDm644 misc/auto-completion/bash/nnn-completion.bash %{buildroot}%{_datadir}/bash-completion/completions/nnn
install -pDm644 misc/auto-completion/zsh/_nnn %{buildroot}%{_datadir}/zsh/site-functions/_nnn
install -pDm644 misc/auto-completion/fish/nnn.fish %{buildroot}%{_datadir}/fish/vendor_completion.d/nnn.fish

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/64x64/apps/nnn.png
%{_datadir}/icons/hicolor/scalable/apps/nnn.svg

%{_datadir}/man/man1/nnn.1.gz
%{_datadir}/bash-completion/completions/nnn
%{_datadir}/zsh/site-functions/_nnn
%{_datadir}/fish/vendor_completion.d/nnn.fish

%changelog
