%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname groovy

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A powerful multi-faceted programming language for the JVM platform
License:        ASL 2.0
URL:            https://groovy-lang.org/
Source:         https://github.com/apache/groovy/archive/master/groovy-master.tar.gz

BuildRequires:  make autoconf pkg-config unzip
BuildRequires:  wget
BuildRequires:  graphviz
#BuildRequires:  java-17-openjdk

%description
Apache Groovy is a powerful, optionally typed and dynamic language, with static-typing and static compilation capabilities, for the Java platform aimed at improving developer productivity thanks to a concise, familiar and easy to learn syntax.

%prep
%autosetup -n groovy-master -p1

cd $HOME && wget https://download.oracle.com/java/17/latest/jdk-17_linux-x64_bin.tar.gz
tar xvf jdk-*.tar.gz
mv $HOME/jdk-*/ $HOME/jdk

%build
export JAVA_HOME=$HOME/jdk
./gradlew clean dist

%install
unzip subprojects/groovy-binary/build/distributions/apache-groovy-binary-*.zip \
    -d %{buildroot}/opt
mv %{buildroot}/opt/groovy-* %{buildroot}/opt/%{name}

%check


%files
%license LICENSE*
%doc README*
/opt/%{name}/*

%changelog
