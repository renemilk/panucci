#
# This file is part of Panucci.
# Copyright (c) 2008-2010 The Panucci Audiobook and Podcast Player Project
#
# Panucci is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Panucci is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Panucci.  If not, see <http://www.gnu.org/licenses/>.
#

PREFIX ?= /usr
DESTDIR ?= /

MESSAGESPOT = data/messages.pot

TRANSLATION_SOURCES=$(wildcard src/panucci/*.py) $(wildcard src/panucci/backends/*.py)

PYTHON ?= python

data/panucci.service: data/panucci.service.in
	sed 's|@INSTALL_PREFIX@|'/$(PREFIX)'|g' < data/panucci.service.in > data/panucci.service


install: mo data/panucci.service
	$(PYTHON) setup.py install --root=$(DESTDIR) --prefix=$(PREFIX)

test:
	PYTHONPATH=src/ $(PYTHON) bin/panucci --debug

po:
	xgettext -k_ -kN_ --from-code utf-8 -Lpython -o $(MESSAGESPOT) $(TRANSLATION_SOURCES)
	for langfile in data/po/*.po; do msgmerge -q -U $${langfile} $(MESSAGESPOT); done

mo:
	for langfile in data/po/*.po; do \
	  mo_dir="data/locale/`basename $${langfile} .po`/LC_MESSAGES/"; \
	  mkdir -p $${mo_dir}; \
	  msgfmt $${langfile} -o $${mo_dir}/panucci.mo; \
	done

clean:
	find src/ -name '*.pyc' -exec rm '{}' \;
	find src/ -name '*.pyo' -exec rm '{}' \;
	rm -rf build data/locale
	rm -f data/panucci.service data/po/*~

distclean: clean
	rm -rf dist

.PHONY: install test po mo clean distclean

