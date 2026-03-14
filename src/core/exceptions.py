class FeeExtractionException(Exception):
    """Base class for all fee extraction related exceptions."""
    pass

class DocumentFetchException(FeeExtractionException):
    """Exception raised when fetching documents fails."""
    pass

class DocumentParseException(FeeExtractionException):
    """Exception raised when parsing document fails."""
    pass

class ValidationError(FeeExtractionException):
    """Exception raised for validation errors."""
    pass

class ExchangeRateRequiredError(FeeExtractionException):
    """Exception raised when an exchange rate is required but not provided."""
    pass

class SchemaError(FeeExtractionException):
    """Exception raised for schema validation errors."""
    pass