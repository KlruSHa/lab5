class LibraryError(Exception):
    pass


class BookNotFoundError(LibraryError):
    pass


class DuplicateBookError(LibraryError):
    pass


class ValidationError(LibraryError):
    pass
