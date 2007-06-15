%define module  Heimdal-Kadm5
%define name    perl-%{module}
%define version 0.06
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Convert numbers to strings with pretty formatting
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://www.pdc.kth.se/heimdal/
Source:		ftp://ftp.su.se/pub/users/leifj/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	heimdal-devel
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
Number::Format is a library for formatting numbers.  Functions are
provided for converting numbers to strings in a variety of ways, and to
convert strings that contain numbers back into numeric form.  The output
formats may include thousands separators - characters inserted between
each group of three characters counting right to left from the decimal
point.  The characters used for the decimal point and the thousands
separator come from the locale information or can be specified by the
user.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
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
