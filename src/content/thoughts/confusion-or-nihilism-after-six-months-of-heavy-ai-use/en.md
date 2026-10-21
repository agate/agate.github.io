---
title: "Confusion or Nihilism: After Six Months of Heavy AI Use"
date: 2026-10-21
---

> I still do the software work I know well, with AI assistants and agents helping me. But I see less and less clearly, and I don't know where the future is.

At first, I thought AI was just a partner: a coworker who helped me get things done faster.

For the past six months I have used it almost obsessively. It is faster than me, and it knows more than I do. I knew that already. What really confuses me is something else: I can't see its method. All I get is an instant result.

We can no longer solve problems the old-fashioned way. The systems of the past felt straightforward. There might be a lot of magic inside, but once you took them apart, the core was simple. AI today is a black box that hides every detail.

## One bug hunt

Here is an example I ran into recently.

Our Android emulator ran on API 36. Every time it cold-booted, pulling a large file would drop the ADB connection, and a while later it would reconnect on its own. Without a cold boot, everything was fine.

Even with Claude, we were stuck on this for a long time. Claude can be a bit dumb sometimes: after a few failed retries, it stopped cold-booting (the default) and switched to a warm boot. With that change, the problem went away.

The workaround did work. But I didn't want to just route around it. I wanted to know what was actually broken underneath. I searched Google and dug through forums, and found nothing. The old-fashioned way depends on error messages, and at the application level this problem had none. ADB just dropped, then reconnected. With no error, we are usually stuck, and all we can do is post on a forum and wait for someone to answer.

Finally, I used the `/goal` command to give Claude a goal: dig to the bottom.

It took a long time, but it found the problem completely. It restarted the emulator again and again, tried different parameters, dumped the kernel logs, and found the few lines about data passing between the virtual machine and the host. The cause was a defect in the Linux kernel: sending 128 KB of data over vsock failed. Then it recalled the name of a well-known Google engineer who works on arm64 virtual machine changes, followed that name, and found the engineer's patch online. The patch fixed exactly what we were seeing.

In the end, we switched the system image from Android 36 to 36.1, and the problem was gone.

## The chill of understanding

Afterwards, I asked Claude to explain how it had found the answer. It said that, for security reasons, it couldn't reveal the internal process of the harness it runs in.

I could understand that; maybe it's a trade secret. But I kept asking, step by step, guiding it to explain what it had done, until I had dug out every detail.

The moment I saw the whole picture, a chill ran down my spine.

Not because I couldn't understand it. Precisely because I did understand it, I knew for sure: I couldn't have done this. Even with all of its tools in my hands, I wouldn't have known what to do, because I don't have that knowledge or that ability. This line of thinking is simply not one I could have come up with. Most frontend and application developers wouldn't know these details either, because this was no longer an application-level problem. It went deep into virtualization and the Linux kernel.

There are really two things here.

The first is that I can't see. A closed-source system doesn't show you the process in between; it just hands you the result. I can see which commands it ran, but not why it thought to look at those few lines of kernel logs. We don't know how it got there, so we have no way to learn the method. Today I can still dig it out by asking, step by step.

The second is that I can't get there. Even when I can see the path, I couldn't walk it myself. And if we stop exploring on our own and rely entirely on something that hands us answers, then even the places we can reach today will be out of reach tomorrow.

This is what confuses me most. If it can do everything, what do I still need to learn? But if I don't learn, when would I ever get the chance? You can learn the basics ahead of time, but most things are learned on the job, while you are using them. This bug hunt should have been a chance to learn, and it just handed me the answer.

Put those two things together, and the result is this: I am becoming a caveman. I hold the starship technology of *Interstellar* in my hands, with no idea of the principles behind it or how it was built.

Not that I have already become one. I am becoming one. Today I can still dig, so I'm not there yet. But this "becoming" is what scares me most.

## Who decides what is right

This feeling doesn't only show up when I'm debugging.

Often, when I want to do this or that, the AI tells me: that's impossible, and there's no need to do it. It just says no. It is deciding for me what is worth doing.

Take it one step further. Someday, people will no longer be able to control AI, because it will be far stronger than us. Once we cross that threshold, all we can do is trust it.

Maybe in the future we will need a kind of training: checking against multiple sources. We should be verifying anyway; that won't change. But what if every source I have points back to the same corpus, and that corpus has already been rewritten by AI? In the end, what counts as fact? People will have no way left to check.

## Who becomes the next senior engineer

There is one more thing I can't figure out.

Junior engineers should be the new blood of this profession. But fewer and fewer of them are being hired. Instead, senior engineers like me spend our days teaching AI how to do things right.

What makes a senior engineer valuable is a method for finding answers. So who will be the senior engineers of the future? Will we not need them anymore? Will we not need methodology anymore? Can AI generate methodology on its own? Or is AI itself the new methodology? The only methodology? Really?

Look back at that bug hunt. The problem got solved because someone at Google had walked that road by hand and written that patch. AI just remembered the name and found the person. And that person was once a junior too. If no new engineers walk these roads by hand anymore, whose patch will AI go looking for next time? When no one is writing anymore, the corpus will hold nothing but what AI wrote itself.

## Confusion, or nihilism

I worry about the future. How should we live alongside AI? What is my value?

Looking back at that bug hunt, one step was mine. Claude had already routed around the problem with a warm boot; I was the one who refused to stop there and told it to dig to the bottom. Maybe that is the bit of value I still have: knowing when not to settle for an answer.

But that judgment came from years of debugging things by hand. If people in the future stop digging by hand, where will they learn not to settle?

And beyond that: when AI can define meaning, what is a human?

I don't have answers to these questions.
