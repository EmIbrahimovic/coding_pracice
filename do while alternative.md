---
strongly-connected:
- "[[python]]"
- "[[programming]]"
- "[[coding patterns]]"
alias:
tags:
---

# do while alternative

```python
output = []
next_index = index + 1

while next_index < len(tokens) and tokens[next_index] != ")":
    element, next_index = parse_expression(next_index)
    output.append(element)

if next_index >= len(tokens):
    raise SchemeSyntaxError(
        "Something went wrong, the parser reached the end of the expression before closing ')'"
    )
```

 ```python
 output = []

        next_index = index + 1

        while True:

            if next_index >= len(tokens):

                raise SchemeSyntaxError(

                    f"Something went wrong, the parser reached the end of the expression before closing ')'"

                )

            if tokens[next_index] == ")":

                break

            element, next_index = parse_expression(next_index)

            output.append(element)
 ```