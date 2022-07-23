%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname rakudo

%define is_git 0

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        5%{?dist}
Summary:        Perl 6 compiler implementation that runs on MoarVM
License:        Artistic 2.0
URL:            http://rakudo.org/
#Source0:

BuildRequires:  perl make gcc

BuildRequires:  git curl tar wget

# To fix rpath issue with executables.
BuildRequires:  chrpath

%description
Rakudo Perl 6, or just Rakudo, is an implementation of the
Perl 6 language specification. More information about Perl 6 is available
from <http://perl6.org/>. This package provides a Perl 6 compiler built for
MoarVM virtual machine.


%prep

%if %{is_git}
git clone --depth=1 https://github.com/rakudo/rakudo.git .
%else
wget https://github.com/rakudo/rakudo/releases/download/2022.06/rakudo-2022.06.tar.gz
tar -xf rakudo-*.tar.gz && rm rakudo-*.tar.gz
cp -r rakudo-*/* . && rm -r rakudo-*
%endif


%build
perl Configure.pl --gen-moar --gen-nqp --backends=moar
%{make_build}

%install
# solve rpath error
export QA_RPATHS=$[ 0x0001 | 0x002 ]

#%{make_install} DESTDIR=%{_prefix}
#%{make_install}

cd install
mkdir -p %{buildroot}%{_prefix}
cp -a bin include lib share %{buildroot}%{_prefix}

# Fix the rpath error.
#chrpath --delete %{buildroot}%{_bindir}/moar


%check


%files
%doc README.md
%license LICENSE
%{_bindir}/moar
%{_bindir}/nqp
%{_bindir}/nqp-m

/usr/include/dyncall/*.h
/usr/include/libtommath/*.h
/usr/include/libuv/uv.h
/usr/include/libuv/uv/*.h
/usr/include/mimalloc/*.h


/usr/include/moar/


/usr/lib/libmoar.so
/usr/share/nqp/lib/
/usr/share/nqp/lib/MAST/Nodes.nqp

/usr/share/pkgconfig/moar.pc


%changelog
