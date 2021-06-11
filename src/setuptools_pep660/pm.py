"""
From https://discuss.python.org/t/implementing-pep-660-for-setuptools/9193/2
"""

from tempfile import TemporaryDirectory
from pathlib import Path
import sys
import os
from setuptools.build_meta import _BuildMetaBackend, no_install_setup_requires


class DevelopBackend(_BuildMetaBackend):
    def get_develop_files(self):
        with TemporaryDirectory() as tmp:
            site_packages = Path(tmp) / "lib" / "site-packages"
            site_packages.mkdir(parents=True)
            # Hack to convince the "are .pth files processed" check that
            # things are OK.
            os.environ["PYTHONPATH"] = str(site_packages)
            sys.argv = [sys.argv[0], "develop", "--prefix", tmp]
            with no_install_setup_requires():
                self.run_setup()

            paths = []
            files = []
            for f in site_packages.iterdir():
                content = f.read_text(encoding="utf-8")
                if f.suffix == ".pth":
                    paths.extend(content.splitlines())
                else:
                    files.append((f.name, content))

            return paths, files


def wheel_content():
    return DevelopBackend().get_develop_files()


if __name__ == "__main__":
    paths, files = wheel_content()
    print(paths, files)