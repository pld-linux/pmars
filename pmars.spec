%define		_fver	%(echo %{version} | tr . _)
Summary:	Portable corewar system with ICWS'94 extensions
Summary(pl.UTF-8):	Przenośny system Wojen Rdzeniowych z rozszerzeniami ICWS'94
Name:		pmars
Version:	0.8.6
Release:	4
License:	Freeware
Group:		Applications/Games
Source0:	http://www.koth.org/pmars/%{name}-%{_fver}_tar.gz
# Source0-md5:	eaea26fc7df36a6e6e851767e5ae4c25
Source1:	corewars.tar.gz
# Source1-md5:	4df24a0f88d0dc4f66f67a4e4fa596cc
BuildRequires:	XFree86-devel
BuildRequires:	groff
BuildRequires:	ncurses-devel
BuildRequires:	vim-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Core War is a game in which two or more virus-like programs fight
against each other in a simulated memory space or core. Core War
programs are written in an assembly language called Redcode which is
interpreted by a Core War simulator or MARS (Memory Array Redcode
Simulator). The object of the game is to prevent the other program(s)
from executing. For more information about Core War check out the
usenet newsgroup rec.games.corewar and its FAQ list
ftp://rtfm.mit.edu/pub/usenet/games/corewar-faq

%description -l pl.UTF-8
Wojny Rdzeniowe są grą w której dwa lub więcej programów podobnych do
wirusów walczy ze sobą w symulowanej przestrzeni adresowej (rdzeniu.)
Programy te pisane są w assemblerze nazwanym Redcode, który jest
interpretowany przez symulator Wojen Rdzeniowych, MARS (Memory Array
Redcode Simulator.) Celem gry jest zapobieżenie wykonywaniu
pozostałych programów. Aby dowiedzieć się więcej o Wojnach Rdzeniowych
sprawdź grupę dyskusyjną rec.games.corewar i jej FAQ
ftp://rtfm.mit.edu/pub/usenet/games/corewar-faq

%package x11
Summary:	pmars with X11 graphics
Summary(pl.UTF-8):	pmars z reprezentacją na X11
Group:		X11/Applications/Games

%description x11
pmars with X11 graphics.

%description x11 -l pl.UTF-8
pmars z reprezentacją na X11.

%package curses
Summary:	pmars with curses graphics
Summary(pl.UTF-8):	pmars z reprezentacją na curses
Group:		Applications/Games

%description curses
pmars with curses graphics.

%description curses -l pl.UTF-8
pmars z reprezentacją na curses.

%prep
%setup -q -a 1

%build
# X11 version
%{__make} CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DEXT94 -DXWINGRAPHX" \
	LIB="%{rpmldflags} -L%{_prefix}/X11R6/%{_lib} -lX11" \
	MAINFILE="xpmars"
%{__make} clean

# curses version
%{__make} CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DEXT94 -DCURSESGRAPHX -I/usr/include/ncurses" \
	LIB="%{rpmldflags} -lncurses" \
	MAINFILE="cpmars"
%{__make} clean

# batch version
%{__make} CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DEXT94" \
	LIB="%{rpmldflags}"

# TODO: svgalib version

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6}

install {,c,x}pmars	$RPM_BUILD_ROOT%{_bindir}
install pmars.6		$RPM_BUILD_ROOT%{_mandir}/man6

mkdir examples
for i in *.red ; do mv -f $i examples ; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CONTRIB primer.94 primer.cdb redcode.ref whatsnew.080 *.opt *.mac
%doc examples
%lang(pl) %doc corewars-pl/*
%attr(755,root,root) %{_bindir}/pmars
%{_mandir}/man6/*

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xpmars

%files curses
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cpmars
