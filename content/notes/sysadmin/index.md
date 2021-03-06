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

## SSH

NOTE: This may eventually be moved to its own "SSH" page

### Key Management

I normally log into a remote machine via my development machine, which is almost always a graphical environment. Right now I am running Ubuntu 18.04 on both my personal and work laptop, with GNOME display manager, `gdm`, as my graphical login program. Until reading [Mark Hershberger's blog](http://mah.everybody.org/docs/ssh) I didn't realize that `gdm` is what started `ssh-agent` for me - I just kind of took it for granted that `ssh-agent` seemed to be running automatically...

Then I tried to go the opposite direction, `scp`'ing a file from my host machine while on the remote machine, and I was greeted by "Enter passphrase for key". I remembered that the solution to this is `ssh-agent` but then after logging out and back into the remote I had to repeat this process. Then it kicked in that I need a means of automatically starting `ssh-agent` on login for my user.

### Host Management

Tired of typing [FQDNs](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) that you log into frequently? Add that host to your `~/.ssh/config` file as a "host" and you will be able to type `ssh <user>@<short-host>`.

```
# Host <short-hostname>
#   Hostname <long-hostname>

Host server1
  Hostname server1.full.path.com
```

Note: The <short-hostname> does not need to match the first label of the FQDN, I follow this template when the first label (subdomain) matches the machine name.

When is this not the case? I have a machine on my home network that is accessible via a URL (using [DDNS](https://en.wikipedia.org/wiki/Dynamic_DNS), that merits a whole other post). However, the public URL doesn't match the machine name (for several reasons), so I map the machine name to the hostname via my `~/.ssh/config`.

Another tip: If you're logging into a remote host using the same username you can omit it from your SSH invocation, e.g. `ssh <hostname>`. This also works for `scp`.

## Networking

Want a quick way to know your IP address(es)?

```bash
$ hostname -I
# <ip-1> <ip-2> ...
10.0.0.208 203.0.113.5
```

Neat note: The IP address range `203.0.113.0/24` is [reserved for documentation](https://tools.ietf.org/html/rfc5737)

## Directory Management

- `cd`
	+ Use `cd -` as shortcut to change to last directory, e.g. $OLDPWD

## Displays

Helpful for HiDPI displays

```bash
$ gsettings set org.gnome.desktop.interface text-scaling-factor 1.25
```