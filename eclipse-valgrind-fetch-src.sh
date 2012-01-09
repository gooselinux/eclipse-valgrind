#!/bin/sh
usage='usage: $0 <tag>'
name=eclipse-valgrind
tag=$1
tar_name=$name-fetched-src-$tag

if [ "x$tag"x = 'xx' ]; then
   echo >&2 "$usage"
   exit 1
fi

rm -fr $tar_name 

# Fetch plugins/features
for f in \
org.eclipse.linuxtools.valgrind-feature \
org.eclipse.linuxtools.valgrind.cachegrind \
org.eclipse.linuxtools.valgrind.core \
org.eclipse.linuxtools.valgrind.doc \
org.eclipse.linuxtools.valgrind.launch \
org.eclipse.linuxtools.valgrind.massif \
org.eclipse.linuxtools.valgrind.memcheck \
org.eclipse.linuxtools.valgrind.ui \
org.eclipse.linuxtools.valgrind.ui.editor \
; do
svn export svn://dev.eclipse.org/svnroot/technology/org.eclipse.linuxtools/valgrind/tags/$tag/$f $tar_name/$f
done

# create archive
tar -cjf $tar_name.tar.bz2 $tar_name/*
