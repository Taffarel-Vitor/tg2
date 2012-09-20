import platform, sys

if platform.system() == 'Windows': # pragma: no cover
    WIN = True
else: # pragma: no cover
    WIN = False

# True if we are running on Python 3.
PY3 = sys.version_info[0] == 3

if PY3:
    string_type = str
    unicode_text = str
    from urllib.parse import urlencode as url_encode
else:
    string_type = basestring
    unicode_text = unicode
    from urllib import urlencode as url_encode

def im_func(f):
    if PY3:
        return f.__func__
    else:
        return f.im_func

def im_self(f):
    if PY3:
        return getattr(f, '__self__', None)
    else:
        return getattr(f, 'im_self', None)

def with_metaclass(meta, base=object):
    """Create a base class with a metaclass."""
    return meta("NewBase", (base,), {})