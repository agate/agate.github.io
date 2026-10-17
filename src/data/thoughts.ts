import { getCollection, type CollectionEntry } from 'astro:content';

export type Lang = 'en' | 'zh';
type Entry = CollectionEntry<'thoughts'>;

export interface Thought {
  slug: string;
  date: Date;
  versions: Partial<Record<Lang, Entry>>;
}

// Groups `<slug>/en.md` and `<slug>/zh.md` into one post, newest first.
export async function getThoughts(): Promise<Thought[]> {
  const entries = await getCollection('thoughts', ({ data }) => import.meta.env.DEV || !data.draft);
  const bySlug = new Map<string, Thought>();
  for (const entry of entries) {
    const [slug, lang] = entry.id.split('/') as [string, Lang];
    const post = bySlug.get(slug) ?? { slug, date: entry.data.date, versions: {} };
    post.versions[lang] = entry;
    bySlug.set(slug, post);
  }
  return [...bySlug.values()].sort((a, b) => b.date.getTime() - a.date.getTime());
}

export function formatDate(date: Date, lang: Lang): string {
  return date.toLocaleDateString(lang === 'zh' ? 'zh-CN' : 'en-US', { year: 'numeric', month: 'short', timeZone: 'UTC' });
}
