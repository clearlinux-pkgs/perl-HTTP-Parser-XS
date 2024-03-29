#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTTP-Parser-XS
Version  : 0.17
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/HTTP-Parser-XS-0.17.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/HTTP-Parser-XS-0.17.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libh/libhttp-parser-xs-perl/libhttp-parser-xs-perl_0.17-1.debian.tar.xz
Summary  : 'a fast, primitive HTTP request parser'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0 MIT
Requires: perl-HTTP-Parser-XS-license = %{version}-%{release}
Requires: perl-HTTP-Parser-XS-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Install)

%description
NAME
HTTP::Parser::XS - a fast, primitive HTTP request parser
SYNOPSIS
use HTTP::Parser::XS qw(parse_http_request);

%package dev
Summary: dev components for the perl-HTTP-Parser-XS package.
Group: Development
Provides: perl-HTTP-Parser-XS-devel = %{version}-%{release}
Requires: perl-HTTP-Parser-XS = %{version}-%{release}

%description dev
dev components for the perl-HTTP-Parser-XS package.


%package license
Summary: license components for the perl-HTTP-Parser-XS package.
Group: Default

%description license
license components for the perl-HTTP-Parser-XS package.


%package perl
Summary: perl components for the perl-HTTP-Parser-XS package.
Group: Default
Requires: perl-HTTP-Parser-XS = %{version}-%{release}

%description perl
perl components for the perl-HTTP-Parser-XS package.


%prep
%setup -q -n HTTP-Parser-XS-0.17
cd %{_builddir}
tar xf %{_sourcedir}/libhttp-parser-xs-perl_0.17-1.debian.tar.xz
cd %{_builddir}/HTTP-Parser-XS-0.17
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/HTTP-Parser-XS-0.17/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTTP-Parser-XS
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-HTTP-Parser-XS/f4534b6d73480e53100c7f12f1c4f50c9adb9904
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTTP::Parser::XS.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-HTTP-Parser-XS/f4534b6d73480e53100c7f12f1c4f50c9adb9904

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
