+++
title = "System Administration"
date = 2021-02-24
# updated = 
+++

## Users and Groups

### Add user to group

```bash
# usermod -a -G <group> <user>

# For example, add yourself to the 'docker' group
$ usermod -aG docker $USER
```

## Displays

Helpful for HiDPI displays

```bash
$ gsettings set org.gnome.desktop.interface text-scaling-factor 1.25
```
