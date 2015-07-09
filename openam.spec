%define version 12.0.0
%{!?release: %{!?release: %define release 1}}

Summary: OpenAM provides open source Authentication, Authorization, Entitlement and Federation.
Name: openam
Version: %{version}
Release: %{release}%{?dist}
License: CDDL
Group: Applications/System
URL: http://openam.forgerock.org/
Source0: https://backstage.forgerock.com/downloads/enterprise/openam/openam12/12.0.0/OpenAM-12.0.0.zip
Source1: openam/SSOConfiguratorTools-12.0.0.zip
Source2: openam/SSOAdminTools-12.0.0.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: java, tomcat6
%description
The only “all-in-one” access management solution that includes Authentication, SSO, Authorization, Federation, Entitlements, Adaptive Authentication, Strong Authentication, and Web Services Security, in a single, unified product.

%package configurator-tools
Summary: OpenAM configurator support tools
%description configurator-tools
See OpenAM package

%package admin-tools
Summary: OpenAM administrative support tools
%description admin-tools
See OpenAM package

%prep
%setup -n %{name}
unzip -x SSOAdminTools-%{version}.zip -d admin-tools
unzip -x SSOConfiguratorTools-%{version}.zip -d configurator-tools

# We don't want any perl dependecies in this RPM:
%define __perl_requires /bin/true

%build

%install
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}/var/lib/tomcat6/webapps
cp OpenAM-%{version}.war %{buildroot}/var/lib/tomcat6/webapps/openam.war

pwd
ls
%{__install} -d %{buildroot}/opt/openam
%{__cp} -a configurator-tools %{buildroot}/opt/openam/
%{__cp} -a admin-tools %{buildroot}/opt/openam/


%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%pre

%post

%preun

%postun

%files
%attr(750, tomcat, tomcat) /var/lib/tomcat6/webapps/openam.war

%files configurator-tools
%attr(-, tomcat, tomcat)  /opt/openam/configurator-tools

%files admin-tools
%attr(-, tomcat, tomcat)  /opt/openam/admin-tools

%changelog
* Thu Jul 09 2015 Nick Byrne <nick@incension.com
- Initial version of openam 12.0.0
