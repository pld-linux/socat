Summary:	Multipurpose relay
Name:		socat
Version:	1.3.1.0
Release:	1
License:	GPL
Group:		Networking/Utilities
URL:		http://www.dest-unreach.org/socat/
Source0:	http://www.dest-unreach.org/socat/download/%{name}-%{version}.tar.bz2
BuildRequires:	openssl-devel
BuildRequires:	libwrap-devel >= 7.6-30 
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Socat is a relay for bidirectional data transfer between two independent data channels. Each of these data channels may be a file, pipe, device (terminal or modem, etc.), socket (Unix, IP4, IP6 - raw, UDP, TCP), a client for SOCKS4, proxy CONNECT, or SSL, etc. It provides forking, logging, and dumping, different modes for interprocess communication, and many more options. It can be used, for example, as a TCP relay (one-shot or daemon), as a daemon-based socksifier, as a shell interface to Unix sockets, as an IP6 relay, for redirecting TCP-oriented programs to a serial line, or to establish a relatively secure environment (su and chroot) for running client or server shell scripts with network connections. 

%prep
%setup -q -n %{name}-1.3

%build
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGREPORTS CHANGES DEVELOPMENT EXAMPLES FAQ README SECURITY
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
