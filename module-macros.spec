Name: module-macros
Version: 0.1
Release: 1%{?dist}
Summary: Macros for creating modules

License: MIT
Source0: macros.module

BuildArch: noarch

%description
This package provides macros for module development.

%prep

%build

%install
mkdir -p %{buildroot}%{rpmmacrodir}
install -m 644 %{SOURCE0} %{buildroot}%{rpmmacrodir}

%files
%{rpmmacrodir}
%{rpmmacrodir}/macros.module

%changelog
* Wed Jun 14 2017 clime <clime@redhat.com> 0.1-1
- Initial version
