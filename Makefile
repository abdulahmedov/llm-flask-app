style:
 flake8 .

types:
 mypy app

tests:
 pytest --lf -vv

check:
 make -j3 style types tests