**django-finkok**
=================

Simple django application to integrate the FINKOK service for sending
invoices to the mexican treasury (SAT).

Background
----------

In Mexico, it is required to report the expenses made by any company and person
to the government treasury department (SAT). This is quite tricky to do by our
own, because a certification is required to be able to connect to their servers
directly, but [Finkok](http://www.finkok.com/) is here for the rescue.

Finkok acts as an intermediary. It has all the certifications on check to
connect with those servers, and it makes it quite easy for anyone to emit a
new invoice. The only problem is that they use a WSDL schema to receive the
information and the files required.

This application does **not** require django. It was created to wrap all the
functionality and the validations required to communicate with Finkok. If
you wish to copy or improve the code, please feel free to do it.

Installation
------------

Before installing this package, make sure your development and production
systems are compatible with the libraries `suds-jurko` and `lxml`, as this
application will not work without them.

**Not available in pip yet, wait for version 0.3**

Release Notes
-------------

*   0.0.1

  * Boilerplate

Disclaimer
---------

The code developed for this repository is used for GRVTYlabs' projects. If you
wish to know more about one of the projects which uses this library, please
visit: [FacturaBot](www.facturabot.com)

GRVTYlabs uses this code in the best possible manner, without trying to
affect the users nor any related party, any bug which does affect the users
will be patched but is unintentional.

The code in this repository is being checked continuously, and any user whom
tries to generate an exploit in a pull-request will not be tolerated. This
package manages sensitive information, please respect that.

Owned and developed by
--------

[![StackShare][stack-shield]][stack-tech]

[![GRVTYlabs][logo]](www.grvtylabs.com)


[logo]: https://github.com/grvty-labs/django-finkok/blob/master/logo.png?raw=true "GRVTYlabs"
[stack-shield]: http://img.shields.io/badge/tech-stack-0690fa.svg?style=flat
[stack-tech]: http://stackshare.io/letops/grvtylabs
