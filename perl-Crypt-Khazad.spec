#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Khazad
Summary:	Crypt::Khazad - Crypt::CBC-compliant block cipher
Summary(pl.UTF-8):	Crypt::Khazad - szyfr blokowy kompatybilny z Crypt::CBC
Name:		perl-Crypt-Khazad
Version:	1.0.3
Release:	7
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f6908bf11cb780d455a8779a60ecc570
URL:		http://search.cpan.org/dist/Crypt-Khazad/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Khazad is a 128-bit key, 64-bit block cipher. Designed by Vincent
Rijmen and Paulo S. L. M. Barreto, Khazad is a NESSIE finalist for
legacy-level block ciphers. Khazad has many similarities with
Rijndael, and has an extremely high rate of diffusion. This module
supports the Crypt::CBC interface.

%description -l pl.UTF-8
Khazad to 64-bitowy szyfr blokowy ze 128-bitowym kluczem. Został
opracowany przez Vincenta Rijmena i Paulo S. L. M. Baretto. Khazad
jest finalistą NESSIE w kategorii spadkowych szyfrów blokowych.
Khazad ma wiele podobieństw do algorytmu Rijndael i ma bardzo
duży współczynnik dyfuzji. Ten moduł obsługuje interfejs Crypt::CBC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd examples
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
for f in * ; do
	sed -e "s@#!/usr/local/bin/perl@#!/usr/bin/perl@" $f \
		> $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Crypt/Khazad.pm
%dir %{perl_vendorarch}/auto/Crypt/Khazad
%{perl_vendorarch}/auto/Crypt/Khazad/Khazad.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/Khazad/Khazad.so
%{_mandir}/man3/*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
