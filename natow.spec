Summary:	N.A.T.O.W - nasty armoured tanks of war!
Summary(pl):	N.A.T.O.W - paskudne opancerzone czo�gi wojenne!
Name:		natow
Version:	0.2.10
Release:	2
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	http://download.sourceforge.net/natow/%{name}-%{version}.tar.gz
Source1:	http://download.sourceforge.net/natow/%{name}-images-0.2.5.tar.gz
Source2:	http://download.sourceforge.net/natow/%{name}-levels-0.2.5.tar.gz
Source3:	http://download.sourceforge.net/natow/%{name}-models-0.2.5.tar.gz
Patch0:		%{name}-install.patch
Patch1:		%{name}-CFLAGS_and_LIBS.patch
Patch2:		%{name}-chdir.patch
BuildRequires:	glass-devel
BuildRequires:	glut-devel
URL:		http://natow.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1
%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
N.A.T.O.W is a 3D (openGL) tank game based loosely on scorched earth
(or the newer xscorch), but including a single player element. The
goal is to kill the other tanks and as much terrain as possible. A
project goal is to add useless objects in that can be additionally
destroyed, like buildings, alien artifacts and of course, defenseless
baby bunnies. (TODO shows, we have to wait for full playability)

%description -l pl
N.A.T.O.W to gra czo�gami bazuj�ca na scorched earth (tak�e xscorch) w
technologii 3D OpenGL. Celem jest niszczenie innych czo�g�w i
generalnie wszystkiego co si� rusza i nierusza. (TODO pokazuje, �e
jeszcze troch� trzeba poczeka� na maksymaln� grywalno��)

%prep
%setup -q -a 1 -a 2 -a 3
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build

CC=%{__cc}
LDFLAGS="-L%{libdir}"

export CC LDFLAGS

%{__make} -C src RPM_OPT_FLAGS="%{rpmcflags}" all

cp src/natow .

%install
rm -rf $RPM_BUILD_ROOT

%{__make} INSTALLDIR="$RPM_BUILD_ROOT/%{_prefix}" install

cp -R models $RPM_BUILD_ROOT%{_datadir}/%{name}

gzip -9nf README TODO Changelog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%doc *.gz
%{_datadir}/%{name}
%{_bindir}/*
