Summary:	a plugin for Rebar3 that bundles providers to interact with Hex
Name:		erlang-rebar3-hex
Version:	7.1.0
Release:	1
License:	APLv2
Group:		Development/Tools
Source0:	https://repo.hex.pm/tarballs/rebar3_hex-%{version}.tar
# Source0-md5:	7bb101e1ad41629979a289200cfce09a
# Disable dev-only project plugins and Hex dep fetching during build;
# runtime behavior comes from Requires: erlang-hex-core and erlang-verl.
Patch0:		offline-local-deps.patch
URL:		https://hex.pm/packages/rebar3_hex
BuildRequires:	erlang >= 2:17
BuildRequires:	erlang-rebar3
BuildRequires:	rpmbuild(macros) >= 2.035
Requires:	erlang-hex-core
Requires:	erlang-rebar3
Requires:	erlang-verl
%{?erlang_requires}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
A plugin for Rebar3 that bundles providers to interact with Hex.

%prep
%setup -q -T -c -a 0 -n rebar3_hex-%{version}
tar -xzf contents.tar.gz
%patch -P0 -p1
rm -f rebar.lock

%build
rebar3 compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/erlang/lib/rebar3_hex-%{version}
cp -rp _build/default/lib/rebar3_hex/* $RPM_BUILD_ROOT%{_libdir}/erlang/lib/rebar3_hex-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{_libdir}/erlang/lib/rebar3_hex-%{version}
