from griptape.google.tools import GoogleCalendarTool


class TestGoogleCalendarTool:
    def test_init(self):
        assert GoogleCalendarTool(owner_email="foo", service_account_credentials={})
