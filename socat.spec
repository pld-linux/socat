Summary:	Multipurpose relay
Summary(pl):	Przeka�nik o wielu zastosowaniach
Name:		socat
Version:	1.4.0.1
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.dest-unreach.org/socat/download/%{name}-%{version}.tar.bz2
# Source0-md5:	b0e7b00f9959239232f97d3cd1839e8f
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

%description -l pl
Socat to przeka�nik do dwukierunkowego przesy�ania danych pomi�dzy
dwoma niezale�nymi kana�ami danych. Ka�dy z tych kana��w mo�e by�
plikiem, potokiem, urz�dzeniem (terminalem, modemem itp.), gniazdem
(uniksowym, IPv4, IPv6 - surowym, UDP, TCP), klientem SOCKS4, proxy
CONNECT, albo SSL itp. Socat ma mo�liwo�� forkowania, logowania i
zrzucania danych, r�ne tryby komunikacji mi�dzyprocesowej oraz wiele
innych opcji. Mo�e by� u�ywane np. jako przeka�nik TCP (jednorazowy
lub demon), jako demon przesy�aj�cy przez SOCKS, jako interfejs dla
pow�oki do gniazd uniksowych, jako przeka�nik IPv6, do
przekierowywania program�w korzystaj�cych z TCP na port szeregowy albo
do stworzenia wzgl�dnie bezpiecznego �rodowiska (su i chroot) do
uruchamiania klienckich lub serwerowych skrypt�w pow�oki z
po��czeniami sieciowymi.

%prep
%setup -q -n %{name}-1.4

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
