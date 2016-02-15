#!/usr/bin/env python

import agate
import agatelookup

agatelookup.patch()

source = agatelookup.Source()

# Simple
table = agate.Table([
    ('WA',),
    ('VA',),
    ('NE',)
], ['usps'])

joined = table.lookup(source, 'usps', 'state')

joined.print_table()

# Versioned
table = agate.Table([
    ('1111',),
    ('313320',),
    ('522310',)
], ['naics'], [agate.Text()])

joined = table.lookup(source, 'naics', 'description', version='2012')

joined.print_table()

# Multiple keys
table = agate.Table([
    ('AZ', '1985'),
    ('WY', '2014'),
    ('SC', '1994')
], ['usps', 'year'], [agate.Text(), agate.Text()])

joined = table.lookup(source, ['usps', 'year'], 'population')

joined.print_table()

# Multiple keys 2
table = agate.Table([
    ('1985', '3'),
    ('2007', '5'),
    ('2011', '6')
], ['year', 'month'], [agate.Text(), agate.Text()])

joined = table.lookup(source, ['year', 'month'], 'cpi')

joined.print_table()
