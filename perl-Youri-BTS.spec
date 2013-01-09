%define module	Youri-BTS

Name:		perl-%{module}
Version:	0.1.1
Release:	8
Summary:	Youri BTS interface
License:	GPL or Artistic
Group:		Development/Other
Source:		http://youri.zarb.or/download/%{module}-v%{version}.tar.bz2
Url:		http://youri.zarb.org
BuildRequires:	perl-devel
Requires:	perl(version)
BuildArch:	noarch

%description
YOURI stands for "Youri Offers an Upload & Repository Infrastucture". It aims
to build tools making management of a coherent set of packages easier.

This class provides an uniform view over various kind of bug-tracking systems.

%prep
%setup -q -n %{module}-v%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc ChangeLog README
%{perl_vendorlib}/Youri
%{_mandir}/man3/*


%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.1.1-6mdv2010.0
+ Revision: 430670
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1.1-5mdv2009.0
+ Revision: 258920
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1.1-4mdv2009.0
+ Revision: 246795
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.1.1-2mdv2008.1
+ Revision: 136373
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Apr 23 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.1-2mdv2008.0
+ Revision: 17196
- force dependency on perl-version

* Sun Apr 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.1-1mdv2008.0
+ Revision: 17027
- new version


* Fri Mar 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.0-1mdv2007.1
+ Revision: 138886
- Imported perl-Youri-BTS-0.1.0-1mdv2007.1 into SVN repository.

* Fri Mar 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.0-1mdv2007.1
- first mdv release

