%define upstream_name Heimdal-Kadm5
%define upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Summary:	Perl extension for adminstration of Heimdal Kerberos servers
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/L/LE/LEIFJ/%{upstream_name}-%{upstream_version}.tar.gz
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
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Sun Feb 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.80.0-3
+ Revision: 773665
- clean out spec
- mass rebuild of perl extensions against perl 5.14.2

* Mon Mar 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.80.0-2mdv2010.1
+ Revision: 528738
- rebuild

* Sun Feb 21 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.80.0-1mdv2010.1
+ Revision: 509022
- new version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.06-10mdv2010.0
+ Revision: 430465
- rebuild

* Thu Oct 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-9mdv2009.0
+ Revision: 290794
- fix summary and description (spotted by Buchan)

* Tue Sep 30 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-8mdv2009.0
+ Revision: 290160
- rebuild to fix linkage

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Jan 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-5mdv2008.1
+ Revision: 156901
- fix build

  + Thierry Vignaud <tv@mandriva.org>
    - add BR on krb5-devel
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Sep 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-2mdv2008.0
+ Revision: 81308
- rebuild

* Fri Jun 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2008.0
+ Revision: 39960
- new version

* Wed May 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2008.0
+ Revision: 20499
- Import perl-Heimdal-Kadm5



* Thu Apr 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2008.0
- first mdv release
