%define python_sitepkgsdir %(echo `python -c "import sys; print (sys.prefix + '/lib/python' + sys.version[:3] + '/site-packages/')"`)

Summary:	Python XMLTools
Name:		Narval
Version:	1.1
Release:	1
Source0:	ftp://ftp.logilab.org/pub/narval/%{name}-%{version}.tar.gz
Source1:	horn.desktop
Patch0:		%{name}-apps_dir.patch
License:	GPL
Group:		Applications
Group(de):	Applikationen
Group(pl):	Aplikacje
BuildRequires:	python >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	python-PyXML
Requires:	python-4Suite
Requires:	python-xmlrpc
Requires:	python-xmltools
Requires:	python-pygtk
Url:		http://www.logilab.org/narval/index.html

%description
NARVAL is the first software agent available as free software (Gnu
Public License).

Narval is the acronym of "Network Assistant Reasoning with a
Validating Agent Language".

Narval is a framework (language + interpreter + GUI/IDE) dedicated to
the setting up of intelligent personal assistants (IPAs). An
Intelligent Personal Assitant is a companion that will help you in
your daily work in the information world.

%description -l pl
NARVAL to pierwszy programowy agent dostêpny jako Wolne
Oprogramowanie.

Narval to skrót od "Network Assistant Reasoning with a Validating
Agent Language".

Narval to szkielet (jêzyk + interpreter + GUI/IDE) dedykowany
tworzeniu inteligentnych osobistych asystentów. Inteligentny osobisty
asystent to towarzysz, który pomo¿e ci w codziennej pracy w ¶wiecie
informacji.

%prep
%setup -q
%patch -p1

%build
CFLAGS="%{rpmcflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/narval/apps,%{_applnkdir}/Applications}
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Applications

gzip -9fn PKG-INFO README doc/ANNOUNCE* doc/CHANGELOG doc/CONTRIBUTORS doc/README.UNIX


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz doc/*.xml doc/howtos doc/manuals
%attr(755,root,root) %{_bindir}/*
%{python_sitepkgsdir}/narval
%{_datadir}/narval
%{_applnkdir}/Applications/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
