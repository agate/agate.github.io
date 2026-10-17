// The one place to change the site's domain or the author's name.
// Imported by astro.config.mjs and by pages/components. Sub-sites (e.g. agate/claude-lights)
// link home with a relative "/" so they follow a domain change automatically.

export const DOMAIN = 'honghao.me';
export const SITE_URL = `https://${DOMAIN}`;

// Surname first, marked with a comma, in both languages.
export const AUTHOR = { en: 'Hong, Hao', zh: 'Hong, Hao' };

export const GITHUB_USER = 'agate';
export const GITHUB_URL = `https://github.com/${GITHUB_USER}`;
