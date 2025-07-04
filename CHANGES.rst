CHANGES
*******

5.1 (unreleased)
================

- Nothing changed yet.


5.0 (2025-06-18)
================

- Replace ``pkg_resources`` namespace with PEP 420 native namespace.


4.1 (2025-06-04)
================

- Add support for Python 3.12, 3.13.

- Drop support for Python 3.7, 3.8.


4.0 (2023-08-28)
================

- Drop support for Python 2.7, 3.4, 3.5, 3.6.

- Add support for Python 3.7, 3.8, 3.9, 3.10, 3.11.


3.0.1 (2018-01-17)
==================

- Replace the use of `grok.implements()` with the `@grok.implementer()`
  directive throughout.

3.0.0 (2018-01-15)
==================

- Python 3 compatibility.

0.4.3 (2016-02-15)
==================

- Update tests.

0.4.2 (2010-10-25)
==================

- Tests fixed by explicitely registering the IClientIdManager and
  ISessionDataContainer utilities. The ftesting.zcml was re-introduced for this.

0.4.1 (2010-10-25)
==================

- Remove ftesting.zcml that was not necessary anymore.

0.4 (2010-10-25)
================

* Make sure ``zope.session`` is configured, as this package claims to provide
  for a session based flash message machinery.

* Made package comply to zope.org repository policy.

0.3 (2010-03-05)
================

* ``UniqueMessageSource`` now implements the ``IMessageSource``
  interface completely, i.e. the ``type`` parameter is now optional
  when using ``UniqueMessageSource.send()``.

0.2 (2010-03-03)
================

* The utility function ``send`` now takes a ``name`` argument,
  allowing the choice of the target message source.

0.1 (2010-03-03)
================

* Factored out from former versions of ``grokui.admin``, ``grok`` and
  ``megrok.layout`` respectively.
