# Hledání čtyřmístného PINu dělitelného prvočíslem 13

## Obsah

1. [Úvod](#úvod)
2. [Kód](#kód)
3. [Závěr](#závěr)

## Úvod

Tomáš Marný má trezor, který chrání čtyřmístný PIN. Jeho kompulzivní porucha mu nařizuje používat pouze PINy, které jsou dělitelné prvočíslem 13. V tomto dokumentu implementujeme tři různé postupy k nalezení takového PINu: hrubou sílu, rozděl a panuj a heuristický algoritmus.

## Kód

1. **Hrubá síla**: Tento přístup prostě prochází všechny možné kombinace čtyřmístných PINů od 1000 do 9999 a ověřuje, zda jsou dělitelné prvočíslem 13. Začíná od 1000 a postupuje až po 9999, což znamená, že prohledá všechny možné kombinace.

2. **Rozděl a panuj**: Tento přístup rozděluje problém na menší části tím, že projde všechny možné kombinace jednotlivých čísel od 0 do 9 a spojí je do čtyřmístného PINu, který poté ověří, zda je dělitelný prvočíslem 13.

3. **Heuristický algoritmus**: Tento přístup se snaží minimalizovat počet průchodů kombinací tím, že zkouší pouze kombinace PINů, které jsou prvočísly. To znamená, že ověřuje, zda je čtyřmístný PIN dělitelný prvočíslem 13 a zároveň je sám prvočíslem.

## Závěr

Každý z těchto postupů má své vlastní výhody a nevýhody. Volba nejlepšího postupu závisí na konkrétní situaci a na požadavcích uživatele. Hrubá síla je jednoduchá, ale může trvat dlouho, zatímco heuristický algoritmus může být efektivnější, pokud je PIN prvočíslo.
