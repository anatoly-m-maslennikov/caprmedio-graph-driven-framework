# CA-M-399@20
"""INFO timing for lifecycle steps, with no input or carrier data in logs."""

from contextlib import contextmanager
from contextvars import ContextVar
from functools import wraps
import sys
import time

from technical_diagnostics import make_technical_logger


_context = ContextVar('lifecycle_timing', default=(None, None))
_names = frozenset({
    'atom_lifecycle_create_draft', 'atom_lifecycle_promote_draft',
    'atom_lifecycle_direct_update', 'atom_lifecycle_change_status',
    'atom_lifecycle_update', 'atom_lifecycle_archive',
})


def _logger(selection):
    settings = getattr(selection, 'settings', None)
    if settings is None:
        return None
    logger, _ = make_technical_logger(settings, selection.root, stream=sys.stdout, component='ATOM_LIFECYCLE')
    return logger


@contextmanager
def span(step, *, tool=None, selection=None):
    name, logger = _context.get()
    if tool in _names and selection is not None:
        name, logger = tool, _logger(selection)
    if logger is None:
        yield None
        return
    state = {'failed': False}
    fields = dict(severity='INFO', event='lifecycle_step', operation=name, code=step,
                  relative_path='', reason='')
    start = time.monotonic()
    logger.emit(**fields, outcome='started')
    try:
        yield state
    except BaseException as error:
        state['failed'] = True
        fields['exception_class'] = type(error).__name__
        raise
    finally:
        status = 'failed' if state['failed'] else 'done'
        elapsed = round((time.monotonic() - start) * 1000, 1)
        logger.emit(**fields, outcome=status, elapsed_ms=elapsed)


def trace(step):
    def decorate(function):
        @wraps(function)
        def timed(*args, **kwargs):
            with span(step) as state:
                value = function(*args, **kwargs)
                if state is not None:
                    if isinstance(value, dict):
                        state['failed'] = value.get('outcome') == 'failed' or bool(value.get('errors'))
                    else:
                        state['failed'] = bool(getattr(value, 'errors', ()))
                return value
        return timed
    return decorate


def lifecycle_tool(function):
    timed = trace('execute')(function)

    @wraps(function)
    def call(selection, model, name, params, **kwargs):
        token = _context.set((name, _logger(selection)) if name in _names else (None, None))
        try:
            return timed(selection, model, name, params, **kwargs)
        finally:
            _context.reset(token)
    return call
