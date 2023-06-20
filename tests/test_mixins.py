import pytest


class TestLoggingMixin:
    @pytest.mark.parametrized(
        "log_method", ["debug", "info", "warn", "error", "critical"]
    )
    def test_log_methods_are_available(self, log_method):
        from mlkit.mixins import LoggerMixin

        class A(LoggerMixin):
            pass

        assert hasattr(A(), log_method)