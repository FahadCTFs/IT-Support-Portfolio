# Outdated Packages Checker

A simple Python script to **check for outdated packages** on Debian/Ubuntu systems.

It can be used as a **cron job** for companies or servers to monitor system updates automatically, helping maintain security and stability.

---

## Features

* Lists packages that have updates available.
* Shows **installed version → available version**.
* Saves results to `outdated_packages.txt` for logging.
* Can be scheduled to run periodically using **cron**.

---

## Usage Example

Run the script manually:

```bash
python3 outdated_packages.py
```

Example output:

```
bash: 5.1-1ubuntu1 → 5.1-2ubuntu1
coreutils: 8.30-3 → 8.30-4
```

Or schedule with **cron** (runs daily at 7 AM):

```cron
0 7 * * * /usr/bin/python3 /path/to/outdated_packages.py
```

Results will be saved automatically for review.

---

## Notes

* Works on **Debian/Ubuntu** systems.
* Requires **Python 3**.
* No packages are updated automatically—this is **monitoring only**, useful for security audits.

---


