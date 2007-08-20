%define name sisctrl
%define version 0.0
%define subrelease 20051202
%define release %mkrel %{subrelease}.3
Summary:  A tool for manipulating SIS driver parameters 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.winischhofer.net/sis/%{name}-%{version}.%{subrelease}.tar.gz
License: GPL
Group: System/Kernel and hardware
Url: http://www.winischhofer.net/linuxsisvga.shtml#download
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: X11-devel , glib2-devel , gtk+2-devel

%description
A gtk+2 tool for manipulating various driver parameters during runtime

%prep
%setup -q -n %{name}-%{version}.%{subrelease} 
%configure

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/sisctrl
%{_mandir}/man1/sisctrl.1*
