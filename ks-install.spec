%global forgeurl https://github.com/cmadamsgit/ks-install
%global commit TBD
%forgemeta

Release:	0.1%{?dist}
License:	GPLv3
BuildArch:	noarch
BuildRequires:	perl-generators perl-podlators
Requires:	virt-install
Recommends:	swtpm-tools

%description
Take a Fedora/CentOS/RHEL kickstart file and make a VM

%prep
%forgesetup

%build
pod2man ks-libvirt > ks-libvirt.1

%install
install -D -m0755 ks-libvirt %{buildroot}%{_bindir}/ks-libvirt
install -D -m0644 ks-libvirt.1 %{buildroot}%{_mandir}/man1/ks-libvirt.1

%files
%license LICENSE
%{_bindir}/*
%{_mandir}/man*/*

%changelog
* Fri Jan 14 2022 Chris Adams <linux@cmadams.net> 1-1
- initial package
