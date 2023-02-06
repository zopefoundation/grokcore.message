import os
from setuptools import setup, find_packages

version = '4.0.dev0'

readme = open(os.path.join('src', 'grokcore', 'message', 'README.txt')).read()
changes = open("CHANGES.txt").read()

long_description = "%s\n\n%s\n" % (readme, changes)

install_requires = [
    'setuptools',
    'grokcore.component >= 2.5dev',
    'z3c.flashmessage',
    'zope.component',
    'zope.traversing',  # zope.session seems not to declare this dep.?
]

tests_require = [
    'zope.publisher',
    'zope.security',
    'zope.session',
    'zope.testrunner',
]

setup(name='grokcore.message',
      version=version,
      description="Grok messaging machinery",
      long_description=long_description,
      keywords='Grok Messages',
      author='Grok Team',
      author_email='grok-dev@zope.org',
      url='http://pypi.python.org/pypi/grokcore.message',
      license='ZPL 2.1',
      namespace_packages=['grokcore'],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require=dict(test=tests_require),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Framework :: Zope :: 3',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: Implementation',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Internet :: WWW/HTTP',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
