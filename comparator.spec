%define debug_package %{nil}

Summary:	Tools for fast comparasion of large source-code trees
Name:		comparator
Version:	2.10
Release:	1
License:	BSD
Group:		Development/Other
Url:		http://www.catb.org/~esr/comparator
Source0:	http://www.catb.org/~esr/comparator/%{name}-%{version}.tar.gz

%description
Comparator and filterator are a pair of tools for rapidly finding
common code segments in large source trees. They can be useful as
tools for detecting copyright infringement.

%prep
%autosetup -p1

%build
%setup_compile_flags
%make_build CC=%{__cc}

%install
install -d %{buildroot}{%{_bindir},%{_mandir}/man1,%{py2_puresitedir}}

install comparator filterator  %{buildroot}%{_bindir}
install comparator.1  %{buildroot}%{_mandir}/man1
install comparator.py  %{buildroot}%{py2_puresitedir}

%files
%doc README
%{_bindir}/*
%{_mandir}/man1/comparator.1*
%{py2_puresitedir}/*
