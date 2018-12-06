#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTTP-Parser-XS
Version  : 0.17
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/HTTP-Parser-XS-0.17.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/HTTP-Parser-XS-0.17.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libh/libhttp-parser-xs-perl/libhttp-parser-xs-perl_0.17-1.debian.tar.xz
Summary  : 'a fast, primitive HTTP request parser'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0 MIT
Requires: perl-HTTP-Parser-XS-lib = %{version}-%{release}
Requires: perl-HTTP-Parser-XS-license = %{version}-%{release}
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
Requires: perl-HTTP-Parser-XS-lib = %{version}-%{release}
Provides: perl-HTTP-Parser-XS-devel = %{version}-%{release}

%description dev
dev components for the perl-HTTP-Parser-XS package.


%package lib
Summary: lib components for the perl-HTTP-Parser-XS package.
Group: Libraries
Requires: perl-HTTP-Parser-XS-license = %{version}-%{release}

%description lib
lib components for the perl-HTTP-Parser-XS package.


%package license
Summary: license components for the perl-HTTP-Parser-XS package.
Group: Default

%description license
license components for the perl-HTTP-Parser-XS package.


%prep
%setup -q -n HTTP-Parser-XS-0.17
cd ..
%setup -q -T -D -n HTTP-Parser-XS-0.17 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/HTTP-Parser-XS-0.17/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTTP-Parser-XS
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-HTTP-Parser-XS/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/HTTP/Parser/XS.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/HTTP/Parser/XS/PP.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTTP::Parser::XS.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/auto/HTTP/Parser/XS/XS.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-HTTP-Parser-XS/deblicense_copyright
