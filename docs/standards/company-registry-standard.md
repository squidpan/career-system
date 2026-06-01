# Company Registry Standard

## Purpose

The company registry maps short stable company codes to full company names.

## Example

```json
{
  "tata": {
    "company_name": "Tata Consultancy Services",
    "company_slug": "tata",
    "company_aliases": ["Tata", "Tata Consultancy Services", "TCS"]
  }
}
```

## Rules

- Use short lowercase keys.
- Avoid long company names in filenames when a clean company code exists.
- Preserve full company name in `company_name`.
- Use aliases to recognize source variations.
