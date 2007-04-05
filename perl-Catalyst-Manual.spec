#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Manual
Summary:	Catalyst::Manual - The Catalyst developer's manual
Summary(pl.UTF-8):	Catalyst::Manual - podręcznik programisty Catalysta
Name:		perl-Catalyst-Manual
Version:	5.700501
Release:	1
License:	Creative Commons Attribution NonCommercial ShareAlike 2.5, parts on GPL v1+ or Artistic
Group:		Documentation
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	da5b7ab234cdfbadf545f8da25c176be
URL:		http://search.cpan.org/dist/Catalyst-Manual/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Catalyst::Manual - The Catalyst developer's manual.

%description -l pl.UTF-8
Catalyst::Manual - podręcznik programisty Catalysta.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Catalyst/*.pm
# Catalyst::Manual.3pm.gz conflicts with file from Catalyst, and that one is more useful
%{_mandir}/man3/Catalyst::Manual::*
