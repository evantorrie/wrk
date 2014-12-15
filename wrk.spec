Name:		wrk
Version:        3.3.1
Release:	1%{?dist}
Summary:        HTTP benchmarking tool with Lua scripting	

%global commit 88aa6c52377889cbc707d12f94cbb1359b7392d5
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Group:	        Development/Tools
License:        Apache 2.0	
URL:            https://github.com/wg/wrk		
#Source0:        https://github.com/wg/wrk/archive/%{commit}/wrk-%{commit}.tar.gz	
Source0:        wrk-%{version}.tar.gz	

BuildRequires:  openssl-devel	
Requires:       openssl	

%description
wrk is a modern HTTP benchmarking tool capable of generating significant
load when run on a single multi-core CPU. It combines a multithreaded
design with scalable event notification systems such as epoll and kqueue.

An optional LuaJIT script can perform HTTP request generation, response
processing, and custom reporting. 

%prep
%autosetup


%build
make %{?_smp_mflags}


%install
mkdir -p %{buildroot}%{_bindir}
cp wrk %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/wrk
%doc README



%changelog
* Mon Dec 15 2014 Evan Torrie <evant@yahoo-inc.com> 3.4.1-1
- use default version as specified (evant@yahoo-inc.com)


* Wed Dec 10 2014 Evan Torrie <evant@yahoo-inc.com> 3.3.1-1
- check in the tgz file from github.com (evant@yahoo-inc.com)

* Wed Dec 10 2014 Evan Torrie <evant@yahoo-inc.com> 3.2.1-1
- new package built with tito


* Tue Dec 9 2014 Evan Torrie <evant@yahoo-inc.com> - 3.1.1-1
- First attempt at RPM packaging

