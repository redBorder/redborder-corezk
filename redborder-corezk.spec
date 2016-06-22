Name:    redborder-corezk
Version: %{__version}
Release: %{__release}%{?dist}

License: GNU AGPLv3
URL: https://github.com/redBorder/redborder-corezk
#Source0: %{name}-%{version}.tar.gz

#BuildRequires: 

Summary: redborder corezk role. 
Group:  Meta-packages/role 

Requires: druid 
Requires: zookeeper
Requires: rb-monitor
Requires: rb-discover
Requires: memcached
Requires: chef-server

%description
%{summary}

%prep
%setup -qn %{name}-%{version}

%changelog
* Wed Jun 22 2016 Alberto Rodríguez <arodriguez@redborder.com> - 1.0.0-1
- first spec version

