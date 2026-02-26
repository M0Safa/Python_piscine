## This project has been created as part of the 42 curriculum by [mosafa]<https://profile-v3.intra.42.fr/users/mosafa>

## Introducion

This project explores Python’s import system and package organization through a series of progressively structured exercises. It focuses on how Python modules and packages are
 designed, exposed, and interconnected.

## part 1:

In this part, we learned how the __init__.py file transforms a folder into a Python package and controls its public interface. By selectively importing specific functions, we
exposed only the intended functionality at the package level while keeping other internal functions hidden. This demonstrated the difference between module contents and what a 
package chooses to make available to its users.

## part 2:

This section explored different import styles in Python, including full module imports, specific function imports, aliased imports, and multiple imports. Each method was
demonstrated with practical examples, highlighting how they affect code readability, namespace management, and maintainability. The trade-offs between clarity and conciseness
were examined to understand when each import style is most appropriate.

## part 3:

In this part, we compared absolute imports and relative imports within a multi-level package structure. Absolute imports were used to provide clarity and robustness across the
project, while relative imports were used for concise internal references within a package. This exercise illustrated how both approaches can coexist and how to choose the
appropriate one based on project scale and context.

## part 4:

The final part addressed circular dependencies, a common and dangerous issue in modular Python projects. We identified how circular imports occur and why they lead to runtime
errors. To resolve this, we implemented a late import technique, allowing dependencies to be loaded only when needed. This demonstrated practical strategies for breaking
circular dependencies and designing safer module interactions.
