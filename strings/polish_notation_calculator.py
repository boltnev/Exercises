import unittest


def evaluate(expression):
    result = None
    expr = expression[:]
    stack = []
    while len(expr) != 0:
        op = expr.pop(0)
        if op.isdigit():
            stack.append(int(op))
        elif op == "+":
            a = stack.pop()
            b = stack.pop()
            stack.append(b+a)
        elif op == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif op == "*":
            a = stack.pop()
            b = stack.pop()
            stack.append(b*a)
        elif op == "/":
            a = stack.pop()
            b = stack.pop()
            stack.append(b/a)
        else:
            assert(False), "bad input: {}".format(op)

    result = stack[-1]

    return result


class CalcTest(unittest.TestCase):


    def test_one_plus_two(self):
        expression = ["1", "2", "+"]
        result = evaluate(expression)
        self.assertEqual(result, 3)

    def test_minus(self):
        expression = ["10", "5", "-"]
        result = evaluate(expression)
        self.assertEqual(result, 5)

    def test_multiply(self):
        expression = ["10", "5", "*"]
        result = evaluate(expression)
        self.assertEqual(result, 50)

    def test_divide(self):
        expression = ["10", "5", "/"]
        result = evaluate(expression)
        self.assertEqual(result, 2)

    def test_complex_expression(self):
        expression = ["10", "5", "/", "8", "3", "-", "*"]
        result = evaluate(expression)
        self.assertEqual(result, 10)

if __name__=="__main__":
    unittest.main()
