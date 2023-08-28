import os

from setuptools import find_packages
from setuptools import setup


version = '4.0'

with open(os.path.join('src', 'grokcore', 'message', 'README.rst')) as f:
    readme = f.read()
with open("CHANGES.rst") as f:
    changes = f.read()

long_description = "{}\n\n{}\n".format(readme, changes)

install_requires = [
    'setuptools',
    'grokcore.component >= 2.5',
    'z3c.flashmessage',
    'zope.component',
]

tests_require = [
    'zope.publisher',
    'zope.security',
    'zope.session >= 5.1',
    'zope.testrunner',
]

setup(name='grokcore.message',
      version=version,
      description="Grok messaging machinery",
      long_description=long_description,
      keywords='Grok Messages',
      author='Grok Team',
      author_email='grok-dev@zope.dev',
      url='https://github.com/zopefoundation/grokcore.message',
      license='ZPL 2.1',
      namespace_packages=['grokcore'],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      python_requires='>=3.7',
      install_requires=install_requires,
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
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Programming Language :: Python :: Implementation',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Internet :: WWW/HTTP',
      ],
      )
