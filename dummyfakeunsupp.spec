Name:		dummyfakeunsupp
%define _empty_manifest_terminate_build 0
Version:	0
Release:	1
Summary:	Fake build test
Group:		System/Configuration/Packaging
License:	Public Domain

BuildArch:	noarch

%ifarch %{riscv}
# Make basesystem happy
Provides:	kernel = 5.2.14-1
Provides:	bootloader
Provides:	pinentry
%endif

Requires:	coreutils
Provides:	/bin/true
Provides:	/bin/false
Provides:	openlitespeed
Provides:	xdg-desktop-portal-implementation

%description
Fake build test

This package is bogus and just used to test various failures.

Do not install this package unless you are ABF

%prep

%build

%install

%files
