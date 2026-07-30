%define upstream_name Heimdal-Kadm5
%define upstream_version 0.08
Name:		perl-%{upstream_name}
Version:	0.08
Release:	1
Summary:	Perl extension for adminstration of Heimdal Kerberos servers
License:	Artistic/GPL
Group:		Development/Perl
Url:		https://metacpan.org/dist/Heimdal-Kadm5
Source0:	https://cpan.metacpan.org/authors/id/L/LE/LEIFJ/Heimdal-Kadm5-0.08.tar.gz
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	heimdal-devel

%description
Heimdal::Kadm5 is a basic XSUB perl glue to the Heimdal
(http://www.pdc.kth.se/src/heimdal) kadm5clnt library. Heimdal is a free,
slightly less export challenged implementation of Kerberos5 by Assar Westerlund
and Johan Danielsson. Heimdal::Kadm5 allows you to perform more administration
of your kdc than you can usually pull off with the included kadmin program.
Heimdal::Kadm5 should be considered alpha-code and may consequently crash and
burn but should not muck up your kdc any more than kadmin itself does.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor INC="-I%{_includedir}/heimdal"
%make

%install
%makeinstall_std

%check
# doesn't work without a running KDC
#make test

%files
%doc Changes README
%{perl_vendorarch}/Heimdal
%{perl_vendorarch}/auto/Heimdal
%{_mandir}/*/*


