import lights from '../icons/lights.svg?raw';
import scroll from '../icons/scroll.svg?raw';
import keyboard from '../icons/keyboard.svg?raw';
import next from '../icons/next.svg?raw';

export type Status = 'shipped' | 'building' | 'hobby' | 'soon';

export interface Project {
  name: { en: string; zh: string };
  blurb: { en: string; zh: string };
  status: Status;
  icon: string;
  url?: string;
}

// Newest or most important first. Add a project here and it shows up on the home page.
export const projects: Project[] = [
  {
    name: { en: 'claude-lights', zh: 'claude-lights' },
    blurb: {
      en: "A macOS menu bar app that shows every Claude Code session as a status light — see who's waiting, working, or done without watching terminals.",
      zh: 'macOS 菜单栏小工具：把每个 Claude Code 会话变成一盏状态灯。谁在等你、谁在忙、谁做完了，不用盯着终端也一眼看到。',
    },
    status: 'shipped',
    icon: lights,
    url: '/claude-lights/',
  },
  {
    name: { en: 'AI Poetry', zh: 'AI 古诗' },
    blurb: {
      en: 'One poem, one painting, one short film. Classical Chinese poetry brought to life with AI.',
      zh: '一首诗，一幅画，一段视频。用 AI 让古诗变成图文和短片。',
    },
    status: 'building',
    icon: scroll,
  },
  {
    name: { en: 'zmk-corne', zh: 'zmk-corne' },
    blurb: {
      en: 'ZMK firmware for my Corne split keyboard.',
      zh: '我那把 Corne 分体键盘的 ZMK 固件配置。',
    },
    status: 'hobby',
    icon: keyboard,
    url: 'https://github.com/agate/zmk-new_corne',
  },
  {
    name: { en: 'Next', zh: '下一个' },
    blurb: {
      en: 'Something new is always on the bench.',
      zh: '工作台上总有下一个新东西。',
    },
    status: 'soon',
    icon: next,
  },
];
