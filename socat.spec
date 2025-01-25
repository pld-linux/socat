Summary:	Multipurpose relay
Summary(pl.UTF-8):	Przekaźnik o wielu zastosowaniach
Name:		socat
Version:	1.8.0.2
Release:	1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://www.dest-unreach.org/socat/download/%{name}-%{version}.tar.bz2
# Source0-md5:	7272fe53d51c63ca0e08e0339681803a
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Source3:	%{name}.tmpfiles
URL:		http://www.dest-unreach.org/socat/
BuildRequires:	gettext-tools
BuildRequires:	libwrap-devel >= 7.6-30
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.644
BuildRequires:	sed >= 4.0
BuildRequires:	yodl
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts >= 0.4.1.26-2
Requires:	systemd-units >= 38
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

%{__sed} -i -e 's#-lssl#-lssl -lcrypto#g' configure*

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	CFLAGS="%{rpmcflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,/var/run/%{name}} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig,%{name}} \
	$RPM_BUILD_ROOT%{systemdtmpfilesdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE3} $RPM_BUILD_ROOT%{systemdtmpfilesdir}/%{name}.conf

cat >> $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/example.conf <<'EOF'
# socat [options] <bi-address> <bi-address>
OPTIONS=""
BIADDRESS1="UNIX-LISTEN:/var/lib/mysql/mysql.sock,fork,user=mysql,group=mysql,mode=777"
BIADDRESS2="TCP:localhost:3306"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add %{name}
%service socat restart "socat"

%preun
if [ "$1" = "0" ]; then
	%service socat stop
	/sbin/chkconfig --del socat
fi

%files
%defattr(644,root,root,755)
%doc BUGREPORTS CHANGES DEVELOPMENT EXAMPLES FAQ README SECURITY
%dir %{_sysconfdir}/%{name}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/example.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/socat
%attr(754,root,root) /etc/rc.d/init.d/socat
%attr(755,root,root) %{_bindir}/filan
%attr(755,root,root) %{_bindir}/procan
%attr(755,root,root) %{_bindir}/socat
%attr(755,root,root) %{_bindir}/socat-broker.sh
%attr(755,root,root) %{_bindir}/socat-chain.sh
%attr(755,root,root) %{_bindir}/socat-mux.sh
%attr(755,root,root) %{_bindir}/socat1
%dir /var/run/%{name}
%{systemdtmpfilesdir}/%{name}.conf
%{_mandir}/man1/socat.1*
%{_mandir}/man1/socat1.1*
