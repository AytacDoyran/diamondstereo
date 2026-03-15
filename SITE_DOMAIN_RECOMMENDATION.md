# Site Domain Recommendation

User request: recommend a suitable custom domain for the site currently exposed via Cloudflare tunnel URL.

## Access check

- Attempted to fetch `https://performance-elite-bytes-cab.trycloudflare.com/` from this environment.
- Received `HTTP/1.1 403 Forbidden` via proxy, so page content could not be inspected directly here.

## Recommended domain options (SEO + brand-safe)

Because the tunnel hostname does not reveal business context, use clear, short, brandable names in one of these patterns:

1. `brandname.com` (best if available)
2. `getbrandname.com`
3. `brandnameapp.com`
4. `brandnameai.com` (if AI product)
5. `brandname.co` (startup-friendly fallback)

### If this is a performance/training site (based on URL token "performance")

- `eliteperformancehub.com`
- `performelite.com`
- `peakperformancestudio.com`
- `eliteperformans.com` (TR audience)
- `performansakademi.com` (TR audience)

## Google indexing preparation checklist

Before publishing to Google Search, ensure:

- Domain is connected in Cloudflare DNS (A/CNAME set correctly)
- Site is reachable with HTTPS on the final domain
- `sitemap.xml` exists and is submitted in Google Search Console
- `robots.txt` allows important pages
- Canonical tags point to final domain
- Title + meta description are unique per page
- Mobile usability and Core Web Vitals are acceptable

## Decision rule (quick)

- If target is global: prefer `.com`
- If primarily Türkiye: use `.com` or `.com.tr` (both can rank)
- Keep domain under ~15 chars if possible
- Avoid hyphens and hard spellings
