# $Id: freepbx-src.spec,v 1.2 2013/05/22 02:40:06 unnilennium Exp $
# Authority: vip-ire
# Name: Daniel Berteaud

%define version 2.11.0.38
%define release 2
%define name freepbx-src


Summary:        FreePBX Sources
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
License:        GPL
Group:          System/Servers

Source0:	freepbx-%{version}.tar.gz
#Source1:	panel-0.1.tgz

BuildRoot:      /var/tmp/%{name}-%{version}-%{release}-buildroot
URL:            http://www.freepbx.org/

BuildArch:	noarch

BuildRequires:	e-smith-devtools
Requires: php-process

AutoReqProv:    no

%description
FreePBX is a Standardised Implementation of Asterisk that gives you a GUI to manage your system. If you have looked into Asterisk, you would know that it does not come with any built in programming. You cannot plug a phone into it and make it work without editing configuration files, writing dialplans, and various messing about. FreePBX simplifies this by giving you a pre-written set of dialplans that allow you to have a fully functional PBX pretty much straight away.
This package only contains the sources, and should be installed with smeserver-freepbx

%changelog
* Sun Jun 21 2015 stephane de Labrusse <stephdl@de-labrusse.fr> 2.11.0.38
- Initial release to sme9

* Tue May 21 2013 JP Pialasse <tests@pialasse.com> [2.5.1-2]
- add php-process requirement bug [SME: 7382]

* Tue Mar 03 2009 daniel B. <daniel@firewall-services.com> [2.5.1-1]
- Add missing %changelog section in spec file
- Add e-smith-devtools as a build dependency

* Mon Aug 04 2008 daniel B. <daniel@firewall-services.com> [2.5.1-0]
- initial release based on freepbx 2.5.1

%prep

%setup -q -n freepbx-%{version}

%build
# Extract freePBX archive
%{__mkdir_p} root/usr/share/freepbx/sources
tar xzf %{SOURCE0} -C root/usr/share/freepbx/sources
# Extract panel module (not an official module yet)
#tar xzf %{SOURCE1} -C root/usr/share/freepbx/sources/freepbx-%{version}/amp_conf/htdocs/admin/modules
ln -s /usr/share/freepbx/sources/freepbx-%{version} root/usr/share/freepbx/sources/freepbx

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
	> %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)


