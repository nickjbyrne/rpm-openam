# rpm-openam

An RPM spec file to install the is Forgerock OpenAM Authentication, Authorization, Entitlement and Federation software.

To Build:

    sudo yum -y groupinstall "Development Tools"
    wget https://backstage.forgerock.com/downloads/enterprise/openam/openam12/12.0.0/OpenAM-12.0.0.zip -P ~/rpmbuild/SOURCES/
    rpmbuild -bb  ~/rpmbuild/SPECS/openam.spec --define "release 1"
