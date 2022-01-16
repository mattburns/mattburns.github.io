---
title: How to install R on OSX
author: matt
type: post
date: 2014-02-18T12:11:17+00:00
url: /blog/2014/02/18/how-to-install-r-on-osx/
cover:
    image: /wp-content/uploads/2014/02/Apple-OS-X-10-9-Mavericks-Wallpaper-672x372.jpg
categories:
  - Uncategorized

---
## Install [Homebrew][1] (if needed)

```
ruby -e "$(curl -fsSL \
https://raw.github.com/Homebrew/homebrew/go/install)"
```

## Install R

```
brew tap homebrew/science
brew install r
```

 [1]: http://brew.sh/