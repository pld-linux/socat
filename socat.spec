Summary:	Multipurpose relay
Summary(pl.UTF-8):   Przekaźnik o wielu zastosowaniach
Name:		socat
Version:	1.5.0.0
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.dest-unreach.org/socat/download/%{name}-%{version}.tar.bz2
# Source0-md5:	84b709de13e236198a4606fb4b80e123
URL:		http://www.dest-unreach.org/socat/
BuildRequires:	libwrap-devel >= 7.6-30
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Socat is a relay for bidirectional data transfer between two
independent data channels. Each of these data channels may be a file,
pipe, device (terminal or modem, etc.), socket (Unix, IPv4, IPv6 -
raw, UDP, TCP), a client for SOCKS4, proxy CONNECT, or SSL, etc. It
provides forking, logging, and dumping, different modes for
interprocess communication, and many more options. It can be used, for
example, as a TCP relay (one-shot or daemon), as a daemon-based
socksifier, as a shell interface to Unix sockets, as an IPv6 relay,
for redirecting TCP-oriented programs to a serial line, or to
establish a relatively secure environment (su and chroot) for running
client or server shell scripts with network connections.

%description -l pl.UTF-8
Socat to przekaźnik do dwukierunkowego przesyłania danych pomiędzy
dwoma niezależnymi kanałami danych. Każdy z tych kanałów może być
plikiem, potokiem, urządzeniem (terminalem, modemem itp.), gniazdem
(uniksowym, IPv4, IPv6 - surowym, UDP, TCP), klientem SOCKS4, proxy
CONNECT, albo SSL itp. Socat ma możliwość forkowania, logowania i
zrzucania danych, różne tryby komunikacji międzyprocesowej oraz wiele
innych opcji. Może być używane np. jako przekaźnik TCP (jednorazowy
lub demon), jako demon przesyłający przez SOCKS, jako interfejs dla
powłoki do gniazd uniksowych, jako przekaźnik IPv6, do
przekierowywania programów korzystających z TCP na port szeregowy albo
do stworzenia względnie bezpiecznego środowiska (su i chroot) do
uruchamiania klienckich lub serwerowych skryptów powłoki z
połączeniami sieciowymi.

%prep
%setup -q
sed -i -e 's#-lssl#-lssl -lcrypto#g' configure*

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
