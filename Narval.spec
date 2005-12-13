Summary:	Python XMLTools
Summary(pl):	Narzêdzia XML dla Pythona
Name:		Narval
%define		_subname	narval
Version:	2.0.2
Release:	0.1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.logilab.org/pub/narval/%{_subname}-%{version}.tar.gz
# Source0-md5:	b996c2eb0eaf20a0569b311fecabd1e3
Source1:	horn.desktop
Patch0:		%{name}-apps_dir.patch
URL:		http://www.logilab.org/narval/
BuildRequires:	python >= 2.0
Requires:	python-4Suite
Requires:	python-PyXML
Requires:	python-modules
Requires:	python-pygtk-gtk
Requires:	python-xmltools
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
%setup -q -n %{_subname}-%{version}
#/%patch -p1

%build
CFLAGS="%{rpmcflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/narval/apps,%{_desktopdir},%{py_sitedir}/narval/}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--record=INSTALLED_FILES

# these files seem missing after installation, so install them here
cp -r   share/data/* $RPM_BUILD_ROOT%{_datadir}/narval/data/
install share/dtd/* $RPM_BUILD_ROOT%{_datadir}/narval/dtd/
install share/recipes/* $RPM_BUILD_ROOT%{_datadir}/narval/recipes/
cp -r   share/tests/* $RPM_BUILD_ROOT%{_datadir}/narval/tests

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

# move files to proper directories
cp -r $RPM_BUILD_ROOT%{_datadir}/python2.4/ $RPM_BUILD_ROOT%{_libdir}
cp -r $RPM_BUILD_ROOT/usr/etc/ $RPM_BUILD_ROOT
rm -frd $RPM_BUILD_ROOT/usr/etc/ $RPM_BUILD_ROOT%{_datadir}/python2.4/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc DEPENDS RECOMMENDS PKG-INFO README SUGGESTS
%doc doc/*.xml doc/technical_manual/*.xml doc/programmer_handbook/*.xml
%doc doc/*.pdf doc/technical_manual/*.pdf doc/programmer_handbook/*.pdf
%attr(755,root,root) %{_bindir}/*
#%{python_sitepkgsdir}/narval
%dir %{py_sitedir}/narval
%{py_sitedir}/narval/*
%{_datadir}/narval
%{_desktopdir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
