Summary:	Testing framework for infrastructure software
Summary(pl.UTF-8):	Szkielet testów do oprogramowania infrastrukturalnego
Name:		kyua
Version:	0.13
Release:	1
License:	BSD
Group:		Development/Tools
#Source0Download: https://github.com/jmmv/kyua/releases/download
Source0:	https://github.com/jmmv/kyua/releases/download/kyua-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	475203c0877ebe739edf8b8dff4606ec
URL:		https://github.com/jmmv/kyua
BuildRequires:	libatf-c++-devel >= 0.17
BuildRequires:	libatf-sh-devel >= 0.15
BuildRequires:	liblutok-devel >= 0.4
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel >= 3.6.22
Requires:	liblutok >= 0.4
Requires:	sqlite3 >= 3.6.22
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		pkgtestsdir	%{_libexecdir}/%{name}/tests

%description
Kyua is a testing framework for infrastructure software, originally
designed to equip BSD-based operating systems with a test suite. This
means that Kyua is lightweight and simple, and that Kyua integrates
well with various build systems and continuous integration frameworks.

Kyua features an expressive test suite definition language, a safe
runtime engine for test suites and a powerful report generation
engine.

Kyua is for both developers and users, from the developer applying a
simple fix to a library to the system administrator deploying a new
release on a production machine.

Kyua is able to execute test programs written with a plethora of
testing libraries and languages. The library of choice is ATF, for
which Kyua was originally designed, but simple, framework-less test
programs and TAP-compliant test programs can also be executed through
Kyua.

%description -l pl.UTF-8
Kyua to szkielet testów dla oprogramowania infrastrukturalnego,
pierwotnie zaprojektowany z myślą o stworzeniu zestawu testów dla
systemów operacyjnych opartych na BSD. Oznacza to, że Kyua jest
lekki i prosty oraz dobrze integruje się z różnymi systemami
budowania i szkieletami ciągłej integracji.

Kyua zawiera język definiowania zestawów testów, bezpieczny silnik
uruchomieniowy do zestawów testów oraz potężny silnik generowania
raportów.

Kyua jest przeznaczony zarówno dla programistów, jak i użytkowników;
od programistów nakładających prostą poprawkę do biblioteki po
administratorów systemów wdrażających nowe wydanie na maszynie
produkcyjnej.

Kyua potrafi uruchamiać programy testowe napisane z użyciem wielu
bibliotek testowych i języków. Biblioteką pierwszego wyboru jest ATF,
dla której Kyua pierwotnie został zaprojektowany, ale można uruchamiać
także proste programy testowe pisane bez szkieletu oraz zgodne z TAP.

%package tests
Summary:	Runtime tests of the Kyua toolchain
Summary(pl.UTF-8):	Testy uruchomieniowe narzędzi Kyua
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	libatf-c++ >= 0.17
Requires:	libatf-sh >= 0.15

%description tests
Runtime tests of the Kyua toolchain.

%description tests -l pl.UTF-8
Testy uruchomieniowe narzędzi Kyua.

%prep
%setup -q

%build
%configure \
	--with-atf \
	--without-doxygen

%{__make} \
	pkgtestsdir=%{pkgtestsdir} \
	testsdir=%{pkgtestsdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgtestsdir=%{pkgtestsdir} \
	testsdir=%{pkgtestsdir} \
	doc_DATA=

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CONTRIBUTORS LICENSE NEWS.md README.md
%attr(755,root,root) %{_bindir}/kyua
%{_datadir}/%{name}
%{_mandir}/man1/kyua.1*
%{_mandir}/man1/kyua-*.1*
%{_mandir}/man5/kyua.conf.5*
%{_mandir}/man5/kyuafile.5*

%files tests
%defattr(644,root,root,755)
%dir %{_libexecdir}/%{name}
%{pkgtestsdir}
