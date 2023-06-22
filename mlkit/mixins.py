"""Module with mixing classes"""
import logging


class LoggerMixin:
    """Mixing class providing methods for direct logging instead of calling `_logger` methods.`"""

    _logger: logging.Logger

    def debug(self, *args, **kwargs):
        """Log on debug level"""
        self._logger.debug(*args, **kwargs)

    def info(self, *args, **kwargs):
        """Log on info level"""
        self._logger.info(*args, **kwargs)

    def warn(self, *args, **kwargs):
        """Log on warning level"""
        self._logger.warn(*args, **kwargs)

    def error(self, *args, **kwargs):
        """Log on error level"""
        self._logger.error(*args, **kwargs)

    def critical(self, *args, **kwargs):
        """Log on critical level"""
        self._logger.critical(*args, **kwargs)
