# Added '-dynamic' to the ghc command to deal with dumb archlinux troubles, may need to be removed for other distro's etc.
cd code
ghc -dynamic -o solve -O2 Solve
cd ..
