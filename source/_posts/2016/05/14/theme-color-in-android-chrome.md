title: theme-color in Android Chrome
date: 2016-05-14 21:07:16
tags:
  - android
  - html
---

早就发现在 Android Chrome 很多网页都会自定义状态栏的颜色. 但是不知道怎么弄. 今天想把自己的网页设置一下就 Google 了一下. 发现从版本 39 起, 就支持你在 html meta 里头设置 theme-color 来自定义系统的状态栏的颜色. 具体的语法格式是这样的:

```html
<meta name="theme-color" content="#you-color">
```

![screenshot](/images/theme-color-in-android-chrome.png)

在官方宣传页面中我还看到还可以自定义 icon (当然早就支持啦)
  
```html
<link rel="icon" sizes="192x192" href="nice-highres.png">
```


* [Support-for-theme-color-in-Chrome-39-for-Android](https://developers.google.com/web/updates/2014/11/Support-for-theme-color-in-Chrome-39-for-Android)
