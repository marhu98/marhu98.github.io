#!/usr/bin/env python3


def callback(func):
    def inner(ctx,param,value):

        if not value or ctx.resilient_parsing:
            return
        func(ctx,param,value)

        ctx.exit()
    return inner
