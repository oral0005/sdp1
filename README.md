# Design Patterns Example

This Python script demonstrates the implementation of several design patterns: Singleton, Factory, Strategy, Decorator, and Adapter.

## Singleton Pattern
The `DatabaseConnectionManager` class ensures that only one instance of the database connection manager is created. This prevents multiple connections to the database, providing a single point of access.

## Factory Pattern
The `FormatterFactory` class acts as a factory for creating different text formatters based on the provided formatter type ("uppercase" or "lowercase").

## Strategy Pattern
The `TextFormatter` class is an abstract strategy interface, and its concrete implementations (`UpperCaseFormatter` and `LowerCaseFormatter`) provide different strategies for formatting text.

## Decorator Pattern
The `TextDecorator` class is an abstract decorator that wraps a `TextFormatter`. Concrete decorators like `BoldDecorator` add additional functionality (in this case, making the text bold) to the formatted text.

## Adapter Pattern
The `TextFormatterAdapter` class serves as an adapter for the `TextFormatter` class, allowing it to be used as a `TextDecorator`. This enables the integration of the `TextFormatter` into the decorator pattern.

## Example Usage
```python
# Singleton
db_manager = DatabaseConnectionManager()
print(db_manager.connection)

# Factory
formatter_factory = FormatterFactory()

# Strategy using Factory
text = "Hello, Design Patterns!"
formatter_type = input("Input type (uppercase/lowercase):")
formatter = formatter_factory.create_formatter(formatter_type)
formatted_text = formatter.format_text(text)
print(f"Formatted text: {formatted_text}")

# Adapter
adapter = TextFormatterAdapter(formatter)
bold_adapter = BoldDecorator(adapter)

# Decorator using the adapted TextFormatter
bold_formatted_text = bold_adapter.format_text(text)
print("Bold formatted text with adapter:", bold_formatted_text)
```

This script showcases how these design patterns can be combined and used together to create a flexible and modular system for text formatting and database connection management.
