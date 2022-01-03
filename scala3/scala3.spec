%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname scala3

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A next-generation compiler for Scala
License:        ASL 2.0
URL:            https://github.com/lampepfl/dotty
Source:         %{url}/archive/master/dotty-master.tar.gz

BuildRequires:  pkg-config java-17-openjdk
BuildRequires:  wget git

Requires:       java-17-openjdk

%description
A next-generation compiler for Scala

%prep
git clone https://github.com/lampepfl/dotty.git .

mkdir -p $HOME
wget -O- https://github.com/sbt/sbt/releases/download/v1.6.1/sbt-1.6.1.tgz | tar xvzf - -C $HOME

%build
$HOME/sbt/bin/sbt dist/packArchive

%install
mkdir -p %{buildroot}/opt/scala3
cp -a dist/target/* %{buildroot}/opt/scala3

%check


%files
%license LICENSE*
%doc README.md
%{buildroot}/opt/scala3/*

%changelog
