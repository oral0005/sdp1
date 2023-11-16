# Singleton Pattern
class DatabaseConnectionManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(DatabaseConnectionManager, cls).__new__(cls)
            cls._instance.connection = "Connected to the database"
        return cls._instance
# Factory Pattern
class FormatterFactory:
    def create_formatter(self, formatter_type):
        if formatter_type == "uppercase":
            return UpperCaseFormatter()
        elif formatter_type == "lowercase":
            return LowerCaseFormatter()
        else:
            raise ValueError(f"Invalid formatter type: {formatter_type}")

# Strategy Pattern
class TextFormatter:
    def format_text(self, text):
        pass

class UpperCaseFormatter(TextFormatter):
    def format_text(self, text):
        return text.upper()

class LowerCaseFormatter(TextFormatter):
    def format_text(self, text):
        return text.lower()

# Decorator Pattern
class TextDecorator(TextFormatter):
    def __init__(self, wrapped_formatter):
        self._wrapped_formatter = wrapped_formatter

    def format_text(self, text):
        pass

class BoldDecorator(TextDecorator):
    def format_text(self, text):
        return "<b>" + self._wrapped_formatter.format_text(text) + "</b>"

# Adapter Pattern
class TextFormatterAdapter(TextDecorator):
    def __init__(self, text_formatter):
        self._text_formatter = text_formatter

    def format_text(self, text):
        return self._text_formatter.format_text(text)

if __name__ == "__main__":
    # Singleton
    db_manager = DatabaseConnectionManager()
    print(db_manager.connection)

    # Factory
    formatter_factory = FormatterFactory()

    # Strategy using Factory
    text = "Hello, Design Patterns!"
    formatter_type = input("Input type(uppercase/lowercase):")
    formatter = formatter_factory.create_formatter(formatter_type)
    formatted_text = formatter.format_text(text)
    print(f"formatted text:", formatted_text)

    # Adapter
    adapter = TextFormatterAdapter(formatter)
    bold_adapter = BoldDecorator(adapter)

    # Decorator using the adapted TextFormatter
    bold_formatted_text = bold_adapter.format_text(text)
    print("Bold formatted text with adapter:", bold_formatted_text)

