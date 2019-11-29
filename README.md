![GitHub Actions status | sdras/awesome-actions](https://github.com/plysytsya/conjugator/workflows/runtests/badge.svg)
[![codecov](https://codecov.io/gh/plysytsya/conjugator/branch/master/graph/badge.svg)](https://codecov.io/gh/plysytsya/conjugator/branch/master/graph/badge.svg)
![PyPI](https://img.shields.io/pypi/v/conjugator)


# Conjugator


A conjugator for spanish verbs. You have to provide a spanish verb and the type of the desired conjugation.



## Description

Installation:

    pip install conjugator

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


The following types are supported:

    'Indicative',
    'Subjunctive',
    'Imperative',
    'Continuous (Progressive)',
    'Perfect',
    'Perfect Subjunctive'

The conjugate-method returns a pandas DataFrame object.

Example:

    >>> df = conjugate("bailar", "Subjunctive")
    >>> df[["Person", "Present"]]
                 Person   Present
    0                yo     baile
    1                tú    bailes
    2       él/ella/Ud.     baile
    3          nosotros  bailemos
    4          vosotros   bailéis
    5  ellos/ellas/Uds.    bailen


For further reference read: https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html



## Note

This project has been set up using PyScaffold 3.2.3. For details and usage
information on PyScaffold see https://pyscaffold.org/.
