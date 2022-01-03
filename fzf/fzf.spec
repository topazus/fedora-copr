%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname fzf
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        🌸 A command-line fuzzy finder
License:        MIT
URL:            https://github.com/junegunn/fzf
Source:         https://github.com/junegunn/fzf/archive/master/%{appname}-master.tar.gz

BuildRequires:  golang git


%description
fzf is a general-purpose command-line fuzzy finder.

%prep
%autosetup -n %{appname}-master -p1

sed -i 's,#!%{_bindir}/env ,#!/bin/,' ./bin/fzf-tmux

%build
go build -v

%install
install -pDm755 fzf %{buildroot}%{_bindir}/%{appname}
install -pDm755 bin/fzf-tmux %{buildroot}%{_bindir}/fzf-tmux

gzip --best man/man1/*
install -pDm644 man/man1/fzf.1.gz %{buildroot}%{_datadir}/man/man1/fzf.1.gz
install -pDm644 man/man1/fzf-tmux.1.gz %{buildroot}%{_datadir}/man/man1/fzf-tmux.1.gz

install -pDm644 shell/completion.bash %{buildroot}%{_datadir}/bash-completion/completions/fzf
install -pDm644 shell/completion.zsh %{buildroot}%{_datadir}/zsh/site-functions/_fzf

%if %{with check}
%check

%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}
%{_bindir}/fzf-tmux

%{_datadir}/man/man1/fzf.1.gz
%{_datadir}/man/man1/fzf-tmux.1.gz

%{_datadir}/bash-completion/completions/fzf
%{_datadir}/zsh/site-functions/_fzf

%changelog
