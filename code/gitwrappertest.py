#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import github3 

gh = login(token='')

me= gh.me()


print(me.name)

print(me.login)

print(me.followers_count)

owner="Opifex-chathamicus"
repository_name="Konopzzzz"
short_repository = qh.repository(owner, repository_name)
for short_repository in gh.repositories_by(owner):
    full_repository = short_repository.refresh()
print(full_repository)
