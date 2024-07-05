# Coolang

## 项目介绍

请编写一个 Coolang 语言，它的 EBNF 语法如下：

```ebnf
assignment ::=  variable_name ws operator ws expression

operator   ::= "+=" | "-=" | "*=" | "/=" | "="

expression ::= variable_name | integer

variable_name ::= letter+

print_statement ::= "(return)" ws expression

letter ::= uppercase_letter | lowercase_letter
uppercase_letter ::= "A"..."Z"
lowercase_letter ::= "a"..."z"

integer      ::=  nonzerodigit digit*
nonzerodigit ::=  "1"..."9"
digit        ::=  "0"..."9"

ws ::= " "*
```
你不必看懂上面的 EBNF，接下来我们通俗的讲解一下我们需要实现什么。

对于 Coolang 来说，它不关注语句中存在的空格符。
每一行仅有一次操作，且操作仅有六种，即加、减、乘、除、赋值和打印语句。
下面语句中，后接 `#` 符号为解释，样例测试中不存在该符号。

```
A = 10 # 将 10 赋给变量 A
B = A # 将变量 A 的值赋给变量 B

A += B # 将 A + B 的值赋给变量 A
A *= 2 # 将 A * 2 的值赋给变量 A
B /= 2 # 将 B / 2 的值赋给变量 B （请注意，该语言不存在小数，请将结果向下取整）
B -= A # 将 B - A 的值 赋给变量 B
(return) B # 打印变量 B 的值
(return) 534 # 打印数字 534
(return) C # 不存在这个变量时，请输出 `Undefined variable`
```

## 项目目标

你只需要补全 `src/coolang` 目录下的 `load_cool_program` 函数，并且通过所有测试。

你可以创建任何新的文件，做任何修改，但禁止修改 `tests` 目录下代码。

### 样例输入
函数将会接收到一个字符串 `file` ，样例如下：

```
A=1
A += 3
(return) A
(return) C
```

### 样例输出

```
3
Undefined variable
```

## 样例测试

你可以通过输入 `pdm run pytest` 来检测代码运行结果

## 其它要求

- 请独立完成项目的编写，不要与他人交流
- 请不要借助 AI 编写代码

## 灵感来源

- 游戏 A=B