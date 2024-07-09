import re
def load_cool_program(file: str):
    def parse(line):
        #算术操作
        assignment_match=re.match(r'([a-zA-Z]+)\s*([\+\-\*/]?=)\s*([a-zA-Z0-9]+)',line)
        #一个或多个（字母，符号，字母或数字）
        #([\+\-\*/]?=)中？表示前面的表达式可以出现0次或1次，=直接匹配表达式的=
        if assignment_match:
            return 'assignment',assignment_match.groups()
        #结果
        result_match=re.match(r'\(return\)\s*([a-zA-Z0-9]+)',line)
        if result_match:
            return 'result',result_match.groups(1)
        raise ValueError(f"Invalid line:{line}")
        #f允许在字符串中嵌入表达式
    variables={}#存储变量值,字典
    output=[]
    for line in file.strip().split('\n'):#去除表达式两边的空格
        line=line.strip()
        if not line:
            continue#空串
        a,b=parse(line)
        #b根据指令类型解构
        if a=='assignment':
            variable,operator,expression=b
            #变量，操作符，操作
            if expression.isdigit():#=后面由单个数字组成
                value=int(expression)
            else:
                if expression not in variables:
                    output.append('Undefined variable')
                    continue
                value=variables[expression]
            if operator == '=':
                variables[variable]=value
            elif operator == '+=':
                variables[variable]+=value
            elif operator == '-=':
                variables[variable]-=value
            elif operator == '*=':
                variables[variable]*=value
            elif operator =='/=':
                variables[variable]//=value #整除
        elif a == 'result':
            if b.isdigit():
                output.append(b)#如果是数字就直接返回
            else:
                output.append(str(variables.get(b,'Undefined variable')))
                #如果字典里面没有定义，就输出Undefined variable
    return '\n'.join(output)
    #join用于将列表中的字符串元素连接成一个长字符串