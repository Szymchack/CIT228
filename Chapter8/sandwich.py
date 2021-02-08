def make_sandwich(*items):
    """Make a sandwich with the given items."""
    print("\nI'll make you a great sandwich:")
    for item in items:
        print("  ...adding " + item + " to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'tomato', 'horseradish', 'mayonnaise')
make_sandwich('turkey', 'bacon', 'apple slices', 'spicy mustard')
make_sandwich('ham', 'capicola', 'pepperoni', 'lettuce', 'tomato', 'mayonnaise', 'italian dressing')