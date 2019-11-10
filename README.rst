============
onjugator
============


A conjugator for spanish verbs. You have to provide a Spanish verb and the type of the desired conjugation.
The following types are supported:

    "Indicative",
    "Subjunctive",
    "Imperative",
    "Continuous (Progressive)",
    "Perfect",
    "Perfect Subjunctive"

The conjugate-method returns a pandas DataFrame object.


Description
===========

Installation:

	pip install esconjugator

Example usage:

    >>> from conjugator.spanish import conjugate
    >>> conjugate("buscar", "Indicative")
                 Person   Present   Preterite   Imperfect  Conditional      Future
    0                yo     busco      busqué     buscaba     buscaría     buscaré
    1                tú    buscas    buscaste    buscabas    buscarías    buscarás
    2       él/ella/Ud.     busca       buscó     buscaba     buscaría     buscará
    3          nosotros  buscamos    buscamos  buscábamos  buscaríamos  buscaremos
    4          vosotros   buscáis  buscasteis   buscabais   buscaríais   buscaréis
    5  ellos/ellas/Uds.    buscan    buscaron    buscaban    buscarían    buscarán



Note
====

This project has been set up using PyScaffold 3.2.3. For details and usage
information on PyScaffold see https://pyscaffold.org/.
