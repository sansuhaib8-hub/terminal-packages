TERMUX_PKG_HOMEPAGE=https://www.zlib.net/
TERMUX_PKG_DESCRIPTION="Compression library implementing the deflate compression method found in gzip and PKZIP"
TERMUX_PKG_LICENSE="ZLIB"
TERMUX_PKG_MAINTAINER="@termux"
TERMUX_PKG_VERSION=1.3.1
TERMUX_PKG_REVISION=0
TERMUX_PKG_SRCURL=https://github.com/madler/zlib/releases/download/v$TERMUX_PKG_VERSION/zlib-$TERMUX_PKG_VERSION.tar.gz
TERMUX_PKG_SHA256=9a93b2b7dfdac77ceba5a558a580e74667dd6fede4585b91eefb60f03b72df23
TERMUX_PKG_BREAKS="ndk-sysroot (<< 19b-3), zlib-dev"
TERMUX_PKG_REPLACES="ndk-sysroot (<< 19b-3), zlib-dev"

termux_step_pre_configure() {
	if [ "$TERMUX_ARCH" = "aarch64" ]; then
		CFLAGS+=" -march=armv8-a+crc"
		CXXFLAGS+=" -march=armv8-a+crc"
	fi

	# Fix relocation issues when linking with libz.a
	CFLAGS+=" -fPIC"
	CXXFLAGS+=" -fPIC"

	# Fix linker script error for zlib 1.3
	LDFLAGS+=" -Wl,--undefined-version"
}

termux_step_configure() {
	"$TERMUX_PKG_SRCDIR/configure" --prefix=$TERMUX_PREFIX --shared
}
