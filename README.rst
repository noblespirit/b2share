.. This file is part of EUDAT B2Share.
   Copyright (C) 2016, CERN.

   B2Share is free software; you can redistribute it and/or
   modify it under the terms of the GNU General Public License as
   published by the Free Software Foundation; either version 2 of the
   License, or (at your option) any later version.

   B2Share is distributed in the hope that it will be useful, but
   WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with B2Share; if not, write to the Free Software Foundation, Inc.,
   59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

   In applying this license, CERN does not
   waive the privileges and immunities granted to it by virtue of its status
   as an Intergovernmental Organization or submit itself to any jurisdiction.

B2SHARE
=======
.. image:: https://img.shields.io/travis/EUDAT-B2SHARE/b2share.svg
        :target: https://travis-ci.org/EUDAT-B2SHARE/b2share

.. image:: https://coveralls.io/repos/github/EUDAT-B2SHARE/b2share/badge.svg?branch=master
        :target: https://coveralls.io/github/EUDAT-B2SHARE/b2share?branch=master

.. image:: https://img.shields.io/github/tag/EUDAT-B2SHARE/b2share.svg
        :target: https://github.com/EUDAT-B2SHARE/b2share/releases

.. image:: https://img.shields.io/github/license/EUDAT-B2SHARE/b2share.svg
        :target: https://github.com/EUDAT-B2SHARE/b2share/blob/master/LICENSE

B2SHARE is an user-friendly, secure, robust, reliable, and trusted service to share and publish your **research data**. B2SHARE is able to add value to your research data via (domain tailored) metadata, and assigning Persistent Identifiers `PIDs <http://www.pidconsortium.eu/>`_ to ensure long-lasting access and references. B2SHARE is one of the B2 services developed via `EUDAT <http://www.eudat.eu/>`_.

**Deposit and release your data** via the generic interface, or select a community extension including domain-specific metadata fields. **Share your data** with others in a safe and trusted environment. **Scientific communities** are able to brand templates, and use their own collections with specific metadata.

B2SHARE is based on `Invenio <http://invenio-software.org/>`_. Invenio enables you to run your own electronic preprint server, your own online library catalogue or a digital document system on the web. It complies with the Open Archive Initiative metadata harvesting protocol.

**Main service is running at:** https://b2share.eudat.eu/

Developer documentation
-----------------------

A developer documentation is available. It can be built like this:

.. code-block:: console

    $ pip install -r requirements.txt # install dependencies
    $ pip install -e .[all]
    $ cd docs
    $ make html
    $ # open in your browser docs/_build/html/index.html

Acknowledgement
---------------

This work is co-funded by the `EOSC-hub project <http://eosc-hub.eu>`_ (Horizon 2020) under Grant number 777536.

.. image:: https://wiki.eosc-hub.eu/download/attachments/1867786/eu%20logo.jpeg?version=1&modificationDate=1459256840098&api=v2
  :height: 24px

.. image:: https://wiki.eosc-hub.eu/download/attachments/18973612/eosc-hub-web.png?version=1&modificationDate=1516099993132&api=v2
  :height: 24px

