title: protobuf
date: 2017-05-22 16:22:29
tags: google
---

其实我注意到项目中有些 gem 依赖一个叫做 [protobuf](https://github.com/google/protobuf) 的 gem 很久了. 一直都没有去试图了解这是什么东西. 知道今天阅读 mesos 书籍的时候才知道它其实是一个数据序列化的中立工具. 提供了多种语言的实现. 自然而然地就让我想到公司一直使用的 Thrift 工具. 简单地 stackoverflow 了一下知道他们基本就是提供同一种服务的. 但是有些许区别.

1. 支持的语言种类有多有少

    | Language     | Protobuf  | Thrift |
    | ------------ | --------- | ------ |
    | Android Java | Y         | (Java) |
    | C#           | Y         | Y      |
    | C++          | Y         | Y      |
    | D            | N         | Y      |
    | Delphi       | N         | Y      |
    | Erlang       | N         | Y      |
    | Go           | Y         | Y      |
    | Haskell      | N         | Y      |
    | Haxe         | N         | Y      |
    | Java         | Y         | Y      |
    | JavaScript   | (Node.js) | Y      |
    | OCaml        | N         | Y      |
    | Objective-C  | Y         | Y      |
    | PHP          | N         | Y      |
    | Perl         | N         | Y      |
    | Python       | Y         | Y      |
    | Ruby         | Y         | Y      |
    | Smalltalk    | N         | Y      |

2. 特性有些许差别

    1. Thrift 支持 'exceptions'
    2. Protocol Buffers 有更好的文档以及例子
    3. Thrift 内置了 `Map` 和 `Set` 类型
    4. Protocol Buffers 允许实现 "extensions" - 你可以继承一个外部的 proto 来添加新的 field, 同时也允许外部代码来操纵值. 这些 Thrift 是无法实现的
    5. Protocol Buffers 更加易读

REF: http://stackoverflow.com/questions/69316/biggest-differences-of-thrift-vs-protocol-buffers
