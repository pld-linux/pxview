Summary:	View Paradox DB files
Summary(pl.UTF-8):   Narzędzie do oglądania plików baz danych Paradox DB
Name:		pxview
Version:	0.2.5
Release:	3
Epoch:		0
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/pxlib/%{name}_%{version}.orig.tar.gz
# Source0-md5:	954dbb0371986d6e27802de8043c6807
URL:		http://pxlib.sourceforge.net/
BuildRequires:	docbook-utils
BuildRequires:	libgsf-devel
BuildRequires:	pkgconfig
BuildRequires:	pxlib-devel >= 0.5.1
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pxview is quite simple command line program which has been originally
created to test pxlib. pxlib is a library to read Paradox files.
During the development pxview has evolved more and more into a useful
program to examine the contents of Paradox files and to convert them
into SQL or CSV format.

%description -l pl.UTF-8
pxview to w miarę mały program działający z linii poleceń, początkowo
stworzony do testowania biblioteki pxlib (służącej do odczytu plików
Paradoksa). Podczas tworzenia pxview coraz bardziej ewoluował stając
się przydatnym programem do oglądania zawartości plików Paradoksa i
konwertowania ich do formatu SQL lub CSV.

%prep
%setup -q

%build
# man pages are build by docbook2man
sed -i -e 's#docbook-to-man#docbook2man#g' configure*
sed -i -e 's#docbook-to-man $<.*#docbook2man $<#g' doc/Makefile*
for man in doc/*.sgml; do
        name=$(basename "$man" .sgml)
        sed -i -e "s#$name#$name#gi" $man
done
CPPFLAGS="$(pkg-config glib-2.0 --cflags)"
%configure \
	--with-sqlite \
	--with-gsf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
