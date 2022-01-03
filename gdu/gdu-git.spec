%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname gdu

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Disk usage analyzer with console interface written in Go
License:        MIT
URL:            https://github.com/dundee/gdu
Source:         https://github.com/dundee/gdu/archive/master/%{appname}-master.tar.gz

BuildRequires:  gcc-c++ make pkg-config git wget

%description
Gdu is intended primarily for SSD disks where it can fully utilize parallel processing. However HDDs work as well, but the performance gain is not so huge.

%prep
%autosetup -n %{appname}-master -p1

mkdir -p $HOME/go-env
wget -O- https://golang.org/dl/go1.16.5.linux-amd64.tar.gz | tar xvzf - -C $HOME/go-env

%build
$HOME/go-env/go/bin/go build -v ./cmd/gdu

%install
install -pDm755 gdu %{buildroot}%{_bindir}/%{appname}

gzip --best gdu.1
install -pDm644 gdu.1.gz %{buildroot}%{_mandir}/man1/gdu.1.gz

%check
$HOME/go-env/go/bin/go test -v ./...

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}
%{_mandir}/man1/gdu.1.gz

%changelog
