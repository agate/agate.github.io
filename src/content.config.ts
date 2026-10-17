import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

// One post = one folder per slug with en.md and/or zh.md inside:
//   src/content/thoughts/<slug>/en.md
//   src/content/thoughts/<slug>/zh.md
const thoughts = defineCollection({
  loader: glob({ pattern: '*/{en,zh}.md', base: './src/content/thoughts' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    draft: z.boolean().default(false),
  }),
});

export const collections = { thoughts };
