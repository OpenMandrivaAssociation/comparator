Summary:	Tools for fast comparasion of large source-code trees
Name:		comparator
Version:	2.8
Release:	1
License:	GPL
Group:		Development/Other
Source0:	http://www.catb.org/~esr/comparator/%{name}-%{version}.tar.gz
URL:		http://www.catb.org/~esr/comparator

%description
Comparator and filterator are a pair of tools for rapidly finding
common code segments in large source trees. They can be useful as
tools for detecting copyright infringement.

%prep
%setup -q

%build
%make

%install
install -d %{buildroot}{%{_bindir},%{_mandir}/man1,%{py_sitedir}}

install comparator filterator  %{buildroot}%{_bindir}
install comparator.1  %{buildroot}%{_mandir}/man1
install comparator.py  %{buildroot}%{py_sitedir}

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/comparator.1*
%{py_sitedir}/*


%changelog
* Tue Jan 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.8-1
+ Revision: 759415
- imported package comparator

