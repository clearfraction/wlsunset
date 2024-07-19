Name     : wlsunset
Version  : 0.4.0
Release  : 1
URL      : https://git.sr.ht/~kennylevinsen/wlsunset
Source0  : https://git.sr.ht/~kennylevinsen/wlsunset/archive/%{version}.tar.gz#/wlsunset-%{version}.tar.gz
Summary  : Day/night gamma adjustments for Wayland compositors
Group    : Development/Tools
License  : MIT
BuildRequires : cmake
BuildRequires : buildreq-meson
BuildRequires : wayland-dev wayland-protocols-dev

%description
Day/night gamma adjustments for Wayland compositors

%prep
%setup -q

%build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256  "
export FCFLAGS="$CFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256  "
export FFLAGS="$CFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256  "
export CXXFLAGS="$CXXFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256  "
meson \
    --libdir=lib64 --prefix=/usr \
    --buildtype=plain builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install
rm -rf %{buildroot}/usr/share/man

%files
%defattr(-,root,root,-)
/usr/bin/wlsunset
