from typing import Dict
from ssg.site import Site
import typer 
from ssg.site import Site

def main(source="content",dest="dest"):
    config = {"source":source, "dest":dest}
    Site(**config).build()

typer.run(main())
