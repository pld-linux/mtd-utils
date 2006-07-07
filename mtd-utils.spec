Summary:	MTD (Memory Technology Devices) utilities
Summary(pl):	Narzêdzia MTD (Memory Technology Devices)
Name:		mtd-utils
Version:	1.0.0
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	ftp://ftp.infradead.org/pub/mtd-utils/%{name}-%{version}.tar.gz
# Source0-md5:	442bdbdb024db27dc9c89207fac16f95
URL:		http://www.linux-mtd.infradead.org/
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
Obsoletes:	mtd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MTD are utilities for jffs (Journalling Flash File System), like
mkfs.jffs2 and NAND Flash devices.

%description -l pl
Programy MTD zawieraj± narzêdzia do jffs (Journalling Flash File
System), jak mkfs.jffs2 oraz urz±dzeñ NAND Flash.

%package devel
Summary:	Header files for MTD utilities
Summary(pl):	Pliki nag³ówkowe dla narzêdzi MTD
Group:		Development/Libraries

%description devel
Header files for MTD utilities.

%description devel -l pl
Pliki nag³ówkowe dla narzêdzi MTD.

%prep
%setup -q
sed -e '/install:/s/${TARGETS}//' -i Makefile

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I./include -Wall"	\
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}

cp -r include/mtd $RPM_BUILD_ROOT%{_includedir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc device_table.txt
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/mtd
