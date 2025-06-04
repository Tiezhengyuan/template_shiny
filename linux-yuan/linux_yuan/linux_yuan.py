from pathlib import PurePath

from htmltools import HTMLDependency, Tag

from shiny.module import resolve_id

# This object is used to let Shiny know where the dependencies needed to run
# our component all live. In this case, we're just using a single javascript
# file but we could also include CSS.
linux_yuan_deps = HTMLDependency(
    "linux_yuan",
    "1.0.0",
    source={
        "package": "linux_yuan",
        "subdir": str(PurePath(__file__).parent / "distjs"),
    },
    script={"src": "index.js", "type": "module"},
)


def linux_yuan(id: str):
    """
    A shiny input.
    """
    return Tag(
        # This is the name of the custom tag we created with our webcomponent
        "linux-yuan",
        linux_yuan_deps,
        # Use resolve_id so that our component will work in a module
        id=resolve_id(id),
    )
