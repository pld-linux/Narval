%define python_sitepkgsdir %(echo `python -c "import sys; print (sys.prefix + '/lib/python' + sys.version[:3] + '/site-packages/')"`)

Summary:	Python XMLTools
Summary(pl):	Narzêdzia XML dla Pythona
Name:		Narval
Version:	1.1
Release:	2
License:	GPL
Group:		Applications
Source0:	ftp://ftp.logilab.org/pub/narval/%{name}-%{version}.tar.gz
# Source0-md5:	6bf5fb6e2242fafbbf8c7cd65fb89f38
Source1:	horn.desktop
Patch0:		%{name}-apps_dir.patch
URL:		http://www.logilab.org/narval/
BuildRequires:	python >= 2.0
Requires:	python-PyXML
Requires:	python-4Suite
Requires:	python-xmlrpc
Requires:	python-xmltools
Requires:	python-pygtk-gtk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--record=INSTALLED_FILES

# these files seem missing after installation, so install them here
install share/dtd/* $RPM_BUILD_ROOT%{_datadir}/narval/dtd/
install share/transforms/Email/* $RPM_BUILD_ROOT%{_datadir}/narval/transforms/Email/

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Applications

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PKG-INFO README doc/ANNOUNCE* doc/CHANGELOG doc/CONTRIBUTORS doc/README.UNIX
%doc doc/*.xml doc/howtos doc/manuals
%attr(755,root,root) %{_bindir}/*
%{python_sitepkgsdir}/narval
%{_datadir}/narval
%{_applnkdir}/Applications/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
