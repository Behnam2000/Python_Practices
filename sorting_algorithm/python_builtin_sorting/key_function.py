# Sort strings by length
words = ["banana", "fig", "apple", "kiwi", "cherry"]
print(sorted(words, key=len))
# ['fig', 'kiwi', 'apple', 'banana', 'cherry']


# Sort strings by last character
print(sorted(words, key=lambda w: w[-1]))
# ['banana', 'apple', 'fig', 'cherry', 'kiwi']


# Sort a list of tuples by the second element
students = [("Alice", 3.8), ("Bob", 3.5), ("Charlie", 3.9), ("Diana", 3.7)]
print(sorted(students, key=lambda s: s[1], reverse=True))
# [('Charlie', 3.9), ('Alice', 3.8), ('Diana', 3.7), ('Bob', 3.5)]


# Sort objects by attribute
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __repr__(self) -> str:
        return f"{self.name}(${self.price})"

products = [Product("Hat", 25), Product("Shirt", 40), Product("Socks", 10)]
print(sorted(products, key=lambda p: p.price))
# [Socks(<span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>10</mn><mo stretchy="false">)</mo><mo separator="true">,</mo><mi>H</mi><mi>a</mi><mi>t</mi><mo stretchy="false">(</mo></mrow><annotation encoding="application/x-tex">10), Hat(</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord">10</span><span class="mclose">)</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord mathnormal" style="margin-right:0.08125em;">H</span><span class="mord mathnormal">a</span><span class="mord mathnormal">t</span><span class="mopen">(</span></span></span></span>25), Shirt($40)]     

# Using operator.attrgetter for cleaner attribute access
from operator import attrgetter
print(sorted(products, key=attrgetter("price")))
# Same result, often faster for large datasets