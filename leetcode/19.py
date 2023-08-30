
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                stack.append(int(t))
            else:
                num_1 = stack.pop()
                num_2 = stack.pop()

                if t == "+":
                    temp = (num_2 + num_1)
                    stack.append(temp)
                elif t == "-":
                    temp = (num_2 - num_1)
                    stack.append(temp)
                elif t == "/":
                    temp = int(num_2 / num_1)
                    stack.append(temp)
                else:
                    temp = (num_2 * num_1)
                    stack.append(temp)


        return stack.pop()

s = Solution()
# print(s.evalRPN(["2","1","+","3","*"]))
# print(s.evalRPN(["4","13","5","/","+"]))
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))