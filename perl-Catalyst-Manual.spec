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
Version:	5.8000
Release:	1
Epoch:		1
License:	GPL v1+ or Artistic
Group:		Documentation
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9648aba17195f86b201c82f373c315dd
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
# Catalyst::Manual.3pm.gz conflicts with file from Catalyst, and that one is more useful
%{_mandir}/man3/Catalyst::Manual::*
