# TODO:
# - missing manual files (no docbook-to-man tool)
Summary:	View Paradox DB files
Name:		pxview
Version:	0.2.3
Release:	1
Epoch:		0
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/pxlib/%{name}_%{version}.orig.tar.gz
# Source0-md5:	0b0164588af775dec7f6f6f64d61e270
URL:		http://pxlib.sourceforge.net/
BuildRequires:	pxlib-devel
BuildRequires:	sqlite-devel
BuildRequires:	libgsf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pxview is quite simple command line program which has been originally
created to test pxlib. pxlib is a library to read Paradox files.
During the development pxview has evolved more and more into a useful
program to examine the contents of Paradox files and to convert them
into SQL or CSV format.

%prep
%setup -q

%build
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
