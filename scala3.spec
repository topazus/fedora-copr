%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname scala3

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A next-generation compiler for Scala
License:        ASL 2.0
URL:            https://github.com/lampepfl/dotty
#Source:         

BuildRequires:  pkg-config java-17-openjdk
BuildRequires:  wget git

Requires:       java-17-openjdk

%description
A next-generation compiler for Scala

%prep
git clone --depth=1 https://github.com/lampepfl/dotty.git .

mkdir -p $HOME
wget https://github.com/sbt/sbt/releases/download/v1.6.1/sbt-1.6.1.tgz
tar xf sbt-*.tgz


%build
./sbt/bin/sbt dist/packArchive

%install
mkdir -p %{buildroot}/opt/scala
cd dist/target/pack/
cp -a * %{buildroot}/opt/scala

rm %{buildroot}/opt/scala/bin/*.bat

mkdir -p %{buildroot}/usr/bin
ln -s /opt/bin/scala %{buildroot}/usr/bin/scala3
ln -s /opt/bin/scalac %{buildroot}/usr/bin/scalac3
ln -s /opt/bin/scaladoc %{buildroot}/usr/bin/scala3doc

%check


%files
/opt/scala/
/usr/bin/scala3
/usr/bin/scala3doc
/usr/bin/scalac3

%changelog
