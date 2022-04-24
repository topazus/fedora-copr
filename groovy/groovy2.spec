%global debug_package %{nil}

Name:           groovy
Version:        4.0.0
Release:        1%{?dist}
Summary:        A powerful multi-faceted programming language for the JVM platform
License:        ASL 2.0
URL:            https://groovy-lang.org/
Source:         https://github.com/apache/groovy/archive/master/groovy-master.tar.gz

BuildRequires:  make autoconf pkg-config unzip git
BuildRequires:  graphviz
BuildRequires:  java-17-openjdk

%description
Apache Groovy is a powerful, optionally typed and dynamic language, with static-typing and static compilation capabilities, for the Java platform aimed at improving developer productivity thanks to a concise, familiar and easy to learn syntax.

%prep
%autosetup -n groovy-master -p1

git clone -b GROOVY_4_0_X https://github.com/apache/groovy.git

%build
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
