#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Catalyst
%define	pnam	Manual
Summary:	Catalyst::Manual - The Catalyst developer's manual
Summary(pl.UTF-8):	Catalyst::Manual - podręcznik programisty Catalysta
Name:		perl-Catalyst-Manual
Version:	5.9013
Release:	1
Epoch:		1
License:	GPL v1+ or Artistic
Group:		Documentation
Source0:	https://www.cpan.org/authors/id/E/ET/ETHER/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	90531616d32e9d5625cce2039622a3e3
URL:		http://search.cpan.org/dist/Catalyst-Manual/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
%endif
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
%{perl_vendorlib}/Catalyst/Manual
# Catalyst::Manual.3pm.gz conflicts with file from Catalyst, and that one is more useful
%{_mandir}/man3/Catalyst::Manual::*
