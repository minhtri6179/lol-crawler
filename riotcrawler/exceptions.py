class RiotCrawlerException(Exception):
    """
    Base exception class.

    All RiotCrawler-specific exceptions should subclass this class.
    """


class ConfigDoesNotExistException(RiotCrawlerException):
    """
    Exception for missing config file.

    Raised when get_config() is passed a path to a config file, but no file
    is found at that path.
    """


class InvalidConfiguration(RiotCrawlerException):
    """
    Exception for invalid configuration file.

    Raised if the global configuration file is not valid YAML or is
    badly constructed.
    """
