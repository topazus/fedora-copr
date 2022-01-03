%if 0%{?fedora} == 35
%global _missing_build_ids_terminate_build 0
%endif

%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname hugo

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        World’s fastest framework for building websites

License:        MIT
URL:            https://github.com/gohugoio/hugo
Source:         https://github.com/gohugoio/hugo/archive/master/%{appname}-master.tar.gz

BuildRequires: golang git gcc-c++ wget
BuildRequires: libsass-devel

%description
The world’s fastest framework for building websites.

%prep
%autosetup -n %{appname}-master -p1
mkdir -p $HOME/go-env
wget -O- https://golang.org/dl/go1.16.5.linux-amd64.tar.gz | tar xvzf - -C $HOME/go-env


%build
$HOME/go-env/go/bin/go build -v -tags extended

./hugo gen man
./hugo gen autocomplete --completionfile hugo-completion

%install
install -pDm755 %{appname} %{buildroot}%{_bindir}/%{appname}

install -pDm644 man/* -t %{buildroot}%{_mandir}/man1
install -pDm644 hugo-completion %{buildroot}%{_datadir}/bash-completion/completions/hugo

%check
$HOME/go-env/go/bin/go test

%files
%license LICENSE
%doc README.md
%{_bindir}/%{appname}
%{_mandir}/man1/*
%{_datadir}/bash-completion/completions/hugo

%changelog
