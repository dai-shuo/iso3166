# ISO 3166-1 and ISO 3166-2 Tables

iso 3166-1 and iso 3166-2 tables.

# iso3166-1.csv

[iso3166-1.csv](iso3166-1.csv) is a table of world countries defined by [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1).

**Example**

| **alpha-2** | **alpha-3** | **name** | **wikipedia** |
| ---- | ---- | ---- | ---- |
| AG |ATG | Antigua and Barbuda | Antigua_and_Barbuda |

- alpha-2: the [ISO 3166-1 Alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code of the country.
- alpha-3: the [ISO 3166-1 Alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of the country.
- name: the country name.
- wikipedia: the wikepedia page of the country is https://en.wikipedia.org/wiki/{wikipedia}.

----

# iso3166-2.csv

[iso3166-2.csv](iso3166-2.csv) is a table of subdivisions of all countries defined by [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2).

**Example**

| **code** | **name** | **wikipedia** |
| ---- | ---- | ---- |
| US-NY | New York | New_York_(state) |

- code: the [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) code of the subdivision. the pattern is always `Alpha-2`-`Subdivision`, where `Alpha-2` is the [ISO 3166-1 Alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. You can always find the alpha-2 code in [iso3166-1.csv](iso3166-1.csv).
- name: the subdivision name.
- wikipedia: the wikepedia page of the subdivision is https://en.wikipedia.org/wiki/{wikipedia}.

----

