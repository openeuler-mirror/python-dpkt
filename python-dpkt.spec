%global _empty_manifest_terminate_build 0
Name:		python-dpkt
Version:	1.9.7.2
Release:	1
Summary:	fast, simple packet creation / parsing, with definitions for the basic TCP/IP protocols
License:	BSD
URL:		https://github.com/kbandla/dpkt
Source0:	https://files.pythonhosted.org/packages/95/51/923b370880eff9b62fe4fe965a916da709022a02669c670731da69088e93/dpkt-1.9.7.2.tar.gz
BuildArch:	noarch


%description
Fast, simple packet creation and parsing library
with definitions for the basic TCP/IP protocols.

%package -n python3-dpkt
Summary:	fast, simple packet creation / parsing, with definitions for the basic TCP/IP protocols
Provides:	python-dpkt
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools

%description -n python3-dpkt
Fast, simple packet creation and parsing library
with definitions for the basic TCP/IP protocols.

%package help
Summary:	Development documents and examples for dpkt
Provides:	python3-dpkt-doc

%description help
Development documents and examples for dpkt

%prep
%autosetup -n dpkt-1.9.7.2

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-dpkt -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Thu Sep 09 2021 Python_Bot <Python_Bot@openeuler.org> - 1.9.7.2-1
- Package Init
