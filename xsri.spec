Summary:	X Set Root Image - display image on the root window
Summary(pl.UTF-8):	X Set Root Image - wyświetlanie obrazu w głównym oknie
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
BuildRequires:	gtk+2-devel >= 1.3.13
BuildRequires:	libtool
BuildRequires:	pkgconfig
Buildrequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Set Root Image - displays images on the root window with parameters.

%description -l pl.UTF-8
X Set Root Image - wyświetla obraz w głównym oknie (jako tapetę) z
podanymi parametrami.

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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
