Summary:	MTD (Memory Technology Devices) utilities
Summary(pl.UTF-8):	Narzędzia MTD (Memory Technology Devices)
Name:		mtd-utils
Version:	1.5.2
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	ftp://ftp.infradead.org/pub/mtd-utils/%{name}-%{version}.tar.bz2
# Source0-md5:	596bc7b20a6d4fb86d63fc9b8af674d6
URL:		http://www.linux-mtd.infradead.org/
BuildRequires:	sed >= 4.0
BuildRequires:	libuuid-devel
BuildRequires:	lzo-devel >= 2
BuildRequires:	zlib-devel
Obsoletes:	mtd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MTD are utilities for jffs (Journalling Flash File System), like
mkfs.jffs2 and NAND Flash devices.

%description -l pl.UTF-8
Programy MTD zawierają narzędzia do jffs (Journalling Flash File
System), jak mkfs.jffs2 oraz urządzeń NAND Flash.

%package devel
Summary:	Header files for MTD utilities
Summary(pl.UTF-8):	Pliki nagłówkowe dla narzędzi MTD
Group:		Development/Libraries

%description devel
Header files for MTD utilities.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla narzędzi MTD.

%prep
%setup -q
sed -e '/install:/s/${TARGETS}//' -i Makefile

%build
CFLAGS="%{rpmcflags}" \
%{__make} \
	CC="%{__cc}" \
	LDFLAGS="%{rpmldflags}" \
	V=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}

cp -r include/mtd $RPM_BUILD_ROOT%{_includedir}
cp -p lib/libmtd.a $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc device_table.txt
%attr(755,root,root) %{_sbindir}/doc_loadbios
%attr(755,root,root) %{_sbindir}/docfdisk
%attr(755,root,root) %{_sbindir}/flash_erase
%attr(755,root,root) %{_sbindir}/flash_eraseall
%attr(755,root,root) %{_sbindir}/flash_lock
%attr(755,root,root) %{_sbindir}/flash_otp_dump
%attr(755,root,root) %{_sbindir}/flash_otp_info
%attr(755,root,root) %{_sbindir}/flash_otp_lock
%attr(755,root,root) %{_sbindir}/flash_otp_write
%attr(755,root,root) %{_sbindir}/flash_unlock
%attr(755,root,root) %{_sbindir}/flashcp
%attr(755,root,root) %{_sbindir}/ftl_check
%attr(755,root,root) %{_sbindir}/ftl_format
%attr(755,root,root) %{_sbindir}/jffs2dump
%attr(755,root,root) %{_sbindir}/jffs2reader
%attr(755,root,root) %{_sbindir}/mkfs.jffs2
%attr(755,root,root) %{_sbindir}/mkfs.ubifs
%attr(755,root,root) %{_sbindir}/mtd_debug
%attr(755,root,root) %{_sbindir}/mtdinfo
%attr(755,root,root) %{_sbindir}/mtdpart
%attr(755,root,root) %{_sbindir}/nanddump
%attr(755,root,root) %{_sbindir}/nandtest
%attr(755,root,root) %{_sbindir}/nandwrite
%attr(755,root,root) %{_sbindir}/nftl_format
%attr(755,root,root) %{_sbindir}/nftldump
%attr(755,root,root) %{_sbindir}/recv_image
%attr(755,root,root) %{_sbindir}/rfddump
%attr(755,root,root) %{_sbindir}/rfdformat
%attr(755,root,root) %{_sbindir}/serve_image
%attr(755,root,root) %{_sbindir}/sumtool
%attr(755,root,root) %{_sbindir}/ubi*
%{_mandir}/man1/mkfs.jffs2.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libmtd.a
%{_includedir}/mtd
