Name:    redborder-corezk
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch

License: GNU AGPLv3
URL: https://github.com/redBorder/redborder-corezk
Source0: %{name}-%{version}.tar.gz

#BuildRequires: 

Summary: redborder corezk role. 
Group:  Meta-packages/role 

Requires: druid 
Requires: zookeeper
Requires: rb_monitor
Requires: rb-discover
Requires: memcached
Requires: chef-server-core
Requires: postgresql-pgpool-II

%description
%{summary}

%prep
%setup -qn %{name}-%{version}

%build

%install
mkdir -p %{buildroot}/usr/share/%{name}
install -D -m 0644 README.md %{buildroot}/usr/share/%{name}

%files
%defattr(644,root,root)
/usr/share/%{name}

%changelog
* Wed Jun 22 2016 Alberto Rodríguez <arodriguez@redborder.com> - 1.0.0-1
- first spec version

