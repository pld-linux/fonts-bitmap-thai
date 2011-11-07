Summary:	Collection of Thai bitmap fonts
Summary(pl.UTF-8):	Kolekcja bitmapowych fontów tajskich
Name:		fonts-bitmap-thai
Version:	1.2.5
Release:	1
License:	Free
Group:		Fonts
Source0:	http://linux.thai.net/pub/thailinux/software/thaixfonts/thaixfonts-%{version}.tar.gz
# Source0-md5:	8264a0cd4ab0ff1603bb4a795c1a1ea2
URL:		http://linux.thai.net/projects/thaixfonts
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
thaixfonts is a collection of Thai bitmap fonts available in free
licenses. It aims to collect fonts for installation convenience, and
maintain them as needed. This is because most fonts are aged,
unmaintained, and now even unavailable in the original sources.

%description -l pl.UTF-8
thaixfonts to kolekcja bitmapowych fontów tajskich dostępnych na
wolnych licencjach. Jej celem jest zebranie fontów dla wygody
instalacji i w razie potrzeby utrzymywanie ich. Jest to przydatne,
ponieważ większość fontów jest już stara, nie utrzymywana, a nawet
niedostępna w oryginalnych źródłach.

%prep
%setup -q -n thaixfonts-%{version}

%build
%configure \
	--with-fontdir=%{_fontsdir}/misc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_fontsdir}/misc/{thai.alias,fonts.alias.thai}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst misc

%postun
fontpostinst misc

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_fontsdir}/misc/etl*-thai.pcf.gz
%{_fontsdir}/misc/pvemacs_*.pcf.gz
%{_fontsdir}/misc/pvfixed_*.pcf.gz
%{_fontsdir}/misc/thai*.pcf.gz
%{_fontsdir}/misc/fonts.alias.thai
