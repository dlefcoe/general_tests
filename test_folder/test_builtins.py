'''

https://www.tutorialsteacher.com/python/python-builtin-modules


'''


import doctest

try: import crypt
except Exception as e:
    print('unable to import crypt module:', e)
    print('quitting')
    quit()

import csv

import dataclasses

import code
import cmath
import calendar

x = crypt.crypt('darren')

print(x)
print(type(x))




'''
help('modules')


IPython             _weakrefset         heapq               secrets
__future__          _winapi             hmac                select
_abc                abc                 html                selectors
_ast                aifc                http                setuptools
_asyncio            antigravity         idlelib             shelve
_bisect             argparse            imaplib             shlex
_blake2             array               imghdr              shutil
_bootlocale         ast                 imp                 signal
_bz2                asynchat            importlib           simplegeneric
_codecs             asyncio             ind                 site
_codecs_cn          asyncore            inspect             six
_codecs_hk          atexit              io                  smtpd
_codecs_iso2022     audioop             ipaddress           smtplib
_codecs_jp          autoreload          ipython_genutils    sndhdr
_codecs_kr          backcall            itertools           socket
_codecs_tw          base64              jedi                socketserver
_collections        bdb                 json                sqlite3
_collections_abc    binascii            keyword             sre_compile
_compat_pickle      binhex              lib2to3             sre_constants
_compression        bisect              linecache           sre_parse
_contextvars        builtins            locale              ssl
_csv                bz2                 logging             stat
_ctypes             cProfile            lzma                statistics
_ctypes_test        calendar            macpath             storemagic
_datetime           cgi                 mailbox             string
_decimal            cgitb               mailcap             stringprep
_distutils_findvs   chunk               marshal             struct
_dummy_thread       cmath               math                subprocess
_elementtree        cmd                 mimetypes           sunau
_functools          code                mmap                symbol
_hashlib            codecs              modulefinder        sympyprinting
_heapq              codeop              msilib              symtable
_imp                collections         msvcrt              sys
_io                 colorama            multiprocessing     sysconfig
_json               colorsys            netrc               tabnanny
_locale             compileall          nntplib             tarfile
_lsprof             concurrent          nt                  telnetlib
_lzma               configparser        ntpath              tempfile
_markupbase         contextlib          nturl2path          test
_md5                contextvars         numbers             tests
_msi                copy                opcode              textwrap
_multibytecodec     copyreg             operator            this
_multiprocessing    crypt               optparse            threading
_opcode             csv                 os                  time
_operator           ctypes              parser              timeit
_osx_support        curses              parso               tkinter
_overlapped         cythonmagic         pathlib             token
_pickle             dataclasses         pdb                 tokenize
_py_abc             datetime            pickle              trace
_pydecimal          dbm                 pickleshare         traceback
_pyio               decimal             pickletools         tracemalloc
_queue              decorator           pip                 traitlets
_random             difflib             pipes               tty
_sha1               dis                 pkg_resources       turtle
_sha256             distutils           pkgutil             turtledemo
_sha3               doctest             platform            types
_sha512             dummy_threading     plistlib            typing
_signal             easy_install        poplib              unicodedata
_sitebuiltins       email               posixpath           unittest
_socket             encodings           pprint              urllib
_sqlite3            ensurepip           profile             uu
_sre                enum                prompt_toolkit      uuid
_ssl                errno               pstats              venv
_stat               faulthandler        pty                 warnings
_string             filecmp             py_compile          wave
_strptime           fileinput           pyclbr              wcwidth
_struct             fnmatch             pydoc               weakref
_symtable           formatter           pydoc_data          webbrowser
_testbuffer         fractions           pyexpat             winreg
_testcapi           ftplib              pygments            winsound
_testconsole        functools           queue               wsgiref
_testimportmultiple gc                  quopri              xdrlib
_testmultiphase     genericpath         random              xml
_thread             getopt              re                  xmlrpc
_threading_local    getpass             reprlib             xxsubtype
_tkinter            gettext             rlcompleter         zipapp
_tracemalloc        glob                rmagic              zipfile
_warnings           gzip                runpy               zipimport
_weakref            hashlib             sched               zlib



'''