# cuneiform-convert
To run this repository, first install imagemagick and [autotrace](https://github.com/autotrace/autotrace). Images are originally from [this](https://github.com/oaregithub/OAsigns) repository.
# How to use
Run `png_to_svg.py`, and then, if you want the filenames to contain the q-codes, you can also run `fix_filenames.py`.
Make sure you also install SPARQLWrapper, PIL, and BeautifulSoup.

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

# Caveats
The script does its best to remove transparency from images. Note that some regions of transparency cannot be removed. Within a sign, any empty white space enclosed on all sides will not become transparent. In short, the exterior of the image becomes transparent, but "pockets" of transparency within the sign do not.
