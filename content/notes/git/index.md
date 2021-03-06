+++
title = "git"
date = 2021-01-02
# updated = 
+++


Recovering lost commits:

```bash
for b in $(ls $(git root)/.git/lost-found/commit); do git show --name-only --oneline $b | grep 'flash.h' && git show $b; done | less
```

Checkout last branch

```console
$ git checkout @{-1}
# Shorthand
$ git checkout -
```

See [here](https://mirrors.edge.kernel.org/pub/software/scm/git/docs/gitrevisions.html) for the `gitrevisions` docs, which has lots of other useful constructs like `${u}` which is shorthand for the upstream branch.


Delete remote branch

```bash
git push origin --delete <branch>
```
