#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код
garden_set = set(garden)
meadow_set = set(meadow)
print(garden_set) # в саду
print(meadow_set) # на лугу
# выведите на консоль все виды цветов
# TODO здесь ваш код
gm = garden_set | meadow_set
print(gm)
# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
gm1 = garden_set & meadow_set
print(gm1)
# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
gm2 = garden_set - meadow_set
print(gm2)
# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
gm3 = meadow_set - garden_set
print(gm3)