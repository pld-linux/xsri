Summary:	xsri - X Set Root Image
Summary(pl):	xsri - X Set Root Image
Name:		xsri
Version:	2.1.0
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.pleyades.net/pawm/utils/%{name}-%{version}.tar.gz
# Source0-md5:	624a8edc75e347fb0f5de7e3a921f67d
URL:		http://www.pleyades.net/pawm/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fontconfig-libs
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libtool
BuildRequires:	pango-devel
Buildrequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Set Root Image - displays images on the root window with parameters.

%description -l pl
X Set Root Image - wy¶wietla obraz jako tapetê.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
