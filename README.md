# Falmouth Shore Excursion

Cruise-passenger planning guide for Falmouth, Jamaica shore excursions.

## Development

```bash
npm install
npm run build
npm run images
npm run check
npm run preview
```

Open http://localhost:8910 (requires local server for partial loading).

## Deploy to Cloudflare

```bash
npm run build && npm run images && npm run check && ./deploy.sh
```

Domain: https://falmouthshoreexcursion.com
