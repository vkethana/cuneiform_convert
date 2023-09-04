# cuneiform-convert
To run this repository, first install imagemagick and [autotrace](https://github.com/autotrace/autotrace).
# How to use
Run `png_to_svg.py`, and then, if you want the filenames to contain the q-codes, you can also run `fix_filenames.py`.

# How to install imagemagick and autotrace (on MacOS)
```
export PATH="/usr/local/opt/gettext/bin:$PATH"
perl -MCPAN -e 'install XML::Parser'
brew install gettext intltool glib libtool autoconf automake pkg-config
brew install imagemagick graphicsmagick pstoedit
git clone https://github.com/autotrace/autotrace.git
cd autotrace
autoreconf -ivf
intltoolize --force
aclocal
test -e /usr/local/lib/pkgconfig/libffi.pc || ln -s ../../Cellar/libffi/3.2.1/lib/pkgconfig/libffi.pc /usr/local/lib/pkgconfig/
sh ./configure MAGICK_CFLAGS="$(pkg-config graphicsmagick --cflags)" MAGICK_LIBS="$(pkg-config graphicsmagick --libs)"
make
make install
```
(from [this link](https://github.com/autotrace/autotrace/blob/master/INSTALL_OSX.md))
