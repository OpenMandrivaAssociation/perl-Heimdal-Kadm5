%define module  Heimdal-Kadm5
%define name    perl-%{module}
%define version 0.06
%define release %mkrel 10

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl extension for adminstration of Heimdal Kerberos servers
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://www.pdc.kth.se/heimdal/
Source:		ftp://ftp.su.se/pub/users/leifj/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	heimdal-devel
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
Heimdal::Kadm5 is a basic XSUB perl glue to the Heimdal
(http://www.pdc.kth.se/src/heimdal) kadm5clnt library. Heimdal is a free,
slightly less export challenged implementation of Kerberos5 by Assar Westerlund
and Johan Danielsson. Heimdal::Kadm5 allows you to perform more administration
of your kdc than you can usually pull off with the included kadmin program.
Heimdal::Kadm5 should be considered alpha-code and may consequently crash and
burn but should not muck up your kdc any more than kadmin itself does.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor INC="-I%{_includedir}/heimdal"
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
# doesn't work without a running KDC
#%{__make} test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/Heimdal
%{perl_vendorarch}/auto/Heimdal
%{_mandir}/*/*
