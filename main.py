from fastapi import FastAPI

app = FastAPI(
    title='Калькулятор'
)


@app.get("/calculator")
def calculator(num_1: int, num_2: int, oper: str):
    if oper == '+':
        return {'Результат': num_1 + num_2}
    if oper == '-':
        return {'Результат': num_1 - num_2}
    if oper == '*':
        return {'Результат': num_1 * num_2}
    if oper == '/':
        return {'Результат': num_1 / num_2}
    if oper == '**':
        return {'Результат': num_1 ** num_2}
    else:
        return {'-'}
