%bcond_with	tests		# build without tests

Summary:	a plugin for Rebar3 that bundles providers to interact with Hex
Name:		erlang-rebar3-hex
Version:	7.0.10
Release:	0.1
License:	APLv2
Group:		Development/Tools
Source0:	https://github.com/erlef/rebar3_hex/archive/refs/tags/v%{version}.tar.gz
# Source0-md5:	de158261831c87af76ac64ba7834177e
URL:		https://github.com/erlef/rebar3_hex/
BuildRequires:	erlang >= 2:17
%if %{without bootstrap}
BuildRequires:	erlang-rebar3
%endif
BuildRequires:	rpmbuild(macros) >= 2.035
%{?erlang_requires}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
A plugin for Rebar3 that bundles providers to interact with Hex.

%prep
%setup -q -n rebar3_hex-%{version}

%build
rebar3 hex build

%if %{with tests}
rebar3 eunit -v
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_libdir}/erlang/lib/rebar3_hex-%{version}/ebin

cp -p ebin/rebar.app $RPM_BUILD_ROOT%{_libdir}/erlang/lib/rebar3_hex-%{version}/ebin
cp -p ebin/*.beam $RPM_BUILD_ROOT%{_libdir}/erlang/lib/rebar3_hex-%{version}/ebin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%defattr(644,root,root,755)
%{_libdir}/erlang/lib/*-*
