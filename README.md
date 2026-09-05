# Falmouth Shore Excursion

Independent cruise-passenger planning guide for Falmouth, Jamaica shore excursions (World 2.0 static specialist).

## Development

```bash
npm install
npm run build
npm run check
npm run preview
```

Open http://localhost:8910 — primary content is inlined in HTML (works without JavaScript).

## Deploy to Cloudflare

```bash
npm run build && npm run check && ./deploy.sh
```

Domain: https://falmouthshoreexcursion.com

Schedule integration and direct payment are deferred.
